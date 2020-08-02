# By: Kenny_G_Loggins
# Created on: 8/2/20, 3:57 PM
# File: reddit_bot_tut.py
# Project: Reddit_bot

import praw

# Grab bot info from praw.ini
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("modernwarfare")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")