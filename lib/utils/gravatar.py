__author__ = 'yu'

import md5
import urllib



DEFAULT_IMAGE_DICT = {
    0: "404",
    # do not load any image if none is associated with the email hash,
    # instead return an HTTP 404 (File Not Found) response
    1: "mm",  # (mystery-man) a simple, cartoon-style silhouetted outline of a person (does not vary by email hash)
    2: "identicon",  # a generated 'monster' with different colors, faces, etc
    3: "wavatar",  # generated faces with differing features and backgrounds
    4: "retro",  # awesome generated, 8-bit arcade-style pixelated faces
    5: "blank"  # a transparent PNG image (border added to HTML below for demonstration purposes)
}

RATING_DICT = {
    0: "g",  # suitable for display on all websites with any audience type.
    1: "pg",  # may contain rude gestures, provocatively dressed individuals, the lesser swear words, or mild violence.
    2: "r",  # may contain such things as harsh profanity, intense violence, nudity, or hard drug use.
    3: "x",  # may contain hardcore sexual imagery or extremely disturbing violence.
}

GRAVATAR_PREFIX = "//www.gravatar.com/avatar/"

# size : xxx px , because the avatar are squared , you just need set one value
# ext : must in : jpg, jpeg, gif, png
def get_gavatar_url(email, size=80, default_image=3, rating=0, extension=".png",default_url = None,force_default=False):
    if default_image not in DEFAULT_IMAGE_DICT and default_url is None:
        default_image = 3
    if rating not in RATING_DICT:
        rating = 0
    email = str(email).lower().strip()
    if default_url :
        if force_default:
            return GRAVATAR_PREFIX + md5.md5(email).hexdigest() + extension + \
                   "?s=" + str(size) + \
                   "&r=" + RATING_DICT[rating] + \
                   "&" + urllib.urlencode({'d':default_url}) + \
                   "&f=y"
        else :
            return GRAVATAR_PREFIX + md5.md5(email).hexdigest() + extension + \
                   "?s=" + str(size) + \
                   "&r=" + RATING_DICT[rating] + \
                   "&" + urllib.urlencode({'d':default_url})
    else :
        if force_default:
            return GRAVATAR_PREFIX + md5.md5(email).hexdigest() + extension + \
                   "?s=" + str(size) + \
                   "&r=" + RATING_DICT[rating] + \
                   "&d=" + DEFAULT_IMAGE_DICT[default_image] + \
                   "&f=y"
        else :
            return GRAVATAR_PREFIX + md5.md5(email).hexdigest() + extension + \
                   "?s=" + str(size) + \
                   "&r=" + RATING_DICT[rating] + \
                   "&d=" + DEFAULT_IMAGE_DICT[default_image]



