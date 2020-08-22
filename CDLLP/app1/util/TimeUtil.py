import time


def getCurrentDate():
    date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    return date

def getCurrentDate1():
    date = time.strftime("%Y%m%d", time.localtime(time.time()))
    return date

def getCurrentMonth():
    date = time.strftime("%Y_%m", time.localtime(time.time()))
    print(date)
    return date


def getCurrentTime():
    date = time.strftime("%H:%M:%S", time.localtime(time.time()))
    return date

def getCurrentTime1():
    date = time.strftime("%H%M%S", time.localtime(time.time()))
    return date

def getCurrentTimeAndDate():
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return date
