import unittest
import tweepy
import requests
import json
import twitter_info

## SI 206 - HW
## COMMENT WITH:
## Your section day/time: Thursday, 3:00pm
## Any names of people you worked with on this assignment:


## Write code that uses the tweepy library to search for tweets with three different phrases of the 
## user's choice (should use the Python input function), and prints out the Tweet text and the 
## created_at value (note that this will be in GMT time) of the first FIVE tweets with at least 
## 1 blank line in between each of them, e.g.


## You should cache all of the data from this exercise in a file, and submit the cache file 
## along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets 
## about "rock climbing", when we run your code, the code should use CACHED data, and should not 
## need to make any new request to the Twitter API.  But if, for instance, you have never 
## searched for "bicycles" before you submitted your final files, then if we enter "bicycles" 
## when we run your code, it _should_ make a request to the Twitter API.

## Because it is dependent on user input, there are no unit tests for this -- we will 
## run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

##SAMPLE OUTPUT
## See: https://docs.google.com/a/umich.edu/document/d/1o8CWsdO2aRT7iUz9okiCHCVgU5x_FyZkabu2l9qwkf8/edit?usp=sharing



## **** For extra credit, create another file called twitter_info.py that 
## contains your consumer_key, consumer_secret, access_token, and access_token_secret, 
## import that file here.  Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information 
## for an 'extra' Twitter account you make just for this class, and not your personal 
## account, because it's not ideal to share your authentication information for a real 
## account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these 
## with variables rather than filling in the empty strings if you choose to do the secure way 
## for EC points

## Set up your authentication to Twitter
consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Set up library to grab stuff from twitter with your authentication, and 
# return it in a JSON-formatted way

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except 
## 		statement shown in class.

cache_fname = "cached_results.json"
try:
    cache_file = open(cache_fname, 'r')
    cache_contents = cache_file.read() 
    cacheDict = json.loads(cache_contents) 
    cache_file.close() 
except:
    cacheDict = {}


## 2. Write a function to get twitter data that works with the caching pattern, 
## 		so it either gets new data or caches data, depending upon what the input 
##		to search for is. 
def get_t(search_term):
    if search_term in cacheDict:
        return cacheDict[search_term] # if search_term is already in the cache, just return that information instead of requesting new info
    else:
        print ("Requesting new data...")
        api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) # grabbing twitter data with authentications 
        results = api.search(q = search_term, count = 5) # dictionary; searching for 5 tweets containing user inputted search term
        try:
            cacheDict[search_term] = results
            dumped_json_cache = json.dumps(cacheDict) # converting cacheDict to json formatted string
            fw = open(cache_fname, "w") # opening cache to write to it
            fw.write(dumped_json_cache) # writing to cache
            fw.close()
            return cacheDict[search_term]
        except:
            print ("Wasn't in cache, not a valid search")
            return None


## 3. Using a loop, invoke your function, save the return value in a variable, and explore the 
##		data you got back!


## 4. With what you learn from the data -- e.g. how exactly to find the 
##		text of each tweet in the big nested structure -- write code to print out 
## 		content from 5 tweets, as shown in the linked example.


prompt3times = ["prompt1", "prompt2", "prompt3"] # making a list with 3 elements so the for loop runs 3 times

for t in prompt3times:
    user_search = input("Enter search term: ")

    list_of_tweets = get_t(user_search)["statuses"] # getting a list of 5 tweets' statuses (which is a big dictionary)
    for tweet in list_of_tweets:
        print(tweet["text"]) # getting the text from each tweet
        print("CREATED AT: ", tweet["created_at"]) # getting the time each tweet was created (GMT time)
        print("\n")


