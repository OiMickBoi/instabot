import random

class upload:
    def random_text():
        """
        Generates a random emoji and concatenates it with instagram tags
        :return: emoji string
        """
        list = ("🐶🐱🐭🐹🐰🦊🐻🐼🐻‍❄🐨🐯🦁🐮🐷🐽🐸🐵🙈🙉🙊🐒🐔🐧"
        + "🐦🐦🐤🐣🐥🦆🦅🦉🦇🐺🐗🐴🦄🐝🐛🦋🐌🐞🐜🦗🕷🕸"
        + "🦂🐢🐍🦎🦖🦕🐙🦑🦐🦀🐡🐠🐟🐬🐳🐋🦈🐊🐅🐆🦓🦍"
        + "🐘🦏🐪🐫🦒🐃🐂🐄🐎🐖🐏🐑🐐🦌🐕🐩🐕🐈🐈🐓🦃🕊🐇🐁"
        + "🐀🐿🦔🐾🐉🐲🌵🎄🌲🌳🌴🌱🌿☘🍀🎍🎋🍃🍂🍁🍄🐚🌾💐🌷"
        + "🌹🥀🌺🌸🌼🌻🌞🌝🌛🌜🌚🌕🌖🌗🌘🌑🌒🌓🌔🌙🌎🌍🌏💫⭐🌟"
        + "✨⚡☄💥🔥🌪🌈☀🌤⛅🌥☁🌦🌧⛈🌩🌨❄☃⛄🌬💨💧💦☔☂🌊🌫")

        tags = ("#explorepage #explore #exploremore #instagram "
        + "#instamood #instamemes #instagood #instalike #instalove "
        + "#fbmemes #fbmemesformentallyillbitches #badlyeditedfacebookmemes "
        + "#facebookmemes #viral #pinterest #pinterestaesthetic #pinterestmemes "
        + "#memes #moodygrams #memesdaily #relatable #relatablequotes "
        + "#relatablepost #relatablememes #relatablememes #twitter #twitterthreads "
        + "#delusional #humor")

        string = "".join(random.sample(list, 1)) + "\n\n.\n.\n" + tags
        return string

    def upload_photo(client, post_path):
        """
        Uploads a photo from a given filepath.
        :client: client object with login info
        :post_name: file path to the post
        :return: media
        """
        media = cl.photo_upload(
            post_path,
            self.random_text())
        return media

