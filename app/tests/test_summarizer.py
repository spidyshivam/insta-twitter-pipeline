import pytest
from unittest.mock import patch
from app.services.summarizer import summarize_caption

@pytest.fixture
def mock_gemini_response():
    class MockResponse:
        candidates = [
            type("Candidate", (), {
                "content": type("Content", (), {
                    "parts": [type("Part", (), {"text": "Summarized tweet content."})]
                })
            })
        ]
    return MockResponse()

@patch("app.services.summarizer.genai.GenerativeModel.generate_content")
def test_summarize_caption(mock_generate_content, mock_gemini_response):
    mock_generate_content.return_value = mock_gemini_response

    caption = "This is a long Instagram caption that needs to be summarized into a tweet."
    result = summarize_caption(caption)

    assert isinstance(result, str)
    assert result == "Summarized tweet content."
