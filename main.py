#Import Libraries
from twython import Twython
import random
import time

#Set Font For Print
class colour:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

#Connect to Twitter API
from BadJokeBotAuth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#Print Program Status
print(colour.PURPLE, colour.BOLD, 'Imported Libraries and Connected to Twitter APIs', colour.END)

#Open replied to file
repliedTo = []
with open('BadJokeBot-repliedTo.txt', 'r') as filehandle:
    filecontents = filehandle.readlines()

    for line in filecontents:
        # remove linebreak which is the last character of the string
        current_place = line[:-1]
        # add item to the list
        repliedTo.append(current_place)

#Print Program Status
print(colour.BLUE, colour.BOLD, 'Opened Replied To File', colour.END)

#Start Loop (run forever)
#Print Program Status
print(colour.BLUE, colour.BOLD, 'Starting Loop', colour.END)
while True:
    # Search Tweets
    print(colour.BLUE, colour.BOLD, 'Searching Tweets', colour.END)
    search_term = '@GetBadJokes #GiveMeAJoke'
    results = twitter.cursor(twitter.search, q=search_term)

    # Reply To Each Result
    for result in results:
        #Define User Metadata
        #Print Program Status
        print(colour.BLUE, colour.BOLD, 'Defining User Metadata', colour.END)
        name = result['user']
        screen_name = name['screen_name']
        creation_date = result['created_at']
        tweet_txt = result['text']
        id = result['id']
        print(colour.BLUE, colour.BOLD, 'User Tweet:', tweet_txt, colour.END)

        #Check for Skip Reasons
        #Print Program Status
        print(colour.BLUE, colour.BOLD, 'Checking for Skip Reasons', colour.END)
        id = str(id)
        #Already replied
        if id in repliedTo:
            print(colour.RED, colour.BOLD, 'Skipped as already replied to', colour.END)
            continue
        #Retweet
        if 'RT' in tweet_txt:
            print(colour.RED, colour.BOLD, 'Skipped as Tweet is a Retweet', colour.END)
            continue
        #Reply to self
        if '@GetBadJokes' in screen_name:
            print(colour.RED, colour.BOLD, 'Skipped as replying to self', colour.END)
            continue
        #Reply To Tweets
        else:
            #Pick Random Joke
            with open('jokes.txt') as jokesList:
                #Scan File
                jokes = jokesList.readlines()
                #Set randomJoke as generated joke
                randomJoke = random.choice(jokes)
                #Set randomJoke as a String
                randomJoke = str(randomJoke)
                #Remove blank line
                randomJoke = randomJoke.replace("\n", "")
                #Print Program Status
                print(colour.BLUE, colour.BOLD, 'Chosen random joke', colour.END)
                #Define hand;le
                twitter_handle = '@' + screen_name
                #Define reply
                message = twitter_handle + " " + randomJoke
                #Print Program Status
                print(colour.BLUE, colour.BOLD, 'Defined reply', colour.END)
                #Post reply
                twitter.update_status(status=message, in_reply_to_status_id=id)
                #Print Program Status
                print(colour.GREEN, colour.BOLD, 'Replied to ', twitter_handle + ':', message, colour.END)
                #Add reply to list
                id = int(id)
                ids_replied_to.append(id)
                with open('BadJokeBot-repliedTo', 'w') as filehandle:
                    filehandle.writelines("%s\n" % place for place in ids_replied_to)
                #Print Program Status
                print(colour.BLUE, colour.BOLD, 'Saved Tweet ID to list', colour.END)
                #Wait 60 seconds to abide by Twitter Rate Limits
                print(colour.BLUE, colour.BOLD, 'Waiting 60 seconds to reply again...', colour.END)
                time.sleep(60)
                #Start Again
