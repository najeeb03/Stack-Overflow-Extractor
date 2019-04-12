# Loading form local file to test json parsing
import json


with open('stack-overflow-questions.json') as my_file:
    data = json.load(my_file)

for items in data['items']:
    print ('Question: ' + items['title'])
    print 'By: ' + items['owner']['display_name']
    print 'tags: ',
    for tags in items['tags']:
        print tags,
