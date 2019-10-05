"""
Encode and Decode TinyURL

TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Other types of URLs:
  https://airport.example.com/
  ftp://174.123.452.34/directory/file

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm 
should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded 
to the original URL.

import re
import random
import string
"""

# MY REGEX SOLUTION
class Codec:
    
    def __init__(self):
        self.global_url = {} 
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        domain = re.findall(r"\/{2}[a-zA-Z0-9.]+",longUrl)
        re_domain = re.sub(r"\/{2}[a-zA-Z0-9.]+","vinytiny.com", longUrl)
        self.global_url["domain"] = domain
        category = re.findall(r"\/{1}\S*",re_domain)
        rand_value = "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(6)])
        re_rand_value = re.sub(r"\/{1}\S*","/{}".format(str(rand_value)), re_domain)
        self.global_url["category"] = category
        protocol = re.findall(r"[a-zA-Z]*:{1}",re_rand_value)
        short_url = re.sub(r"[a-zA-Z]*:{1}","http://", re_rand_value)
        self.global_url["protocol"] = protocol
        
        return(short_url)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        temp = ""
        temp = self.global_url["domain"][0]
        re_domain = re.sub(r"\/{2}[a-zA-Z0-9.]+",temp, shortUrl)
        rand_value = "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(6)])
        temp = self.global_url["category"][0]
        re_rand_value = re.sub(r"\/{1}[a-zA-Z0-9]{6}$",temp, re_domain)
        temp = self.global_url["protocol"][0]
        long_url = re.sub(r"[a-zA-Z]*:{1}",temp, re_rand_value)

        return long_url        

# SOLUTION FROM StefanPochmann. I made a few changes only.
# class Codec:

#     def __init__(self):
#         self.long2short = {}
#         self.short2long = {}

#     def encode(self, longUrl):
#         while longUrl not in self.long2short:
#             code = ''.join(random.choice(string.ascii_letters + string.digits) for n in xrange(6))
#             if code not in self.short2long:
#                 self.short2long[code] = longUrl
#                 self.long2short[longUrl] = code
#         return 'http://vinyurl.com/' + self.long2short[longUrl]
#     def decode(self, shortUrl):
#         return self.short2long[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:

#codec = Codec()
#codec.decode(codec.encode(url))
