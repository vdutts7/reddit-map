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