# Dictionary Bot
### The Twitter Bot **@GetBadJokes**

Here is the code for my Twitter **Bad Joke Bot**.
You can view and experiment with the code, but I don't recommend launching a Bad Joke Bot similar to mine unless you change key features (such as good jokes) as Twitter users typically will only follow one account/bot if there are multiple providing the same service.

## Libraries Used

I used **Twython** to access Twitter - it's a very simple module to access Twitter through Python. It uses Twitter APIs, so your account will have to be a Twitter developer to get those APIs. Twython has a large amount of uses, but I only use the Tweet functionality. My other Twitter bot, @ADictionaryBot, uses Tweepy. I used Twython here in an attempt to remove any possibility of conflict by using the same module at the same time on the same Raspberry Pi. 

I used **Random** to choose a random joke - this is pretty simple and I'm sure most people who have used Python have used this at some point. Essentially, it picks a random word from *jokes.txt* and then replies with that.

## Jokes

**jokes.txt** is a text file with many jokes. Jokes were sourced from different websites and added to this list. If you'd like to submit a joke, then email *badjokebot@itsnoahevans.co.uk* with your joke. Make sure they're bad, but funny!

**ids_replied_to.txt** contains Tweets that the bot has replied to in order to stop the bot from replying to the same mention multiple times.

## Thanks!

A huge thanks to **Geek Tech Stuff** who posted their Twitter auto-reply bot code online for others to use. Without you, it would have been much harder for me! I changed a few things and edited a few lines here and there to make it work better for my use case.
