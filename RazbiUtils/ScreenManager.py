import win32api


class Screen:
    def __init__(self, resolution: tuple):
        self.rect = resolution

    @property
    def middle_x(self):
        return int((self.rect[0]+self.rect[2]) / 2)

    @property
    def middle_y(self):
        return int((self.rect[1]+self.rect[3]) / 2)

    @property
    def top_right(self):
        return self.middle_x, self.rect[0], self.rect[2], self.middle_y

    @property
    def top_left(self):
        return self.rect[0], self.rect[1], self.middle_x, self.middle_y

    @property
    def bottom_left(self):
        return self.rect[0], self.middle_y, self.middle_x, self.rect[3]

    @property
    def bottom_right(self):
        return self.middle_x, self.middle_y, self.rect[2], self.rect[3]

    @property
    def full_screen(self):
        return self.rect

    def __str__(self):
        return f"Screen({self.rect[0]}, {self.rect[1]}, {self.rect[2]}, {self.rect[3]})"

    def __len__(self):
        return len(self.rect)

    def __iter__(self):
        yield from self.rect


class ScreenManager:
    """
    It will initialise coordinate system for all available monitors
    """
    resolutions = {}
    screens = resolutions
    for index_screen, screen_ in enumerate(win32api.EnumDisplayMonitors()):
        resolutions[index_screen] = Screen(screen_[2])
    main_screen = resolutions[0]

    def __str__(self):
        return str(self.resolutions)

    def __iter__(self):
        yield from self.resolutions.values()

    def __len__(self):
        return len(self.resolutions)

    def __getitem__(self, item):
        return self.resolutions[item]


if __name__ == '__main__':
    sm = ScreenManager()
    for screen in sm:
        print(repr(screen))








