import os


class DataProgram:
    IsDebugMode = True
    UpdatePerSecond = 60

    @staticmethod
    def Init():
        _data = os.popen('vcgencmd measure_temp').readline()
        DataProgram.IsDebugMode = _data == ""
