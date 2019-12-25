import re
import tweepy as tw
from xlwt import Workbook

# Twitter API credentials
consumer_key = "aPupBiCom9T0hWtlik3QxlgCc"
consumer_secret = "5X8NgCSptafqz1AM14Pop13vHbSzfu9JRsAaEPpNPx2WbWiTnG"
access_token = "1152102556018991106-7KNe0RhlbXuJriVSCdZyvGoYiIYqLp"
access_token_secret = "iiljRVsatQ06Rf1RvqJ4AeoBwDrtDePx8Bd6yGBHzIL64"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Workbook is created
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

search_words = "climate -filter:retweets"
date_since = "2019-12-20"

def remove_xuong_dong(txt):
    return " ".join(re.sub("\n", "", txt).split())

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since = date_since).items(5000)

i = 0
for tweet in tweets:
    tweet_mot_dong = remove_xuong_dong(tweet.text)
    # sheet1.write(i, 1, tweet.user.screen_name)
    sheet1.write(i, 0, tweet_mot_dong)
    # sheet1.write(i, 1, tweet.created_at)
    i += 1
    print(i)

wb.save('excel/climate_v5.csv')