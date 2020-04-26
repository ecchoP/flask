from flask import Flask
import sys
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    API_KEY = 'RGAPI-aede0911-42b5-4258-a176-e3664c44030d'
    URL = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/CallumKoi?api_key=%s' % (API_KEY)
    riotapilevel = 'summonerLevel'
    r = requests.get(URL)
    level = r.json()[riotapilevel]
    return 'Callum\'s Summoner Level is currently:<br>%s<br>Number of cute boys Callum has cuddled with: 0 <br><a href="https://youtu.be/fQfLfuGsUBg">Keyboard</a> and im sorry callum<br> Python Version: %s <br> this website is a joke, and any and all resemblences between persons on this website and persons either living or dead, are purely coincidental' % (level, '.'.join(['%d'%k for k in sys.version_info[:3]]))
    #return 'hello'



