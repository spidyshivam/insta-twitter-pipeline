import logging
import os
import requests
from instagrapi import Client
from app.config import Config

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def fetch_latest_instagram_post():
    cl = Client()

    try:
        logging.info("Attempting to log in to Instagram...")
        cl.login(Config.INSTAGRAM_USERNAME, Config.INSTAGRAM_PASSWORD)
        logging.info("Instagram login successful.")

        bbc_user = cl.user_info_by_username("bbcnews")
        logging.info(f"Fetched user info for {bbc_user.username} (ID: {bbc_user.pk})")

        posts = cl.user_medias(bbc_user.pk, amount=10)
        logging.info(f"Retrieved {len(posts)} posts from {bbc_user.username}")

        for post in posts:
            if post.media_type in [1, 8]:  # 1=photo, 8=carousel
                image_url = post.thumbnail_url if post.media_type == 1 else post.resources[0].thumbnail_url
                logging.info(f"Found suitable post. Image URL: {image_url}")

                image_folder = os.path.join(os.getcwd(), "image")
                os.makedirs(image_folder, exist_ok=True)
                image_path = os.path.join(image_folder, "image.png")

                response = requests.get(image_url, stream=True)
                if response.status_code == 200:
                    with open(image_path, "wb") as f:
                        for chunk in response.iter_content(1024):
                            f.write(chunk)
                    logging.info(f"Image saved to {image_path}")

                return {
                    "caption": post.caption_text,
                    "image_url": image_url
                }

        logging.warning("No image posts found in the last 10 posts.")
        return {"error": "No image posts found in last 10 posts"}

    except Exception as e:
        logging.error(f"Error fetching Instagram post: {str(e)}", exc_info=True)
        return {"error": str(e)}

    finally:
        try:
            cl.logout()
            logging.info("Logged out from Instagram.")
        except Exception as e:
            logging.warning(f"Error logging out: {str(e)}")
