from client.client_setups import client_setups
from server.server_setups import server_setups


class StartUi:
    """A class representing the start screen"""

    def show(self):
        "open the ui"
        self._start_screen()
        if self._ask_if_server():
            self._launch_server()
        else:
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
