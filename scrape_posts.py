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

# subreddits to scrape from
subreddits = ["AskReddit", "CreepyAskReddit", "ask"]

# filter political posts (can be flagged by youtube)
# if any of these words are found in a subreddit title, that subreddit will be filtered out.
banned_words = [
    "epstein", "trump", "clinton", "doj",
    "supreme court", "ice", "protest", "gaza",
    "election", "israel", "qanon"
    ]
def filter_post(submission):
    for word in banned_words:
        if word in submission.title.lower():
            return False
    return True

print("The following posts will be used:")
for subreddit_name in subreddits:
    print(f"\nFrom r/{subreddit_name}:")
    for submission in reddit.subreddit(subreddit_name).top(time_filter='week', limit = 5):
        if filter_post(submission):
            print(submission.title)