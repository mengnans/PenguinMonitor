from abc import abstractmethod


class IScreen:
    isForceUpdate = False

    @abstractmethod
    def OnUpdate(self):
        pass

    @abstractmethod
    def OnPaint(self):
        pass

    @staticmethod
    def ForceUpdate():
        IScreen.isForceUpdate = True
