import praw
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

subreddit_name = sys.argv[1]
post_id = sys.argv[2]

# Create a Reddit instance
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

# Access the specified subreddit and post
subreddit = reddit.subreddit(subreddit_name)
post = reddit.submission(id=post_id)

# Access information about the post
upvotes = post.ups
downvotes = post.downs
comments_count = post.num_comments

print(f"Upvotes: {upvotes}")
print(f"Downvotes: {downvotes}")
print(f"Number of Comments: {comments_count}")
