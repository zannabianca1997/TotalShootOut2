from client.client_setups import client_setups
from server.server_setups import server_setups
import setups

import logging


class StartUi:
    """A class representing the start screen"""

    def __init__(self):
        """inizialize the Ui"""
        super().__init__()
        self.start_screen_data = setups.data.startup.start_screen

    def show(self):
        "open the ui"
        logger = logging.getLogger(__name__)
        logger.info("Opening start screen")
        self._start_screen()
        logger.info("Asking if server")
        if self._ask_if_server():
            logger.info("Server was choosed")
            self._launch_server()
        else:
            logger.info("Client was choosed")
            self._launch_client()

    # do the stuffs

    def _launch_server(self):
        "load the server and launch it"
        raise NotImplementedError

    def _launch_client(self):
        "ask the remote server ip and lauch the client"
        raise NotImplementedError

    # actual User Interface

    def _start_screen(self):
        "visualize the starting screen"
        raise NotImplementedError

    def _ask_if_server(self) -> bool:
        "Ask if you want to open the server or client"
        raise NotImplementedError

    def _ask_client_setups(self, remote_server) -> client_setups:
        "Ask the user to enter client setups (username, ship type, etc...)"
        raise NotImplementedError

    def _ask_remote_server_ip(self) -> str:
        "Ask the user to choose a server"
        raise NotImplementedError

    def _ask_server_setups(self) -> server_setups:
        "Ask the usee to enter the local server setups (ram, assetspack, etc...)"
        raise NotImplementedError
