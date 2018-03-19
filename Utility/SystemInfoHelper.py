import os

from DataPack.DataProgram import DataProgram


def GetTemperature():
    if DataProgram.IsDebugMode:
        return "XX"
    _data = os.popen('vcgencmd measure_temp').readline()
    _data = _data.replace("temp=", "")
    _data = _data.replace("'C\n", "")
    return int(float(_data))
