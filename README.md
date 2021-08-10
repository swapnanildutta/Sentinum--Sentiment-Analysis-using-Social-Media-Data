# Social-Media-Sentiment-Analysis-API

**The Application Programming Interface (API) is written in Python Programming Language, using the Tweepy Package by Twitter, and the Flask server is used to host this entire API.**In this project, we are using the Sentiment Analysing algorithm to predict the emotional state of an individual based on the data input from the person's social media posts and interactions. To perform this analysis, we use an interactive platform like the website or the mobile application and take the user authorized account name and process the data accordingly in our server and finally display the result of analysis performed i.e. the emotional state of the individual whose account name was provided.

> Tweepy:- Tweepy is a Python library for accessing the official Twitter API - as such, you need to apply for developer access and get keys from Twitter. Tweepy’s documentation is, in our views, top-notch. Its documentation includes tutorials for everything from authentication to streaming and includes an API reference for all of its methods.

We had to apply for the Twitter Developer Account with reasons stating the reason for data collection and when they found it convincing, and then they provided us with tokens that were required to authenticate the API calls. The Twitter API is authenticated for each individual call. The input accepted (Twitter Username) is collected through a Flask route and is passed into the API to retrieve the user timeline, and since here we are using a free plan, we are allowed to retrieve the latest 20 tweets only. After retrieving the tweets the tweets are passed into the custom ML Model for processing.

The ML Model uses a saved NLTK model to predict. The NLTK has been called “a wonderful tool for teaching and working in, computational linguistics using Python” and “an amazing library to play with natural language.” The saved model (.pkl and .sav) file is then extracted in a separate function within the Flask server to return the predicted value.

Upon receiving the output, the result is jsonified and returned by our Flask Server to the respective calling platform (Mobile/Web Application).

This is just the API of our project, hosted on Heroku and hence the Procfile is made.

## Setup

- Create a Twitter Developer Account and acquire the access token and key and API key and token.
- Paste those credentials into the [_app.py_](/app.py).

### Hosting Locally

- Install the dependencies using :

  ```bash
  pip install -r requirements.txt
  ```

- Run the [_app.py_](/app.py) file :

  ```bash
  python3 app.py
  ```

### Hosting Remotely

- Fork the entire repository and make the necessary changes.
- Link the repository to the Heroku pipeline.

### Output ( Same for Locally and Remotely Hosted )

#### Viewed In Browser

<p align="center">
<img src='Static\1.jpg' alt="Browser View">
</p>

#### Viewed In API Testing Platform

<p align="center">
<img src='Static\2.jpg' alt="API Tester View">
</p>
