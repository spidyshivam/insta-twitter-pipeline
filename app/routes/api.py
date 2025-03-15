from fastapi import APIRouter
from app.services.instagram_fetch import fetch_latest_instagram_post
from app.services.summarizer import summarize_caption
from app.services.twitter_api import post_tweet

router = APIRouter()

@router.get("/instagram/latest-post")
def get_latest_instagram_post():
    return fetch_latest_instagram_post()

@router.post("/post-tweet/")
def post_summarized_tweet():

    data = fetch_latest_instagram_post()

    if not data:
        return {"error": "Failed to fetch Instagram post"}

    summarized_caption = summarize_caption(data["caption"])
    response = post_tweet(summarized_caption)

    return response
