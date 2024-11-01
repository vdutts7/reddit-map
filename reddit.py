import pandas as pd
from prawcore.exceptions import PrawcoreException
import praw
import os
from dotenv import load_dotenv
import time

load_dotenv()

client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')

def scrape_reddit_comments(reddit: praw.Reddit, submission: praw.models.reddit.submission.Submission) -> list:
    # Function to scrape Reddit comments
    max_attempts = 5  
    current_attempt = 0
    while current_attempt < max_attempts:
        try:
            # Load all comments at once
            submission.comments.replace_more(limit=None)
            comments = []
            
            # Use comment_forest's list() method to get all comments at once
            for comment in submission.comments.list():
                comment_data = {
                    'text': comment.body,
                    'author': comment.author.name if comment.author else '[deleted]',
                    'score': comment.score,
                    'depth': comment.depth,
                    'created_utc': comment.created_utc
                }
                comments.append(comment_data)
            
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

def get_reddit_instance(client_id: str, client_secret: str, user_agent: str) -> praw.Reddit:
    # Function to create a Reddit instance
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )
    return reddit

def main():
    # Function to scrape Reddit comments and save to CSV
    reddit_url = input("Enter Reddit post URL: ")

    # Initialize Reddit instance
    reddit = get_reddit_instance(client_id, client_secret, user_agent)
    submission = reddit.submission(url=reddit_url)

    # Scrape Reddit comments
    comments = scrape_reddit_comments(reddit, submission)
    
    # Convert to DataFrame and save as CSV
    if comments:
        df = pd.DataFrame(comments)
        filename = f"reddit_comments_{int(time.time())}.csv"
        df.to_csv(filename, index=False)
        print(f"Comments saved to {filename}")
    else:
        print("No comments were scraped.")

if __name__ == "__main__":
    main()