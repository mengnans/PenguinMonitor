import os

from DataPack.DataProgram import DataProgram
from ScreenPack.IScreen import IScreen


class PiInfoScreen(IScreen):
    # <editor-fold desc="Declaration and Initial / Constructor">

    __blkTemperature = [0, 0, 0, 0, 0]

    def __init__(self):
        self.tickIndex = 0
        _temperatureInit = PiInfoScreen.__GetTemperatureCurrent()
        for i in range(0, 5):
            PiInfoScreen.__blkTemperature[i] = _temperatureInit

    # </editor-fold>

    # <editor-fold desc="Key Related Logic">

    def OnKeyboardUpdate(self):
        pass

    # </editor-fold>

    # <editor-fold desc="Update Logic">

    def OnUpdatePerSecond(self):
        PiInfoScreen.__blkTemperature[self.tickIndex] = PiInfoScreen.__GetTemperatureCurrent()
        self.tickIndex = (self.tickIndex + 1) % 5

    def OnUpdatePerMinute(self):
        pass

    # </editor-fold>

    # <editor-fold desc="Paint Logic">

    def OnPaint(self):
        pass

    # </editor-fold>

    # <editor-fold desc="Assistant Logic">

    @staticmethod
    def GetTemperatureAverage() -> float:
        value = 0
        for i in range(0, 5):
            value = value + PiInfoScreen.__blkTemperature[i]
        return value / 5

    @staticmethod
    def __GetTemperatureCurrent() -> float:
        if DataProgram.IsDebugMode:
            return 25.0
        _data = os.popen('vcgencmd measure_temp').readline()
        _data = _data.replace("temp=", "")
        _data = _data.replace("'C\n", "")
        return float(_data)

    # </editor-fold>
