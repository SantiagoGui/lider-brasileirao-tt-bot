import tweepy
from leaderScreatch import takeLeader

api = tweepy.Client(
            consumer_key= '6sFIxQtbmE6kbZln0EK5VkYaK',
            consumer_secret= 'faaxc2MYEtssZu9jzo2w1Y9WMHXw4SytvG2OwhzHA9hswk4KvG',
            access_token= '1682130051578429446-ZudJ1DTicLRlQfdLm6o6b3lFa4sSZP',
            access_token_secret= 'pyhm724FHwTybKFpM7ARHeKMaFLvbVIf16LtpmXumT1i7'
)



tweet = api.create_tweet(text= takeLeader())


