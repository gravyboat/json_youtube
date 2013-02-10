import urllib.request
import json

url = 'http://gdata.youtube.com/feeds/api/standardfeeds/most_popular?v=2&alt=json'

if __name__ == "__main__":
    pullUrl = urllib.request.urlopen(url)
    openIt = pullUrl.readall().decode('utf-8')
    jsong = json.loads(openIt)
    topVidList = []
    for item in jsong['feed']['entry']:
        topVidList.append(item.get('title').get('$t'))
    print(topVidList[0])
