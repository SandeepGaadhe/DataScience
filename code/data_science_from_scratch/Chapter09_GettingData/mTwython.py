"""
Consumer API keys
DZT6QkNFddfor97JobykkIGRR (API key)

vxEDfbeh1h7b96VmkQxMh2FdLi7lPFCKkaGFX9C6EMBXEm0PV8 (API secret key)
"""

from twython import Twython

CONSUMER_KEY = 'DZT6QkNFddfor97JobykkIGRR'
CONSUMER_SECRET = 'vxEDfbeh1h7b96VmkQxMh2FdLi7lPFCKkaGFX9C6EMBXEm0PV8'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)
# search for tweets containing the phrase "data science"
for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"].encode('utf-8')
    text = status["text"].encode('utf-8')
    print (user, ":", text)
    print('\n')


