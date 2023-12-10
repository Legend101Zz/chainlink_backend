import praw
import sys

subreddit_name = sys.argv[1]
post_id = sys.argv[2]

# Create a Reddit instance
reddit = praw.Reddit(
    client_id='IHoJop-M58PbO-h3NnbS7w',
    client_secret='5ysclq7UJe1-pG5h-3ZPeZvYgLlEbA',
    user_agent='chainlink',
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
