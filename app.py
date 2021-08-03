from flask import Flask, render_template, url_for, send_from_directory, flash
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from forms import NameForm
import requests
import json
import re
import plotly.graph_objects as go

key=re.compile(r'''(
    ^(?=.*[A-Z].*[A-Z])
    (?=.*[!@#$%&*])
    (?=.*[0-9].*[0-9])
    (?=.*[a-z].*[a-z].*[a-z])
    .{10,}
    $
)''',re.VERBOSE)

app=Flask(__name__)
app.config['SECRET_KEY']=str(key)
Bootstrap(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/how-to-use',methods=['GET'])
def how_to_use():
    return render_template('howtouse.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/Privacy-Policy', methods=['GET'])
def privacy_policy():
    return render_template('Privacy Policy.html')

@app.route('/twitter', methods=['GET','POST'])
def twitter():
    error = False
    response = None
    url= 'API_URL'
    form = NameForm()
    if form.validate_on_submit():
        user= username=form.name.data
        response = requests.get((url+str(user)))
        predictions=None
        if response.status_code == 200:
            predictions=response.json()['result']
            labels=['Happiness', 'Sadness']
            values=[predictions*100, (1-predictions)*100]
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.7)])
            fig = fig.to_html()
            return render_template('twitterresult.html',user=user, predictions=str(int(predictions*100)), pred=predictions*100, fig=fig )
        else:
            error = True
            flash("Looks like you've entered a wrong username!")
    return render_template('twitter.html',form=form, error=error)

@app.route('/twitter-result', methods=['GET'])
def twitter_result():
    return render_template('twitterresult.html',)

if __name__ == '__main__':
    app.run()