import hashlib

"""
Problem 535: Encode and Decode TinyURL

TinyURL is a URL shortening service where you enter a URL such as 
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as
http://tinyurl.com/4e9iAk. Design the encode and decode methods for the TinyURL
service. There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL
can be decoded to the original URL.

Note: in industry the storage solution of translating between long and short
links should be a database of some kind. For my approach for this problem I
instead used dictionaries. If this script was to crash all of the link 
translations would be lost.

Approach: Take the long url, encode it to UTF-8 byte string to then encode to 
a hash with sha256, grab the last few characters of that hash and that would
represent the tag we will use to shorten that link. Prepend the base URL to 
that and you now have a shortened link you can decode. Decoding is a 
dictionary lookup.

(assuming links are bounded by 2048 characters or less)
n := number of links our codec translates
Runtime Complexity: O(1)
Space Complexity: O(n)
Runtime: 36ms, faster than 52.1%
Space: 16.1 MB, less than 5.64%
"""

class Codec:
    def __init__(self):
        self.orig_link_dict = {}
        self.shortened_link_dict = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short_hash = hashlib.sha256()
        short_hash.update(longUrl.encode())
        short_tag = short_hash.hexdigest()[-7:]
        # print(short_tag)
        short_link = "http://tinyurl.com/" + short_tag
        self.orig_link_dict[longUrl] = short_link
        self.shortened_link_dict[short_link] = longUrl
        return short_link

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.shortened_link_dict[shortUrl]

if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    codec = Codec()
    url = "https://leetcode.com/problems/encode-and-decode-tinyurl/"
    print(codec.decode(codec.encode(url)))