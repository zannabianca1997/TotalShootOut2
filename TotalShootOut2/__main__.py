# Main starting file of the program

#for dir navigation
from os import path, getcwd, chdir
# logging system
import logging, sys
#read the setups
import setups

def main():
    """The main program course"""
    #logging start
    logging.basicConfig(level = logging.DEBUG)

    #find dir
    prj_dir = path.dirname(path.realpath(__file__))

    #load setups
    setups.load_all(prj_dir)

    # create the start Ui
    # import the ui
    from start_ui import Ui as StartUi
    start_ui = StartUi()
    # start the program
    start_ui.show()

    # stop the logging
    logging.shutdown()


if __name__ == '__main__':
    main()
