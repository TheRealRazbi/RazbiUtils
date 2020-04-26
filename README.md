# RazbiUtils

This package is a wrapper around  win32api, pyautogui and pynput intended for ScreenScrapping.

`pip install RazbiUtils`

RazbiUtils supports at least python 3.6 and I've tested it only on **windows**. No guarantee that will work on **linux**.


The API is designed to be similar to **pyautogui**, but to fix a lot of the issues pyautogui has.


The first issue it solves is the mouse input, by using internally **pynput** for mouse clicks and keyboard keys, this assures that all the programs/games will receive the input. Which wasn't a problem for chrome, but it was on many other random programs.


The second issue was both the click speed and the **screenshot** speed. The click speed was fixed once again by **pynput** and for the screenshot I used something written using win32api by **Frannecklp** [Here's a link to the origin of the screenshot <https://pythonprogramming.net/next-steps-python-plays-gta-v/>]


The third issue I attempt to solve is to make it work for multiple monitors and to make the coordinate system easier, by letting you specify portions of the screen without specific coordinates. I've fixed this by detecting the monitors using win32api and organising it.

# Examples

### Basic template detection
```python
from RazbiUtils import ScreenScrapper

sc = ScreenScrapper()

path_to_template = 'object_to_detect'
if sc.find_on_screen_bool(path_to_template):
    print("Object Detected")
```

Assuming that you have a path to an actual **.png** that it's on the main screen right now. The script should be able to detect it.
[For managing template images, I strongly recommend paint.net <https://www.dotpdn.com/downloads/pdn.html> as it's free, easy to use and lighweight]

Ok, but let's make a little more interesting: let's make it click on the found object:

```python
from RazbiUtils import ScreenScrapper, InputController

sc = ScreenScrapper()

path_to_template = 'object_to_detect'
found = sc.find_on_screen(path_to_template)
if found:
    print(f"Object Detected at {found[0]}")
    InputController.click(sc.center(found[0]))
```
```Object Detected at Box(left=1590, top=951, width=189, height=54)```

Note that I use `found[0]` instead of just `found`, because the screenshot by default returns a list of all found objects, [0] being the first.
Also note that you if you don't use sc.center(), you'll use only the top-left of the detected image.

### Multi-monitor support:
Let's say you want to screenshot something visible on your second monitor, pyautogui is normally unable to do this, but with RazbiUtils you just do:
```python
from RazbiUtils import ScreenScrapper, ScreenManager

sc = ScreenScrapper()

path_to_template = 'object_to_detect'
if sc.find_on_screen_bool(path_to_template, ScreenManager.screens[1]):
    print("Object Detected")
```
The order of the screens are basically, the order you set in the OS.

Also if you want to screenshot just specific parts to make the screenshot fast without actual coordinates you can do:
`ScreenManager.screens[0].bottom_right` for just the bottom right. Also you can do `ScreenManager.main_screen` which is equivalent with `ScreenManager.screens[0]`

Note: You can also instantiate ScreenManager if you want to reference it in a shorter form like `sm`


### Mouse clicks support on ANY app

I'm referring to just clicks, mouse movements won't work certainly. 
Keep in mind that internally it uses `pynput` for clicks, so if you just want that, just use `pynput`.

The InputController.click() has a parameter for `framerate` by default 60.
That means the delay between clicks is 1/60 which is 0.016, which will guarantee it will register the click if the app is 60fps.

For some reason the pyautogui clicks don't work on most games, so feel free to use this library or `pynput` for clicks

### Support
If you have any suggestions, please make a pull request, so far I added only features I use really often for ScreenScrapping, but I'm sure I haven't covered everything that's being used by everyone.
