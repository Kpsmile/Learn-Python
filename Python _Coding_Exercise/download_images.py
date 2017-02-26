import requests  
from lxml import html  
import sys
import os
import urlparse
import pdb; pdb.set_trace()

response = requests.get('https://media.guim.co.uk/43b232940616ef539e80483d5e3cfbfdea0ab29c/0_346_5407_3244/500.jpg')  
parsed_body = html.fromstring(response.text)

# Grab links to all images
images = parsed_body.xpath('//img/@src')  
if not images:  
    sys.exit("Found No Images")

# Convert any relative urls to absolute urls
images = [urlparse.urljoin(response.url, url) for url in images]  
print 'Found %s images' % len(images)
os.mkdir("downloaded_images")

# Only download first 10
for url in images[0:10]:  
    import pdb;pdb.set_trace()
    r = requests.get(url)
    f = open('downloaded_images/%s' % url.split('/')[-1], 'w')
#     f = open('downloaded_images', 'w')
    f.write(r.content)
    f.close()