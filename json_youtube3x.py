import urllib.request
import json

# This version doesn't work yet.

url = 'http://gdata.youtube.com/feeds/api/standardfeeds/most_popular?v=2&alt=json'

if __name__ == "__main__":
    pullUrl = urllib.request.urlopen(url)
    openIt = urllib.request.build_opener()
    openIt.addheaders = ['utf-8']
    f = openIt.open(url)
    jsong = json.load(f)
    topVidList = []
    for item in jsong['feed']['entry']:
        topVidList.append(item.get('title').get('$t'))
    print(topVidList[0])
