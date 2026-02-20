import os
import praw
from dotenv import load_dotenv

# must have a .env file with environment variables
load_dotenv()

# https://www.reddit.com/prefs/apps/
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')

reddit = praw.Reddit (
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    user_agent = USER_AGENT,
)

subreddits = ["AskReddit", "CreepyAskReddit", "ask"]

for subreddit_name in subreddits:
    for submission in reddit.subreddit(subreddit_name).top(time_filter='week', limit = 5):
        print(submission.title)