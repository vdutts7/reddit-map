import pandas as pd
import pyarrow as pa
from nomic import atlas
from prawcore.exceptions import PrawcoreException
import praw
import os

client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')
nomic_api_key = os.getenv('NOMIC_API_KEY')


def scrape_reddit_comments(reddit: praw.Reddit, submission: praw.models.reddit.submission.Submission) -> list:
    # Function to scrape Reddit comments
    max_attempts = 5  
    current_attempt = 0
    while current_attempt < max_attempts:
        try:
            submission.comments.replace_more(limit=None)
            time.sleep(1)  # Add a delay between replace_more() calls
            comments = fetch_all_comments(submission)
            print(f"Number of comments fetched: {len(comments)}")
            return comments
        except PrawcoreException as e:
            if e.response and e.response.status_code == 429:
                delay = 2 ** current_attempt  
                print(f"Rate limit exceeded. Retrying in {delay} seconds...")
                time.sleep(delay)
                current_attempt += 1
            else:
                print(f"Error scraping comments: {e}")
                return []

    print("Max retry attempts reached. Could not fetch comments.")
    return []



def fetch_all_comments(submission: praw.models.reddit.submission.Submission) -> list:
    # Function to fetch all comments from a Reddit submission
    comments = []
    submission.comments.replace_more(limit=None)
    time.sleep(1)
    for comment in submission.comments.list():
        comment_data = {
            'text': comment.body,
            'author': comment.author.name if comment.author else '[deleted]',
            'score': comment.score,
            'depth': comment.depth,
            'created_utc': comment.created_utc
        }
        comments.append(comment_data)
        comments.extend(fetch_replies(comment))
    return comments

def fetch_replies(comment: praw.models.reddit.comment.Comment) -> list:
    # Function to fetch replies to a Reddit comment
    replies = []
    if isinstance(comment, praw.models.reddit.comment.Comment):
        if hasattr(comment, 'replies') and isinstance(comment.replies, praw.models.comment_forest.CommentForest):
            comment.replies.replace_more(limit=None)
            time.sleep(1)
            for reply in comment.replies.list():
                reply_data = {
                    'text': reply.body,
                    'author': reply.author.name if reply.author else '[deleted]',
                    'score': reply.score,
                    'depth': reply.depth,
                    'created_utc': reply.created_utc
                }
                replies.append(reply_data)
                replies.extend(fetch_replies(reply))
    return replies


def comments_to_arrow_table(comments: list) -> pa.Table:
    # Function to convert comments into an Arrow Table for efficient data handling
    df = pd.DataFrame(comments)
    arrow_table = pa.Table.from_pandas(df)
    return arrow_table


def main():
    # Function to automate Reddit comment mapping with Nomic Atlas

    # Retrieve Reddit API credentials and Nomic API key from environment variables
    client_id = os.getenv('REDDIT_CLIENT_ID')
    client_secret = os.getenv('REDDIT_CLIENT_SECRET')
    user_agent = os.getenv('REDDIT_USER_AGENT')
    reddit_url = input("Enter Reddit post URL: ")
    nomic_api_key = os.getenv('NOMIC_API_KEY')

    # Initialize Reddit instance
    reddit = get_reddit_instance(client_id, client_secret, user_agent)
    submission = reddit.submission(url=reddit_url)

    # Scrape Reddit comments
    comments = scrape_reddit_comments(reddit, submission)
    arrow_table = comments_to_arrow_table(comments)

    try:
        map_name = f"[Reddit Comment Thread] {submission.title}"  

        # Map data using Nomic Atlas
        dataset = atlas.map_data(data=arrow_table,
                                 indexed_field='text',
                                 description='Reddit comments mapped via automation.',
                                 topic_model=True,
                                 identifier=map_name)
        if dataset and 'id' in dataset:
            print("Map created on Atlas with ID:", dataset['id'])
            print("All done! Visit the map link to see the status of your map build.")
        else:
            print("Map creation failed. Dataset ID not found in response.")
    except Exception as e:
        print(f"An error occurred while building map on Atlas: {e}")

def get_reddit_instance(client_id: str, client_secret: str, user_agent: str) -> praw.Reddit:
    # Function to create a Reddit instance
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )
    return reddit

if __name__ == "__main__":
    main()