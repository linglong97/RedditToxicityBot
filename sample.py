import praw
import time


'''
Sample bot goes through to learn PRAW,
and uses a simple model to flag comments in the '2007scape' subreddit.
This is one of my favourite games to play and there is a lot of toxic comments. 
I want to search for comments, and build a model which predicts the upvotes and downvotes based purely on 
sentiment analysis, or more specifically the toxicity of the comment.
'''


#authentication token
r = praw.Reddit(client_id='HXn5Vr_ub1_0OQ',
                client_secret='xohyqSpivQ0v017HlUUHydsVyI8',
                user_agent='sample bot v0.1',
                username='blahblahboar',
                password='noobies4life')
print r.user.me()
sub = r.subreddit('2007scape')
comments = sub.stream.comments()

'''
polite_users = set()   # to avoid duplicates
for i in xrange(0,10):  # Run the loop 10 times
    comments = r.get_comments('askreddit')
    for comment in comments:
        body = comment.body.lower()
        if body.find("thank") != -1 or body.find("please") != -1:
            polite_users.add(comment.author)
    time.sleep(120)   # Sleep for 2 minutes
'''
new = []
for comment in comments:
	print comment
