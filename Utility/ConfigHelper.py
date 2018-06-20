import json

from Entity.Court import Court


class ConfigHelper:
    @staticmethod
    def LoadFromFile():
        try:
            _readFile = open("ConfigData.dat", "r")
            _alarmClockContent = _readFile.readline()
            _pillContent = _readFile.readline()
            _readFile.close()
            Court.configItemAlarmClock = json.loads(_alarmClockContent)
            Court.configItemPill = json.loads(_pillContent)
        except:
            Court.configItemAlarmClock = {"time": ["00:00", "09:00", "21:00"], "type": [0, 0, 0]}
            Court.configItemPill = {"date": "0000", "isColinTaken": False, "isStoneTaken": False}
            ConfigHelper.SaveToFile()
            pass

    @staticmethod
    def SaveToFile():
        __recordFile = open("ConfigData.dat", "w")
        _alarmClockContent = json.dumps(Court.configItemAlarmClock)
        _pillContent = json.dumps(Court.configItemPill)
        __recordFile.write(_alarmClockContent + "\n")
        __recordFile.write(_pillContent + "\n")
        __recordFile.flush()
        __recordFile.close()
