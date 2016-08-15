import requests
import time
from datetime import datetime

MIME_TYPE_JSON = 'application/json'
CONTENT_TYPE = 'Content-type'


def api_handler(i):
    response = None

    try:
        begin = datetime.now()

        response = requests.get("https://ctqa.dsc.umich.edu/access/content/public/ok.txt")
        print "what is in response: " + response.text

        end = datetime.now()
        diff = end - begin
        print str(i) + " execution time: " + str(diff)

    except (requests.exceptions.RequestException, Exception) as exception:
        raise exception

    return response


print 'started at: ' + str(datetime.now())

for i in range(1, 2000):
    api_handler(i)

print 'ended at: ' + str(datetime.now())
