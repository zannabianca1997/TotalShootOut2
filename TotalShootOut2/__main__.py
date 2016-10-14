# Main starting file of the program


#for finding modules navigation
from os import path
import sys
#find dir
prj_dir = path.dirname(path.realpath(__file__))
sys.path.append(path.join(prj_dir, "bin"))


# logging system
import logging
logging.basicConfig(level = logging.DEBUG,filename="out.log")

#read the setups
import setups
# import the ui
from start_ui import Ui as StartUi

def main():
    """The main program course"""

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
