# Social-Media-Sentiment-Analysis-API

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![HitCount](http://hits.dwyl.com/swapnanildutta/Social-Media-Sentiment-Analysis-API.svg)](http://hits.dwyl.com/swapnanildutta/Social-Media-Sentiment-Analysis-API)

In this project, we are using the Sentiment Analysing algorithm to predict the emotional state of an individual based  on the data input from the person's social media posts and interactions. To perform this analysis, we use an interactive platform like the website or the mobile application and take the user authorized account name and process the data accordingly in our server and finally display the result of analysis performed i.e. the emotional state of the individual whose account name was provided.

This is just the API of our project, hosted on Heroku and hence the Procfile is made.

## Setup

- Create a Twitter Developer Account and acquire the access token and key and API key and token.
- Paste those credentials into the [*app.py*](/app.py).

### Hosting Locally

- Install the dependencies using :

    ```bash
    pip install -r requirements.txt
    ```

- Run the [*app.py*](/app.py) file :

    ```bash
    python app.py
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
