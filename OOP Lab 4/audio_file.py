import datetime
from usage_stats import UsageStats
from abc import abstractmethod


class AudioFile:
    """
    represents a simple audio player


    Class: ACIT 2515
    Author: Nicholas Janus
    ID: A01179897
    """
    def __init__(self, title: str, artist: str, runtime: str, pathname: str, filename: str) -> None:
        """Creates new song instance."""
        self._title = title
        self._artist = artist
        self._runtime = runtime
        self._pathname = pathname
        self._filename = filename
        self._user_rating = ""
        self._usage = UsageStats(datetime.date.today())

    def get_location(self) -> str:
        return self._pathname

    def get_play_count(self) -> int:
        return self._usage.play_count

    @abstractmethod
    def get_description(self) -> str:
        pass

    def update_usage(self) -> None:
        self._usage.last_played()
        self._usage.increment_usage_stats()

    def get_usage_stats(self) -> UsageStats:
        return self._usage

    @abstractmethod
    def meta_data(self) -> dict:
        pass

    @property
    def user_rating(self) -> str:
        """Getter for user_rating"""
        if self._user_rating != "":
            return self._user_rating
        else:
            return "None"

    @user_rating.setter
    def user_rating(self, rating: int) -> None:
        """Sets user rating of song instance"""
        if type(rating) == int and 0 <= int(rating) <= 5:
            self._user_rating = str(rating) + "/5"
        else:
            print(f"Error: Rating not int, or not in range 0-5")
