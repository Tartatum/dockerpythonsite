from flask import Flask, request
import time
import redis
from statistics import mean
app = Flask(__name__)

cache = redis.Redis(host='redis', port=6379)

def get_hits_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    hits = get_hits_count()
    vals = request.args.get('vals',type=str)
    if type(vals) == str:
        liste = vals.split(",")
        try:
            liste = map(float, liste)
            liste_mean = mean(liste)
            return f"mean of ({vals}) = {liste_mean}"
        except:
            return "The values given is not only composed of int"
       
    else: 
        return "200,Hello to my App page, please give a vals (like : ?vals=5000,2000,3000) in the web link"


if (__name__== '__main__'):
    app.run(host = '0.0.0.0',port = 5000)