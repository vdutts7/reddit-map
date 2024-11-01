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