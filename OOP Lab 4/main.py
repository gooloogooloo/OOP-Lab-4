from audio_file import AudioFile
from song import Song
from podcast import Podcast
from usage_stats import UsageStats
import datetime

def test1():
    # First Song
    song1 = Song("Sugar", "Kate Loverson", "3:01", "/desktop/made_up_folder/music", "test.wav", "Sweets",
                 ["Jazz", "Pop"])
    print(song1.get_description())
    print(song1.meta_data())

    print()

    # Second Song
    song2 = Song("TNT", "AC/DC", "3:43", "/desktop/made_up_folder/music", "tnt.wav", "High Voltage",
                 ["Rock"])
    print(song2.get_description())
    print(song2.meta_data())

    print()

    # Third song
    song3 = Song("Real Slim Shady", "Eminem", "4:03", "/desktop/made_up_folder/music", "slim_shady.wav",
                 "Marshall Mathers", ["Rap", "Hip-Hop"])
    print(song3.get_description())
    print(song3.meta_data())

    print()

    # Fourth song
    song4 = Song("Go Popek", "Popek", "3:55", "/desktop/made_up_folder/music", "go_popek.wav", "Dr Jekyll and Mr Hyde",
                 ["Rap", "Hip-Hop"])
    print(song4.get_description())
    print(song4.meta_data())


def test2():
    # First podcast
    podcast1 = Podcast("Do Aliens Exist?", "Joe Rogan", "1:53:02", "/desktop/made_up_folder/podcast",
                       "do_aliens_exist.wav", "JRE", datetime.date(2019, 6, 15), datetime.time(0))

    print()

    # Second podcast
    podcast2 = Podcast("Eddie Bravo argues over flat earth", "Joe Rogan", "25:08", "/desktop/made_up_folder/podcast",
                       "eddie_bravo_earth.wav", "JRE", datetime.date(2019, 9, 7), datetime.time(0))


if __name__ == '__main__':
    # Testing song class
    test1()
    print()
    # Testing podcast class
    test2()
