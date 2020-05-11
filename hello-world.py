from flask import Flask
import sys
import requests
app = Flask(__name__)

@app.route('/new_tournament')
def callum_website():
    return '<a href="https://youtu.be/fQfLfuGsUBg">CALLUM</a> WEBSITE <br> CALLUM WEBSITE'
#def new_tournament():
#    API_KEY = 'RGAPI-7f6672d3-470f-4b5d-a312-24aace5bbd18'
#    URL = 'https://americas.api.riotgames.com/lol/tournament-stub/v4/providers?api_key=RGAPI-7f6672d3-470f-4b5d-a312-24aace5bbd18'
#    #URL = 'https://americas.api.riotgames.com/lol/tournament-stub/v4/providers?api_key=%s' % (API_KEY)
#    r = requests.get(URL, data={'region': 'NA', 'url': 'http://127.0.0.1:80'})
#    print(r)
#    return repr(r)


