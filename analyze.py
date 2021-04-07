from textblob import TextBlob
import praw
# import os

# print(os.getcwd())

# Create reddit instance
reddit = praw.Reddit(client_id="xt5pmMV2eaKApw",
client_secret="Q_u2kTLSRuo2XRIvighrD0JXc1o7Cg",
user_agent="reddit-reviews sentiment analysis by u/Lost_You4257",
)

# praw.ini file not being found, giving errors when
# Reddit instance initialized this way
# reddit = praw.Reddit(site_name='api-access')

# Product to be searched
product = "pixel 4a"

# Loop through the 
for submission in reddit.subreddit("all").search(product):
    print(submission.title)

