import apikey
import tweepy
import time
import requests
import datetime

while True: 
    try:
        headers={
            'X-CMC_PRO_API_KEY' : apikey.key,
            'Accept':'application/json'
        }
        params={
            'start': '1',
            'limit': '12',
            'convert' : 'USD'
        }
        obj={}
        obj1={}
        url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        json=requests.get(url, params=params, headers=headers).json()
        coins=json['data']
        for i in coins:
            obj[i['symbol']] = i['quote']['USD']['price']
        for j in coins:
            obj1[j['symbol']]=j['quote']['USD']['percent_change_1h']
        BTC="#BTC:$"+str("{:.2f} |  ".format(obj["BTC"]))
        ETH="#ETH:$"+str("{:.2f} |  ".format(obj["ETH"]))
        BNB="#BNB:$"+str("{:.2f} |  ".format(obj["BNB"]))
        USDT="#USDT:$"+str("{:.2f} |  ".format(obj["USDT"]))
        ADA="#ADA:$"+str("{:.2f} |  ".format(obj["ADA"]))
        USDC="#USDC:$"+str("{:.2f} |  ".format(obj["USDC"]))
        XRP="#XRP:$"+str("{:.2f} |  ".format(obj["XRP"]))
        LUNA="#LUNA:$"+str("{:.2f} | ".format(obj["LUNA"]))
        DOT="#DOT:$"+str("{:.2f} | ".format(obj["DOT"]))
        AVAX="#AVAX:$"+str("{:.2f} | ".format(obj["AVAX"]))
        DOGE="#DOGE:$"+str("{:.2f} | ".format(obj["DOGE"]))

        BTC1=str("{:.2f}".format(obj1["BTC"])+"%")
        ETH1=str("{:.2f}".format(obj1["ETH"])+"%")
        BNB1=str("{:.2f}".format(obj1["BNB"])+"%")
        USDT1=str("{:.2f}".format(obj1["USDT"])+"%")
        ADA1=str("{:.2f}".format(obj1["ADA"])+"%")
        USDC1=str("{:.2f}".format(obj1["USDC"])+"%")
        XRP1=str("{:.2f}".format(obj1["XRP"])+"%")
        LUNA1=str("{:.2f}".format(obj1["LUNA"])+"%")
        DOT1=str("{:.2f}".format(obj1["DOT"])+"%")
        AVAX1=str("{:.2f}".format(obj1["AVAX"])+"%")
        DOGE1=str("{:.2f}".format(obj1["DOGE"])+"%")

        MESSAGE=BTC+BTC1+'\n'+ETH+ETH1+'\n'+BNB+BNB1+'\n'+USDT+USDT1+'\n'+ADA+ADA1+'\n'+USDC+USDC1+'\n'+XRP+XRP1+'\n'+LUNA+LUNA1+'\n'+DOT+DOT1+'\n'+AVAX+AVAX1+'\n'+DOGE+DOGE1+'\n'
        MESSAGE2=BTC+BTC1+'\n'+ETH+ETH1+'\n'+BNB+BNB1+'\n'+USDT+USDT1+'\n'+ADA+ADA1+'\n'+USDC+USDC1+'\n'
        # print(MESSAGE)
        if len(MESSAGE)>280:
            print("Message length is too long")
            MESSAGE=MESSAGE[:279]

        api_key=apikey.API_KEY
        api_key_secret=apikey.API_KEY_SECRET
        access_token=apikey.ACCESS_TOKEN
        access_token_secret=apikey.ACCESS_TOKEN_SECRET

        auth= tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)

        api=tweepy.API(auth)

        api.update_status(MESSAGE  +"\n"+ str(datetime.datetime.now()))
        print("Tweet Sent...")

        FILE_NAME = 'last_seen_id.txt'

        def retrieve_last_seen_id(file_name):
            f_read = open(file_name, 'r')
            last_seen_id = int(f_read.read().strip())
            f_read.close()
            return last_seen_id

        def store_last_seen_id(last_seen_id, file_name):
            f_write = open(file_name, 'w')
            f_write.write(str(last_seen_id))
            f_write.close()
            return


        def reply_to_tweets():
            print('retrieving and replying to tweets...', flush=True)
            # DEV NOTE: use 1060651988453654528 for testing.
            last_seen_id = retrieve_last_seen_id(FILE_NAME)
            # NOTE: We need to use tweet_mode='extended' below to show
            # all full tweets (with full_text). Without it, long tweets
            # would be cut off.
            mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
            for mention in reversed(mentions):
                print(str(mention.id) + ' - ' + mention.full_text, flush=True)
                last_seen_id = mention.id
                store_last_seen_id(last_seen_id, FILE_NAME)
                if '#btc' in mention.full_text.lower():    
                    api.update_status('@'+mention.user.screen_name+"\n"+MESSAGE2 +"\n"+ str(datetime.datetime.now()), mention.id)
        reply_to_tweets()
        time.sleep(10)
    except:
        print("Something went wrong...")
        time.sleep(10)