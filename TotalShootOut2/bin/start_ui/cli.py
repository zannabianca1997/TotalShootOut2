from .start_user_interface import StartUi
import setups

import shutil
import time


class Cli(StartUi):

    def __init__(self):
        "setup the Cli"
        super().__init__()
        self.setup = setups.data.startup.cli_setup

    # StartUi implementation

    def _start_screen(self):
        "open a start screen"
        size = self._get_terminal_size()
        # Printing
        print(self.start_screen_data.content.title.upper().center(size.columns))
        print()
        for line in self.start_screen_data.content.subtitles:
            print(line.center(size.columns))
        print()
        for type, names in setups.data.general.credit.items():
            print("{}: {}".format(type,", ".join(names)))
        time.sleep(self.start_screen_data.time)


    # utility

    def _get_terminal_size(self):
        "get the terminal size"
        return shutil.get_terminal_size(self.setup.default_terminal)
