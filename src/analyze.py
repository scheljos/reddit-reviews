from textblob import TextBlob
import praw
# import os

# print(os.getcwd())

# Create reddit instance
reddit = praw.Reddit(client_id="xt5pmMV2eaKApw",
client_secret="Q_u2kTLSRuo2XRIvighrD0JXc1o7Cg",
user_agent="reddit-reviews sentiment analysis by u/Lost_You4257",
)

# TODO: Is web-app vulnerable because authentication
# details are hard coded?

# praw.ini file not being found, giving errors when
# Reddit instance initialized this way:
# reddit = praw.Reddit(site_name='api-access')

# Product to be searched
# TODO: This should be a variable based on web-app input
product = "pixel 4a"

# TODO: Loop through the submissions, calculating polarity of title & comments
# Weight text with more upvotes higher than text with less upvotes
# Find the average polarity, apply it to a scale for a rating
for submission in reddit.subreddit("all").search(product):
    print(submission.title)

# TODO: Communicate this rating to the front end

# TODO: Allow specific subreddits to be searched; provide examples of good ones

# TODO: Find common words associated with the product (a set number, ordered
# by frequency)