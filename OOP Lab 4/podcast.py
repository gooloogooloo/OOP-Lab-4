from audio_file import AudioFile
import datetime


class Podcast(AudioFile):

    def __init__(self, title: str, artist: str, runtime: str, pathname: str, filename: str, series: str,
                 episode_date: datetime, progress: datetime.time, season: str = None, episode_number: int = None):
        super().__init__(title, artist, runtime, pathname, filename)
        self._series = series
        self._season = season
        self._episode_number = episode_number
        if self.__validate_datetime(episode_date):
            self._episode_date = episode_date
        self._progress = progress

    def get_description(self):
        if self._episode_number is None and self._season is None:
            return f"{self._series}: {self._title}, {self._episode_date} ({self._runtime} mins)"
        elif self._episode_number is None:
            return f"{self._series}: {self._title}, {self._episode_date}, {self._season} ({self._runtime} mins)"
        else:
            return f"{self._series}: {self._title}, {self._episode_date}, {self._season} Episode" \
                   f" {self._episode_number} ({self._runtime} mins)"

    def meta_data(self):
        return {'title': self._title,
                'artist': self._artist,
                'series': self._series,
                'season': self._season,
                'episode_number': self._episode_number,
                'episode_date': self._episode_date,
                'progress': self._progress,
                'runtime': self._runtime,
                'pathname': self._pathname,
                'filename': self._filename,
                'play_count': self._usage._play_count,
                'last_played': self._usage._last_played,
                'rating': self.user_rating
                }

    def set_progress(self, progress: datetime.time):
        if type(progress) == datetime.time:
            self._progress = progress
        else:
            raise ValueError("Progress not time object")

    def get_progress(self):
        return self._progress

    def __validate_datetime(self, episode_date):
        if type(episode_date) == datetime.date:
            return True
        else:
            raise ValueError("Episode date invalid")
