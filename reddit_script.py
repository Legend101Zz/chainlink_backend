import praw

# Create a Reddit instance
reddit = praw.Reddit(
    client_id='IHoJop-M58PbO-h3NnbS7w',
    client_secret='5ysclq7UJe1-pG5h-3ZPeZvYgLlEbA',
    user_agent='chainlink',
)

# Access the Chainlink subreddit and a specific post
subreddit = reddit.subreddit('Chainlink')
post_id = '18dscwy'
post = reddit.submission(id=post_id)

# Access information about the post
upvotes = post.ups
downvotes = post.downs
comments_count = post.num_comments

print(f"Upvotes: {upvotes}")
print(f"Downvotes: {downvotes}")
print(f"Number of Comments: {comments_count}")
