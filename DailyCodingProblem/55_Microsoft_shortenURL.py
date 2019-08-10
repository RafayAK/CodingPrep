"""
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url.
If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
"""


import hashlib

class tinyURL:
    def __init__(self):
        self.m = hashlib.sha3_256
        self.prefix = "rafay.ak/"
        self.key_to_URL = dict()

    def shorten(self, url):
        key = self.m(url.encode()).hexdigest()[:6]
        self.key_to_URL[key] = url
        return self.prefix+key

    def get_url(self, shortened_url):
        key = shortened_url.replace(self.prefix, "")
        return self.key_to_URL[key]


if __name__ == '__main__':

    url = "https://arxiv.org/pdf/1606.05340v2.pdf"
    print("Original URL: " + url)
    tinyURL = tinyURL()
    short_1 = tinyURL.shorten(url)
    print("Shortened URL_1: " + short_1, end=" ---- ")
    print("Original URL: " + tinyURL.get_url(short_1))
    short_2 = tinyURL.shorten(url)
    print("Shortened URL: " + short_2, end=" ---- ")
    print("Original URL: " + tinyURL.get_url(short_2))


