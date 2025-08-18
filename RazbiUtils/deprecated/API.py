import pyautogui
from .screen_grabber import grab_screen
import cv2
import os
import time
import win32gui
from .ScreenManager import ScreenManager, Screen


class ScreenScraper:
    def __init__(self, starting_path="", templates_path=""):
        """
The main object used for screen scraping.
The path to search for files is starting_path/templates_path/img"""
        self.path = {"starting_path": starting_path,
                     'templates_path': templates_path}

        self.chests_collected_so_far = 0
        self.image_cache_colored = {}
        self.image_cache_gray_scaled = {}

    @staticmethod
    def screenshot(region=None, show=False, color='gray'):
        """
        To call bare-bones screenshot use 'from RazbiUtils import grab_screen'
        :param region: tuple | if not provided, it will use the full screen of the main screen
        :param show: bool | true if you want to see how the screenshot looks like it makes it, it also blocks the program while doing so
        :param color: str | colors are RGB, BGR and GRAY
        :return:
        """
        if not region:
            region = (0, 0, *pyautogui.size())
        elif isinstance(region, (tuple, list)):
            if len(region) != 4:
                raise ValueError(f"Type expected tuple/list/Screen, type got {type(region)}")

        elif isinstance(region, Screen):
            region = region.rect
        else:
            raise ValueError(f"Type expected tuple/list/Screen, type got {type(region)}")

        while True:
            s = grab_screen(region=region, color=color)
            if show:
                cv2.imshow('test', s)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break
            else:
                break
        return s

    def with_start(self, path):
        if self.path["starting_path"] == '':
            return path
        return os.path.join(self.path["starting_path"], path)

    def find_on_screen(self, image_path: str, screenshot=None, confidence=0.75, color=False):
        """
        The path to search for files is starting_path/templates_path/img
        By default starting_path and templates_path are empty strings
        :param image_path: string
        :param screenshot: numpy array of the screen, if given a 4-length tuple or list, it will screenshot at those coordinates
        :param confidence: int, threshold for the detection
        :param color: bool, False = grayscale, True or higher = RGB | grayscale is faster
        :return: a list of places where the image was found, if None found returns an empty list
        """
        if screenshot is None:
            screenshot = self.screenshot()
        elif len(screenshot) == 4 and isinstance(screenshot, (tuple, list, Screen)):
            where_to_screenshot = screenshot
            screenshot = self.screenshot(where_to_screenshot)

        if image_path.endswith('.png'):
            image_path = image_path[:-4]
        try:
            if color:
                needle = self.image_cache_colored[image_path]
            else:
                needle = self.image_cache_gray_scaled[image_path]
        except KeyError:
            path_to_image = f'{self.with_start(os.path.join(self.path["templates_path"], image_path.lower()))}.png'
            if color:
                needle = cv2.imread(path_to_image)
                self.image_cache_colored[image_path] = needle
            else:
                needle = cv2.imread(path_to_image, 0)
                self.image_cache_gray_scaled[image_path] = needle

        res = None
        try:
            res = list(pyautogui.locateAll(needle, screenshot, confidence=confidence))
        except NameError:
            pass
        except TypeError:
            print(f'Image at the path "{path_to_image}" not found.')

        if not res:
            return []
        return res

    def find_on_screen_bool(self, image_path: str, screenshot=None, confidence=0.75, color=False):
        """
        Identical to find_on_screen, but it returns a True if at least one element detected and False otherwise
        """
        if self.find_on_screen(image_path, screenshot, confidence=confidence, color=color):
            return True
        return False

    @staticmethod
    def get_selected_window():
        """
        Uses win32gui to get the foreground window
        :return: hwnd of the selected window
        """
        return win32gui.GetForegroundWindow()

    @staticmethod
    def set_selected_window(window_hwnd: int):
        """
        Uses win32gui to set the foreground window
        :param window_hwnd: hwnd
        """
        return win32gui.SetForegroundWindow(window_hwnd)

    @staticmethod
    def sleep(amount):
        time.sleep(amount)

    @classmethod
    def center(cls, box):
        return pyautogui.center(box)


if __name__ == '__main__':
    # time.sleep(2)
    sc = Screenscraper()
    sm = ScreenManager()
    path_to_template = "thing"  # any
    for screen in sm:
        if sc.find_on_screen_bool(path_to_template, screen.bottom_right):
            print("Chat found")



