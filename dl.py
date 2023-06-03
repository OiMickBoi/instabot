import os
from instagrapi import Client
from data import login as cred

cl = Client()
cl.login(cred.getUserName(), cred.getPassword())

# photo_url = "https://www.instagram.com/p/CsodehWrLgm/"
# video_url = "https://www.instagram.com/p/Cs9MIW2gcsx/"
# #album_url = "https://www.instagram.com/p/Csq3CN1S74a/"
# album_url = "https://www.instagram.com/p/CsghdUhL573/"

# photo_pk = cl.media_pk_from_url(photo_url)
# video_pk = cl.media_pk_from_url(video_url)
# album_pk = cl.media_pk_from_url(album_url)
def check_path(path):
    """
    Checks to make sure the file path exists, and
    if it does not, it creates it.
    :path: the path
    """
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print("Created the " + path + " directory!")

def convert_url(url):
    """
    Converts a url string to a media_pk
    :url: media url to download
    :return: media_pk
    """
    return cl.media_pk_from_url(url)

class Media:
    def get_video(media_pk, path):
        """
        Downloads a instagram video from a given url.
        :media_pk: the media_pk 
        :returns the path the file is saved at.
        """
        print("Downloading video...")
        print("Downloaded video!")
        return cl.video_download(media_pk, folder='tmp')

    def get_video(media_pk, ):
        """
        Downloads a instagram video from a given url.
        :media_pk: the media_pk 
        :returns the path the file is saved at.
        """
        print("Downloading video...")
        print("Downloaded video!")
        return cl.video_download(media_pk, folder='tmp')


    def get_photo(media_pk):
        """
        Downloads a instagram photo from a given url
        :media_pk: the media_pk
        :returns: the path the file is saved at.
        """
        print("Downloading photo...")
        print("Downloaded photo!")
        return cl.photo_download(media_pk, folder='tmp')

    def get_album(media_pk):
        """
        Downloads a instagram album from a given url
        :media_pk: the media_pk
        :returns: the path the file is saved at.
        """
        #Download album
        print("Downloading album...")
        print("Downloaded album!")
        return cl.album_download(media_pk, folder=album_path)

    def get_album(url, path):
        """
        Downloads a instagram album from a given url
        :media_pk: the media_pk
        :returns: the path the file is saved at.
        """
        # Make sure path exist
        check_path(path)
        
        #Download album
        print("Downloading album...")
        print("Downloaded album!")
        return cl.album_download(convert_url(url), folder=path)

    

# print(get_photo(photo_pk))
# print(get_video(video_pk))
# print(get_album(album_pk))

# get_album("https://www.instagram.com/p/CsghdUhL573/", "tmp/itzy_album")
