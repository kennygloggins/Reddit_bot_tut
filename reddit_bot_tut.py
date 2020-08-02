# By: Kenny_G_Loggins
# Created on: 8/2/20, 3:57 PM
# File: reddit_bot_tut.py
# Project: Reddit_bot

import praw
import sqlite3
import re


# Sqlite db connect
replied_to = sqlite3.connect('replied_to.db')
c = replied_to.cursor()

# Uncomment first time running to create database
# c.execute('CREATE TABLE replied_to (subreddit  text, message text)')

# Grab bot info from praw.ini
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("DangerZoneboot")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

    # Check if we replied to post already
    c.execute("SELECT message FROM replied_to WHERE message=?", (submission.id,))
    if c.fetchone():
        pass
    else:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Botty bot says: Me too!!")
            c.execute("INSERT INTO replied_to VALUES (:subreddit, :message)", {'subreddit': 'DangerZoneboot',
                                                                               'message': submission.id})

# Commit Changes
replied_to.commit()
# Close Connection outside of tkinter loop
replied_to.close()