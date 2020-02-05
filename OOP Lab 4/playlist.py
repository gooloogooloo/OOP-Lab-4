from audio_file import AudioFile
from usage_stats import UsageStats
from datetime import datetime
from typing import Union
from song import Song


class Playlist:
    """ represents a playlist

    Class: ACIT 2515
    Author: Nicholas Janus
    ID: A01179897
    """
    def __init__(self, name: str, description: str):
        """ creates playlist instance """
        self._name = name
        self._description = description

        self._playlist = []
        self._usage = UsageStats(datetime.now())

    def add_song(self, song: Song, posn: int = None) -> None:
        """ adds song to playlist instance either by position or to the end of list"""
        if posn is not None:
            if not Playlist.__valid_position(posn):
                self._playlist.append(song)
                raise ValueError("ValueError")
            else:
                self._playlist.insert(posn, song)
        else:
            self._playlist.append(song)

    def remove_song(self, song: Song) -> None:
        """ removes song from playlist instance """
        if song in self._playlist:
            self._playlist.remove(song)
        else:
            raise Exception("Error: Song not in playlist")

    def move_song(self, song: Song, posn: int) -> None:
        """ moves song to a specified position in playlist instance """
        if song in self._playlist and Playlist.__valid_position(posn) and 0 <= posn < len(self._playlist):
            self._playlist.insert(posn, self._playlist.pop(self._playlist.index(song)))
        else:
            raise ValueError("Song does not exist or invalid position")

    def list_songs(self) -> list:
        """ lists all songs within a playlist instance """
        song_list = []
        for i in range(len(self._playlist)):
            song = self._playlist[i]
            song_list.append(f"{i + 1}. {song._title.ljust(20)}{song._artist.ljust(20)}"
                             f"{song._album.ljust(20)}{song._runtime.ljust(20)}")
        return song_list

    def get_song_by_position(self, posn: int) -> Song:
        """ returns songs position in playlist instance """
        if Playlist.__valid_position(posn) and 0 <= posn < len(self._playlist):
            return self._playlist[posn - 1]

    def find_song(self, title: str = None, artist: str = None, album: str = None) -> Union[int, None]:
        """ finds song by title, artist, and/or album. returns none if no match found """
        if artist is None:
            artists = set([self._playlist.index(song) for song in self._playlist])
        else:
            artists = set([self._playlist.index(song) for song in self._playlist if song._artist == artist])
        if album is None:
            albums = set([self._playlist.index(song) for song in self._playlist])
        else:
            albums = set([self._playlist.index(song) for song in self._playlist if song._album == album])
        if title is None:
            titles = set([self._playlist.index(song) for song in self._playlist])
        else:
            titles = set([self._playlist.index(song) for song in self._playlist if song._title == title])
        if len(sorted(list(artists.intersection(albums, titles)))) != 0:    # Checking if list isn't empty
            return list(artists.intersection(albums, titles))[0]
        else:   # If list is empty
            return None

    def number_of_songs(self) -> int:
        """ returns number of songs in a playlist instance """
        return len(self._playlist)

    def update_usage_stats(self) -> None:
        """ updates usage stats """
        self._usage.increment_usage_stats()

    def get_usage_stats(self) -> UsageStats:
        """ returns usage stats """
        return self._usage

    def get_name(self):
        """ returns the name of a playlist instance """
        return self._name

    def change_name(self, name: str) -> None:
        """ changes the name of a playlist instance """
        if Playlist.__valid_string(name):
            self._name = name
        else:
            raise ValueError("Name empty or not type str")

    def get_description(self):
        """ returns a playlist instances description """
        return self._description

    def change_description(self, description: str) -> None:
        """ changes description of a playlist instance """
        if Playlist.__valid_string(description):
            self._description = description
        else:
            raise ValueError("Description empty or not type str")

    @classmethod
    def __valid_position(cls, posn):
        """ private method to validate that posn is an int """
        if type(posn) is not int:
            return False
        else:
            return True

    @classmethod
    def __valid_string(cls, string):
        """ private method to validate that a string is a string """
        if type(string) is not str or string == "":
            return False
        else:
            return True
