import pynput
import pyautogui
import time


class InputController:
    """
    Class for controlling mouse and keyboard, it's a wrapper around pynput
    """
    mouse = pynput.mouse.Controller()
    keyboard = pynput.keyboard.Controller()
    mouse_buttons = pynput.mouse.Button
    key = pynput.keyboard.Key

    @classmethod
    def current_mouse_pos(cls):
        return cls.mouse.position

    @classmethod
    def click(cls, coordinates=None, duration=0, frame_rate=60):
        """
        :param coordinates: list/tuple
        :param duration: int | delay to move the mouse, if also coordinates provided
        :param frame_rate: int | the frame_rate of the application:
        browsers usually have 60 fps
        if the frame_rate is lower than the app frame_rate, clicks may not be registered
        if the frame_rate is higher than the app frame_rate, delay between clicks can be lower
        :return: None
        """
        if coordinates:
            pyautogui.moveTo((coordinates[0], coordinates[1]), duration=duration)
        cls.mouse.press(cls.mouse_buttons.left)
        time.sleep(1/frame_rate)
        cls.mouse.release(cls.mouse_buttons.left)

    @staticmethod
    def move_to(coordinates):
        pyautogui.moveTo(coordinates)

    @classmethod
    def press(cls, key_to_press):
        cls.keyboard.press(key_to_press)

