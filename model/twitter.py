import os

import tweepy


class Twitter_Client:
    """Instance for interacting with the Twitter API"""

    def __init__(self) -> None:
        """Constructor"""
        auth = tweepy.OAuthHandler("REPLACE WITH YOUR KEYS", "REPLACE WITH YOUR KEYS")
        auth.set_access_token("REPLACE WITH YOUR TOKENS", "REPLACE WITH YOUR TOKENS")
        self.api = tweepy.API(auth)

    def create_tweet(self, text_content: str) -> None:
        """Create a tweet with specified text content"""
        self.api.update_status(text_content)

    def create_tweet_with_media(self, text_content: str, media_path: str) -> None:
        """Create a tweet with specified text content and media content"""
        self.api.update_status_with_media(status=text_content, filename=os.path.join(os.getcwd(), media_path))
