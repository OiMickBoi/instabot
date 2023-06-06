import os
from instagrapi import Client
from data import login as cred

cl = Client()
cl.login(cred.USERNAME, cred.PASSWORD)

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
    def get_video(url):
        """
        Downloads a instagram video from a given url.
        :media_pk: the media_pk 
        :returns the path the file is saved at.
        """
        print("Downloading video...")
        print("Downloaded video!")
        return cl.video_download(convert_url(url), folder='tmp')

    def get_video(url, path):
        """
        Downloads a instagram video from a given url.
        :media_pk: the media_pk
        :path: path to download file
        :returns the path the file is saved at.
        """
        check_path(path)

        print("Downloading video...")
        print("Downloaded video!")
        return cl.video_download(convert_url(url), folder='tmp')

    def get_photo(url):
        """
        Downloads a instagram photo from a given url
        :media_pk: the media_pk
        :returns: the path the file is saved at.
        """
        print("Downloading photo...")
        print("Downloaded photo!")
        return cl.photo_download(convert_url(url), folder='tmp')

    def get_photo(url, path):
        """
        Downloads a instagram photo from a given url
        :media_pk: the media_pk
        :path: path to download file
        :returns: the path the file is saved at.
        """
        check_path(path)

        print("Downloading photo...")
        print("Downloaded photo!")
        return cl.photo_download(convert_url(url), folder='tmp')

    def get_album(url):
        """
        Downloads a instagram album from a given url
        :media_pk: the media_pk
        :returns: the path the file is saved at.
        """
        print("Downloading album...")
        print("Downloaded album!")
        return cl.album_download(convert_url(url), folder=album_path)

    def get_album(url, path):
        """
        Downloads a instagram album from a given url
        :media_pk: the media_pk
        :path: path to download file
        :returns: the path the file is saved at.
        """
        check_path(path)
        
        print("Downloading album...")
        print("Downloaded album!")
        return cl.album_download(convert_url(url), folder=path)
