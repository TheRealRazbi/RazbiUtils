# RazbiUtils

This package contains utils for scripts/RPA.
Most functionality is using the windows API, hence limited linux support

```pip install RazbiUtils```

# Examples

### Hiding a python window

```python
import time
from razbi_utils.core import hide_window

WINDOW_TITLE = "Some Program"


def main():
    print("I am doing very useful stuff, I wanna do that in the background")
    while True:
        time.sleep(10)
        print(f"Did some useful stuff right now {time.strftime('%H:%M:%S')}")

if __name__ == '__main__':
    hide_window(WINDOW_TITLE)
    main()
```
^ Now if you run a batch script that runs this script, and you make a shortcut to it and name it "Some Program"
When you start the "Some Program.lnk" it will hide it on-start, can be very useful for python listener scripts

For showing the window, you need to run `show_window(WINDOW_TITLE)` 

### Support/Contributions
If you have any suggestions, please make a pull request. 
If there's activity, I will create a discord server and update this README.md
