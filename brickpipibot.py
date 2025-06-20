import os
from dotenv import load_dotenv
import praw
from praw import Reddit
from praw.models import Submission, Subreddit, Comment

load_dotenv()

CLIENT = os.getenv("CLIENT_ID")
SECRET = os.getenv("CLIENT_SECRET")
BOT_USERNAME = os.getenv("BOT_USERNAME")
BOT_PASSWORD = os.getenv("BOT_PASSWORD")
TOKEN = os.getenv("REFRESH_TOKEN")

reddit=praw.Reddit(
    client_id=CLIENT,
    client_secret=SECRET,
    token=TOKEN,
    user_agent="BrickPipiBot v.1.1",
    redirect_uri="http://localhost:8080",
    username=BOT_USERNAME,
    password=BOT_PASSWORD
)

print(reddit.user.me())

print(reddit.read_only)

subreddit=reddit.subreddit("AnarchyChess")
forced_moves = ["en passant", "il vaticano"]
brick_triggers = ["declin", "deny", "deni", "nt forced", "n't forced", "not forced"]
brick_reply = "*bricks your pipi*"

def process_comment(comment):
    normalized_comment=comment.body.lower()
    for forced_move in forced_moves:
        if forced_move in normalized_comment:
            for brick_trigger in brick_triggers:
                if brick_trigger in normalized_comment:
                    print("Pipi bricked")
                    comment.reply(brick_reply)
                    break

def process_submission(submission):
    normalized_post=[submission.selftext.lower(), submission.title.lower()]
    for forced_move in forced_moves:
        if forced_move in normalized_post:
            for brick_trigger in brick_triggers:
                if brick_trigger in normalized_post:
                    print("Pipi bricked")
                    submission.reply(brick_reply)
                    break

for comment in subreddit.stream.comments():
    process_comment(comment)
    
for submission in subreddit.stream.submissions():
    process_submission(submission)
        
                
                