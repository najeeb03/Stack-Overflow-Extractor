# Loading form local file to test json parsing
import json


with open('stack-overflow-questions.json') as my_file:
    data = json.load(my_file)

for item in data['items']:
    print ('Question: ' + item['title'])
    print 'By: ' + item['owner']['display_name']
    print 'tags: ',
    for tag in item['tags']:
        print tag,
