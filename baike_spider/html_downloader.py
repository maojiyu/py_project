import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        response = requests.get(url)
        response.encoding = 'utf-8'
        if response.status_code != 200:
            return None
        return response.text
        # response = urllib2.urlopen(url)
        #
        # if response.getcode() != 200:
        #     return None
        #
        # return response.read()
