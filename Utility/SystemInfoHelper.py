import os

from DataPack.DataProgram import DataProgram


class SystemInfoHelper:

    @staticmethod
    def GetTemperature() -> float:
        if DataProgram.IsDebugMode:
            return 25.0
        _data = os.popen('vcgencmd measure_temp').readline()
        _data = _data.replace("temp=", "")
        _data = _data.replace("'C\n", "")
        return float(_data)
