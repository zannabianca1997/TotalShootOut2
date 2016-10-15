from .base_ui import StartUi
import setups
import logging

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
        logger = logging.getLogger(__name__)
        logger.debug("Printing start screen")
        size = self._get_terminal_size()
        # Printing
        print(self.start_screen_data.content.title.upper().center(size.columns))
        print()
        for line in self.start_screen_data.content.subtitles:
            print(line.center(size.columns))
        print()
        for type, names in setups.data.general.credit.items():
            print("{}: {}".format(type,", ".join(names)))
        logger.info("Opened start screen")
        time.sleep(self.start_screen_data.time)
        logger.info("Ended start screen")


    def _ask_if_server(self) -> bool:
        "Ask if you want to open the server or client"
        logger = logging.getLogger(__name__)
        while True: #user can be as stupid as he want
            ch = input("{} [{}/{}]".format(self.setup.ask_server.message,*self.setup.ask_server.options))
            if ch in self.setup.ask_server.options:
                if ch == self.setup.ask_server.options[0]:
                    return True
                else:
                    return False



    # utility

    def _get_terminal_size(self):
        "get the terminal size"
        t_size = shutil.get_terminal_size(self.setup.default_terminal)
        logging.getLogger(__name__).debug("Terminal size: (%d,%d)",*t_size)
        return t_size
