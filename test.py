from instagrapi import Client

cl = Client()
USERNAME=""
PASSWORD=""
# cl.login (USERNAME, PASSWORD)
# cl.dump_settings("session.json")

cl.load_settings("session.json")
cl.login (USERNAME, PASSWORD) # this doesn't actually login using username/password but uses the session
cl.get_timeline_feed() # check session

# photo = "https://www.instagram.com/p/CiMYkEXuNAJ/"
# video = "https://www.instagram.com/p/CsJbKHno1cR/"
album = "https://www.instagram.com/p/CsghdUhL573/"
pk = cl.media_pk_from_url(album)
cl.album_download(pk, folder='tmp/itzy_album')


# dl.get_album(album, "tmp/itzy_album")

# dl.get_photo(photo, "tmp")
# dl.get_video(video, "tmp")
# dl.get_album(album, "tmp/itzy_album")
