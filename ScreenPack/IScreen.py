from abc import abstractmethod


class IScreen:
    @abstractmethod
    def Tick(self):
        pass

    @abstractmethod
    def OnKeydown(self):
        pass
