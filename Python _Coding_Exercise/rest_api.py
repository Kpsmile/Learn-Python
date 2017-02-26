
import json
import os
import urllib2
import requests
import shutil

class api(object):
    def __init__(self, *args):
        self.data = []
    global dump

    def request_data(self, *args):

        response = urllib2.urlopen('http://content.guardianapis.com/search?api-key=test&show-fields=thumbnail,headline')
        get_data = response.read()
        result_data = json.loads(get_data)['response']['results']
        res=[d['fields'] for d in result_data]
        img_href=[each['thumbnail'] for each in res]
        print(len(img_href))
        for each_img in img_href: 
             file = requests.get(each_img, stream=True)
             for index, each_img in enumerate(img_href):
                with open('img_'+str(index)+'.png', 'wb') as location:
                    shutil.copyfileobj(file.raw, location)
                
        print('Success')
                
            
if __name__ == "__main__":
    output = api()
    output.request_data()