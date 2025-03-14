from instagrapi import Client
from app.config import Config
import requests
import os

def fetch_latest_instagram_post():
    cl = Client()

    try:
        cl.login(Config.INSTAGRAM_USERNAME, Config.INSTAGRAM_PASSWORD)

        bbc_user = cl.user_info_by_username("bbcnews")

        posts = cl.user_medias(bbc_user.pk, amount=10)

        for post in posts:
            if post.media_type in [1, 8]:  # 1=photo, 8=carousel
                image_url = post.thumbnail_url if post.media_type == 1 else post.resources[0].thumbnail_url

                image_folder = os.path.join(os.getcwd(), "image")
                os.makedirs(image_folder, exist_ok=True)
                image_path = os.path.join(image_folder, "image.png")

                response = requests.get(image_url, stream=True)
                if response.status_code == 200:
                    with open(image_path, "wb") as f:
                        for chunk in response.iter_content(1024):
                            f.write(chunk)

                return {
                    "caption": post.caption_text,
                    "image_url": image_url
                }

        return {"error": "No image posts found in last 10 posts"}

    except Exception as e:
        return {"error": str(e)}

    finally:
        cl.logout()
