import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
CLIENT_ID = os.getenv("TWITTER_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITTER_CLIENT_SECRET")


def post_tweet(tweet: str):

    try:
        auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET)
        auth.set_access_token(
            ACCESS_TOKEN,
            ACCESS_SECRET,
        )

        newapi = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_SECRET,
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
        )
        api = tweepy.API(auth)
        media = api.media_upload(os.path.join(os.getcwd(), "image", "image.png"))
        response = newapi.create_tweet(text=tweet, media_ids=[media.media_id])
        print(response)
        return response
        return {
            "status": "Tweet posted successfully",
            "tweet_id": response.data['id'],
            "text": response.data['text']
        }
    except tweepy.TweepyException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}
