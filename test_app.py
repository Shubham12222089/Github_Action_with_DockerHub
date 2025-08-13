from app import get_message

def test_get_message():
    assert get_message() == "Automated using CI/CD pipelines."