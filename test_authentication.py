import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("zlGLMkY8cMI3ZzHvM83iuOx6R",
    "nfjjDVwgfUAZtQnsg3Ee8fdmFHjt9BboNrShiZtR6QfZ0B67tv")
auth.set_access_token("1260971179910868994-AV7mGZHs6z7lBTUrjs5J7oOZ3xFstG",
    "tJ4Y8gvLJvNZMPs2n28NEnQ1LWZga02ezJtEec0vCqdS6")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")

# api.update_status("This is the Arma bot")

# user = api.get_user("")
#
# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)
#
# print("Last 20 Followers:")
# for follower in user.followers():
#     print(follower.name)

# for tweet in api.search(q="Python", lang="en", rpp=10):
#     print(f"{tweet.user.name}:{tweet.text}")

search = "online resources"
numberOfTweets = 20

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.retweet()
        print('Retweeted the tweet')
    except:
        print('Retweet failed')

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

