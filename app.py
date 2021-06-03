from flask import Flask, render_template, request , redirect , url_for
from apscheduler.schedulers.background import BackgroundScheduler as scheduler

import requests
import json

app=Flask(__name__)



@app.route('/')
def news():
    with open('news_database.json') as json_file:
        news = json.load(json_file)

    for i in range(len(news)):
        news[i]["ID"]="news"+ str(news[i]["index"])

    return render_template('news.html', news=news)

if __name__ == '__main__':
    app.run( debug = True)
