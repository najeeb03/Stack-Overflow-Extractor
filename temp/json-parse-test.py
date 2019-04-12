# Testing JSON parsing
# import json

# Loading form local file to test json parsing
"""with open('stack-overflow-questions.json') as my_file:
    data = json.load(my_file)

for item in data['items']:
    print ('Question: ' + item['title'])
    print 'By: ' + item['owner']['display_name']

    print 'tags: ',
    for tag in item['tags']:
        print tag,
"""

# Getting the JSON data directly from an API call
import requests

url_newest = 'http://api.stackexchange.com/2.2/questions?pagesize=10&fromdate=1554508800&todate=1555027200' \
             '&order=desc&sort=creation&tagged=android&site=stackoverflow'
url_votes = 'http://api.stackexchange.com/2.2/questions?pagesize=10&fromdate=1554508800&todate=1555027200' \
           '&order=desc&sort=votes&tagged=android&site=stackoverflow'

r = requests.get(url_votes)

if r.ok:
    data = r.json()

    for item in data['items']:
        print ('Question: ' + item['title'])
        print 'By: ' + item['owner']['display_name']

        print 'tags: ',
        print ", ".join(str(tag) for tag in item['tags'])
