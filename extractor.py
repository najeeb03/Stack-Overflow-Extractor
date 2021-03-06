import requests
from html import unescape
from datetime import datetime, timedelta
from flask import Flask, render_template


def get_data(url, payload):
    r = requests.get(url, params=payload)

    data = {}
    if r.ok:
        data = r.json()
        # Convert unix time to readable datetime format
        for item in data['items']:
            item['title'] = unescape(item['title'])
            item['creation_date'] = datetime.fromtimestamp(item['creation_date'])
    return data


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    # get time for one week form now
    to_date = datetime.today()
    from_date = to_date - timedelta(days=7)
    # convert datetime to unix time
    to_date = int(to_date.timestamp())
    from_date = int(from_date.timestamp())

    payload = {'pagesize': 10, 'order': 'desc', 'tagged': 'android', 'site': 'stackoverflow'}

    url_newest = 'http://api.stackexchange.com/2.2/questions?sort=creation&fromdate=' + str(
        from_date) + '&todate=' + str(to_date)
    url_votes = 'http://api.stackexchange.com/2.2/questions?sort=votes&fromdate=' + str(from_date) + '&todate=' + str(
        to_date)

    data_newest = get_data(url_newest, payload)
    data_votes = get_data(url_votes, payload)

    return render_template('home.html', data_newest=data_newest, data_votes=data_votes, zip=zip)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
