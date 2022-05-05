import pyautogui
import cv2
import win32api
import win32con
import win32gui
import datetime


def get_system_time():
    return datetime.datetime.now()


class System:

    __origin_coo = [0.0, 0.0]
    __main_pro_name = '碧蓝航线-星云引擎'

    def __init__(self):
        handle = win32gui.FindWindow(0, self.__main_pro_name)
        if handle == 0:
            raise Exception('Image %s Not Found' % self.__main_pro_name)
        else:
            x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
            self.__origin_coo = [x1, y1]

    def mouse_init(self):
        pyautogui.moveTo(self.__origin_coo)

