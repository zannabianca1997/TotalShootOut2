#!/usr/bin/env python3
# Main starting file of the program

# logging system
import logging
#for finding modules navigation
from os import path
import sys, pprint


def main():
    """The main program course"""
    #start logging
    start_logging()
    #setup pypath
    set_pypath() #now i can refere to local modules
    #load the setups
    load_setups()
    try:
        # create the start Ui
        start_ui = create_start_ui()
        # start the program
        start_ui.show()
    except Exception:
        logging.getLogger(__name__).exception(
            "An exception has been raised from the game, and not stopped"
        )
        raise
    finally:
        # stop the logging
        logging.getLogger(__name__).info("Logging End")
        logging.shutdown()




def start_logging():
    logging.basicConfig(level = logging.INFO)
    #the logging will be finer after the setups will be read

def set_pypath():
    """Add project dir to pypath"""
    logger = logging.getLogger(__name__)
    #find dir
    global prj_dir #all accessible
    prj_dir = path.dirname(path.realpath(__file__))
    logger.info("Project localized in %s", prj_dir)
    sys.path.insert(0, path.join(prj_dir, "bin"))
    logger.debug("Actual PYTHONPATH:\n%s", pprint.pformat(sys.path))

def load_setups():
    "read the setups"
    logger = logging.getLogger(__name__)
    import setups
    global setups
    logger.info("Loading setups")
    setups.load(prj_dir)

def create_start_ui():
    logger = logging.getLogger(__name__)
    logger.debug("Creating StartUi")
    # import the ui
    from start_ui import Ui as StartUi
    start_ui = StartUi()
    return start_ui

if __name__ == '__main__':
    main()
