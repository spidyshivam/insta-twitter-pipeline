import pytest
from unittest.mock import patch, MagicMock
import os
from app.services.twitter_api import post_tweet

@pytest.fixture
def mock_twitter_response():
    class MockResponse:
        data = {"id": "123456789", "text": "Tweeted successfully!"}
    return MockResponse()

@patch("app.services.twitter_api.tweepy.Client.create_tweet")
@patch("app.services.twitter_api.tweepy.API.media_upload")
def test_post_tweet(mock_media_upload, mock_create_tweet, mock_twitter_response):
    mock_media_upload.return_value = MagicMock(media_id="987654321")
    mock_create_tweet.return_value = mock_twitter_response

    tweet_text = "This is a test tweet."
    response = post_tweet(tweet_text)

    assert isinstance(response, object)
    assert response.data["id"] == "123456789"
    assert response.data["text"] == "Tweeted successfully!"

    mock_media_upload.assert_called_once_with(os.path.join(os.getcwd(), "image", "image.png"))
    mock_create_tweet.assert_called_once_with(text=tweet_text, media_ids=["987654321"])
