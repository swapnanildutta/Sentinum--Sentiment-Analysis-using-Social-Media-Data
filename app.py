#Import the model
from Model import model

#Import the Packages
import tweepy
import json
from flask import Flask

#Initialize API credentials
api_key='YOUR API KEY'
api_secret='YOUR API SECRET'

access_token='YOUR ACCESS TOKEN'
access_secret='YOUR ACCESS SECRET'

#Authenticate the API
auth= tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api=tweepy.API(auth)

app=Flask(__name__)
#Routes
@app.route('/twitter/<string:name>')
def get_Twitter(name):
    _Tdata=dict()
    try:
        #Extract twitter data
        public_tweets= api.user_timeline(screen_name=name)
        i=0
        #Form a dictionary of tweet
        for tweet in public_tweets:
            _Tdata.update({
                i: tweet.text
            })
            i+=1
        #Predict the ratio
        prediction = model.model_pred(_Tdata)
        #Return the prediction
        return {'result': prediction},200
    except:
        #Return the error message
        return {'result': 'error'},204

if __name__ == "__main__":
    app.run(port=5000)