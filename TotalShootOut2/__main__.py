# Main starting file of the program

# logging system
import logging
logging.basicConfig(level = logging.DEBUG)

#for dir navigation
from os import path
#read the setups
import setups
# import the ui
from start_ui import Ui as StartUi

def main():
    """The main program course"""
    #find dir
    prj_dir = path.dirname(path.realpath(__file__))

    #load setups
    setups.load(prj_dir)

    # create the start Ui
    start_ui = StartUi()
    # start the program
    start_ui.show()

    # stop the logging
    logging.shutdown()


if __name__ == '__main__':
    main()
