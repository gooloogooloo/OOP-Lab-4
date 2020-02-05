from audio_file import AudioFile


class Song(AudioFile):
    def __init__(self, title: str, artist: str, runtime: str, pathname: str, filename: str, album: str,
                 genre: list = None):
        super().__init__(title, artist, runtime, pathname, filename)
        self._album = album
        self._genre = []
        if genre and self.__validate_genre(genre):
            self._genre.extend(genre)

    def get_description(self):
        if self._usage.play_count > 0 and self._user_rating != "":
            description = (f"{self._title} by {self._artist} from the album {self._album} added on {self._usage._date_added}. "
                    f"Runtime is {self._runtime}. Last played on {self._usage._last_played}. User ra"
                    f"ting is {self._user_rating}.")
        elif self._usage.play_count > 0:
            description = f"{self._title} by {self._artist} from the album {self._album} added on {self._usage._date_added}. " \
                   f"Runtime is {self._runtime}. Last played on {self._usage._last_played}. "
        else:
            description = f"{self._title} by {self._artist} from the album {self._album} added on {self._usage._date_added}. " \
                   f"Runtime is {self._runtime}."
        if len(self._genre) > 0:
            description += f" Genre(s): {', '.join(self._genre)}"
            return description
        else:
            return description

    def meta_data(self):
        return {'title': self._title,
                'artist': self._artist,
                'album': self._album,
                'genre': ', '.join(self._genre),
                'date_added': self._usage._date_added,
                'runtime': self._runtime,
                'pathname': self._pathname,
                'filename': self._filename,
                'play_count': self._usage._play_count,
                'last_played': self._usage._last_played,
                'rating': self.user_rating
                }

    def __validate_genre(self, genre):
        if type(genre) == list:
            return True
        else:
            raise ValueError("Genre not valid")
