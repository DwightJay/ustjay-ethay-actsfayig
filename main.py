import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    piglatinize_url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    fact = get_fact()

    # send a request to https://hidden-journey-62459.herokuapp.com/
    # it should be a post request, and it should have form data with input_text
    # of the fact that we scraped and use the keyword argument "follow_redirects=false"
    # when making your request so that you can capture and analyse the redirect response
    # looks like:
    response = requests.post(
        piglatinize_url,
        data = {"input_text": fact},
        allow_redirects = False
    )
    #print(response.status_code)
    #print(response.headers)
    #print(dir(response))
    # status_code

    # then get the location header from the responseself.
    # looks like
    # finish here
    location_header = response.headers['Location']

    return requests.get(location_header).text

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
