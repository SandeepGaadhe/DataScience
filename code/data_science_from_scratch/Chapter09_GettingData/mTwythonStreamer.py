from twython import TwythonStreamer
# appending data to a global variable is pretty poor form
# but it makes the example much simpler
tweets = []

CONSUMER_KEY = 'DZT6QkNFddfor97JobykkIGRR'
CONSUMER_SECRET = 'vxEDfbeh1h7b96VmkQxMh2FdLi7lPFCKkaGFX9C6EMBXEm0PV8'
ACCESS_TOKEN = '1207750839097536514-c6KwYdTrkJJQ4on1trXK1JW9HEvKHC'
ACCESS_TOKEN_SECRET = '6VpggggqqsrBQSOxMIM3yU7qb0eCHPRtsTOzf1nMHmH5z'

class MyStreamer(TwythonStreamer):
    """our own subclass of TwythonStreamer that specifies how to interact with the stream"""
    def on_success(self, data):
        """what do we do when twitter sends us data? here data will be a Python dict representing a tweet"""
        # only want to collect English-language tweets
        if data['lang'] == 'en':
            tweets.append(data)
            print (f"\nreceived tweet #, {len(tweets)}")
            print (f"received tweet, {data}")
        
            # stop when we've collected enough
            if len(tweets) >= 10:
                self.disconnect()
            
    def on_error(self, status_code, data):
        print (f"Error : {status_code}, {data}")
        self.disconnect()
        

# ------------------------------
# Using MyStreamer
# ------------------------------

stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        
# starts consuming public statuses that contain the keyword 'data'
stream.statuses.filter(track='data')        
        
        
        