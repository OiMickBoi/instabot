from data import login as cred
from dl import Media as dl

photo = "https://www.instagram.com/p/CiMYkEXuNAJ/"
video = "https://www.instagram.com/p/CsJbKHno1cR/"
album = "https://www.instagram.com/p/CsghdUhL573/"

dl.get_photo(photo, "tmp")
dl.get_video(video, "tmp")
dl.get_album(album, "tmp/itzy_album")
