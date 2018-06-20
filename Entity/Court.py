class Court:
    screenTimeAnalogItem = None
    screenTimeDigitalItem = None
    screenCountdownTimerItem = None
    screenPillReminderItem = None
    screenPiInfoItem = None

    screenType = None
    bottomGadget = None

    configItemAlarmClock = {"time": ["01:23", "09:00", "21:00"], "type": [0, 1, 2]}
    configItemPill = {"date": "0000", "isColinTaken": False, "isStoneTaken": False}
