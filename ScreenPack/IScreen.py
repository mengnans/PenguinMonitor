from abc import abstractmethod


class IScreen:
    isForceUpdate = False

    @abstractmethod
    def OnUpdate(self):
        pass

    @abstractmethod
    def OnUpdateSecond(self):
        pass

    @abstractmethod
    def OnUpdateMinute(self):
        pass

    @abstractmethod
    def OnPaint(self):
        pass

    @staticmethod
    def ForceUpdate():
        IScreen.isForceUpdate = True

    @staticmethod
    def PaintShadowText(argCanvas, argFont, argContent, argColor, argLocation):
        argCanvas.blit(argFont.render(argContent, True, (128, 128, 128)), (argLocation[0] + 5, argLocation[1] + 5))
        argCanvas.blit(argFont.render(argContent, True, argColor), argLocation)

    @staticmethod
    def PaintShadowTextOffset(argCanvas, argFont, argContent, argColor, argLocation, argOffset):
        argCanvas.blit(argFont.render(argContent, True, (128, 128, 128)), (argLocation[0] + argOffset, argLocation[1] + argOffset))
        argCanvas.blit(argFont.render(argContent, True, argColor), argLocation)
