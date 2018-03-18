from abc import abstractmethod


class IScreen:

    @abstractmethod
    def OnUpdate(self):
        pass

    @abstractmethod
    def OnPaint(self):
        pass

    @abstractmethod
    def OnKeyDown(self):
        pass
