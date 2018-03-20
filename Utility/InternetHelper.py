import urllib.request
import json


class InternetHelper:

    @staticmethod
    def GetExternalIP():
        _url = "http://ip.jsontest.com/"
        _fullData = json.loads(urllib.request.urlopen(_url).read().decode("utf-8"))
        _ip = _fullData["ip"]
        return _ip
