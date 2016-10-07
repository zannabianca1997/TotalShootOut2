from .start_user_interface import StartUi

import shutil
import json
import time


class Cli(StartUi):

    def __init__(self, default_terminal_size=(80, 20)):
        "setup the Cli"
        self.default_terminal_size = default_terminal_size

    # StartUi implementation

    def _start_screen(self):
        "open a start screen"
        size = self._get_terminal_size()
        # todo: change with a paths class
        data = json.load(open("assets/json/startup/start_screen.json"))
        # Printing
        print(data["content"]["title"].upper().center(size.columns))
        print()
        for line in data["content"]["subtitles"]:
            print(line.center(size.columns))
        # todo: print authors from package file
        time.sleep(data["time"])


    # utility

    def _get_terminal_size(self):
        "get the terminal size"
        return shutil.get_terminal_size(self.default_terminal_size)
