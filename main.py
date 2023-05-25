from instagrapi import Client
from data import login as cred

cl = Client()
cl.login(cred.getUserName(), cred.getPassword())

media = cl.photo_upload(
    "test.jpg",
    "Check out @ecommerce.academy for more content like this!",
)