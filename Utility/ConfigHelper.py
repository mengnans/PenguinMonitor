import json

from DataPack.Court import Court


class ConfigHelper:
    @staticmethod
    def LoadFromFile():
        # try:
        _readFile = open("ConfigData.dat", "r")
        _alarmClockContent = _readFile.readline()
        _pillContent = _readFile.readline()
        _readFile.close()
        _abc = json.loads(_alarmClockContent)
        _def = json.loads(_pillContent)
        Court.configItemAlarmClock = json.loads(_alarmClockContent)
        Court.configItemPill = json.loads(_pillContent)
        # except:
        #     pass

    @staticmethod
    def SaveToFile():
        __recordFile = open("ConfigData.dat", "w")
        _alarmClockContent = json.dumps(Court.configItemAlarmClock)
        _pillContent = json.dumps(Court.configItemPill)
        __recordFile.write(_alarmClockContent + "\n")
        __recordFile.write(_pillContent + "\n")
        __recordFile.flush()
        __recordFile.close()
