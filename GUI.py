import cv2
import pyautogui


class Button:

    __BTN_Tuple = ('WEIGH_ANCHOR', 'RESEARCH', 'EXIT', 'RETURN', 'GOAROUND')
    __BTN_Coo_Map = {'WEIGH_ANCHOR': [163, 547], 'RETURN': [85, 75]}

    name = ''

    center_coordinate = [0.0, 0.0]

    def __init__(self, name):
        if not (name in self.__BTN_Tuple):
            raise Exception('Button name not Available: {}'.format(name))
        else:
            self.name = name
            self.center_coordinate = self.__BTN_Coo_Map[name]


class GUI:

    Current_state = ''

    def __init__(self):
        self.Current_state = 'Main_Window'

    def update_state(self, state):
        self.Current_state = state

    def main_window_click_button(self, button):
        if self.Current_state != 'Main_Window':
            raise Exception('There is no Button %s in Window %s' % (button.name, self.Current_state))
        else:
            if button.name == 'WEIGH_ANCHOR':
                pass

