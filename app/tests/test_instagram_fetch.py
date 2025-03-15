import pytest
from unittest.mock import patch, MagicMock
from app.services.instagram_fetch import fetch_latest_instagram_post

@pytest.fixture
def mock_instagram_post():
    return MagicMock(
        pk="12345",
        media_type=1,
        thumbnail_url="https://example.com/image.jpg",
        caption_text="Breaking News: Major Event Happened!"
    )

@patch("app.services.instagram_fetch.Client")
def test_fetch_latest_instagram_post(mock_client, mock_instagram_post):

    mock_instance = mock_client.return_value
    mock_instance.login.return_value = None
    mock_instance.user_info_by_username.return_value = MagicMock(pk="12345")
    mock_instance.user_medias.return_value = [mock_instagram_post]

    response = fetch_latest_instagram_post()

    assert isinstance(response, dict)
    assert "caption" in response
    assert "image_url" in response
    assert response["caption"] == "Breaking News: Major Event Happened!"
    assert response["image_url"] == "https://example.com/image.jpg"

    mock_instance.logout.assert_called_once()
