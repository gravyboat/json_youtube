import urllib2
import json
url = 'http://gdata.youtube.com/feeds/api/standardfeeds/most_popular?v=2&alt=json'

if __name__ == "__main__":
    pullUrl = urllib2.Request(url)
    openIt = urllib2.build_opener()
    f = openIt.open(pullUrl)
    jsong = json.load(f)
    topVidList = []
    for item in jsong['feed']['entry']:
        topVidList.append(item.get('title').get('$t'))
    print(topVidList[0])
