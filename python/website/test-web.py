#!/usr/bin/python3


from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_memes():
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests("GET",url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large,subreddit

@app.route("/")
def index():
    meme_pic,subreddit = get_memes()
    return render_template("meme_index.html",meme_pic=meme_pic,subreddit=subreddit)