from DataPack.DataProgram import DataProgram


def OnDebug(func):
    def wrapper(*args, **kw):
        if DataProgram.IsDebugMode is False:
            return None
        else:
            return func(*args, **kw)
    return wrapper
