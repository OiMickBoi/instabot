from instagrapi import Client
from data import login as cred
from dl import Media as stuff

cl = Client()
cl.login(cred.getUserName(), cred.getPassword())

# stuff.get_album("https://www.instagram.com/p/CsghdUhL573/", "tmp/itzy_album")

media = cl.photo_upload(
    "tmp/itzy_album/itzy.all.in.us_3107630885783749734.jpg",
    "CHOI JISU! And Yej",
)
