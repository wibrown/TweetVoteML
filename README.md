TweetVoteML - Predicting who you'll vote for this election using Machine Learning and your Twitter data.

Application is live at http://tweetvote.ml
Backend code is viewable at https://github.com/robzajac/TweetVoteML-Backend

How it works:
We found thousands of users who had tweeted either the hashtag #ImWithHer or #MakeAmericaGreatAgain, designated them as Hillary or Trump supporters respectively, and stored collections of their tweets into separate databases. We used the two databases to generate a prediction model using scikit-learn's logistic regression algorithm. When a user enters their Twitter username into the application, 200 of their recent tweets are vectorized and compared individually against the model. Each tweet is labeled as pro-Trump or pro-Hillary based on occurrence of unique words in either database, and both sets of tweets are counted. The larger of the two counts is then output as a ratio of overall tweets, alongside a collection of user tweets that correspond to their political preferences.
