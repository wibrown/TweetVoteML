import twitter
import keys
import math
from sklearn.externals import joblib


api = twitter.Api(consumer_key=keys.CONSUMER_KEY2,
                  consumer_secret=keys.CONSUMER_SECRET2,
                  access_token_key=keys.ACCESS_TOKEN2,
                  access_token_secret=keys.ACCESS_SECRET2,
                  sleep_on_rate_limit=True)


def process_username(username):
    try:
        # Load model from hard drive
        text_clf = joblib.load('model/tweets_classifier.joblib.pk1')

        # Get tweets
        tweets = api.GetUserTimeline(screen_name=username, count=200)

        texts = []
        for tweet in tweets:
            texts.append(tweet.text)

        # 0 for Hillary, 1 for Trump
        predicted = text_clf.predict(texts)

        trump_count = 0
        hillary_count = 0

        for i in range(0, len(texts)):
            if predicted[i] == 0:
                hillary_count += 1
            else:
                trump_count += 1

        # 0 for Hillary, 1 for Trump
        orientation = 0

        if trump_count >= hillary_count:
            orientation = 1

        ratio = max(trump_count, hillary_count) * 1.0 / len(texts)

        # Calculation to get number of tweets for each candidate
        larger_count = math.floor(ratio * 10)
        smaller_count = 10 - larger_count

        trump_tweets = []
        hill_tweets = []

        if orientation == 1:
            i = 0
            while i < len(texts) and len(trump_tweets) < larger_count:
                if predicted[i] == 1:
                    trump_tweets.append(texts[i])
                i += 1

            j = 0
            while j < len(texts) and len(hill_tweets) < smaller_count:
                if predicted[j] == 0:
                    hill_tweets.append(texts[j])
                j += 1
        else:
            i = 0
            while i < len(texts) and len(trump_tweets) < smaller_count:
                if predicted[i] == 1:
                    trump_tweets.append(texts[i])
                i += 1

            j = 0
            while j < len(texts) and len(hill_tweets) < larger_count:
                if predicted[j] == 0:
                    hill_tweets.append(texts[j])
                j += 1

        # print "REPORT"
        # print "NAME: " + username
        # print "ORIENTATION: " + str(orientation)
        # print "RATIO: " + str(ratio)
        # print "TRUMP COUNT: " + str(trump_count)
        # print "HILLARY COUNT: " + str(hillary_count)
        # print "TRUMP TWEET SIZE: " + str(len(trump_tweets)) + " " + str(trump_tweets)
        # print "HILLARY TWEET SIZE: " + str(len(hill_tweets)) + " " + str(hill_tweets)
        user_dict = {'name': username,
                     'orientation': orientation,
                     'ratio': ratio,
                     'trump_tweets': trump_tweets,
                     'hillary_tweets': hill_tweets,
                     'error': ""}
        return user_dict

    except twitter.error.TwitterError:
        error = "Sorry, this user is private."
        return {'error': error}
