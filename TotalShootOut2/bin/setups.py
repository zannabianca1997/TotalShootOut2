import os, logging
logger = logging.getLogger(__name__.upper())

class BunchDict(dict):
    def __init__(self,kw):
        super().__init__()
        for (key, value) in kw.items():
            if issubclass(type(value),dict):
                value = BunchDict(value) #itero la transformazione
            self[key] = value
            self.__dict__[key] = value


json = None
paths = None

def load_all(prj_path):
    logger.info("Loading setups...")
    #create paths dictionary
    mount_paths(prj_path)
    #load all jsons
    load_jsons()


def mount_paths(prj_path):
    logger.info("Loading paths...")
    bin_path = os.path.join(prj_path, "bin")
    ass_path = os.path.join(prj_path, "assets")
    jsn_path = os.path.join(ass_path, "json")
    spr_path = os.path.join(ass_path, "sprite")
    global paths
    paths = {
        "bin": bin_path,
        "assets": ass_path,
        "json": jsn_path,
        "sprite": spr_path
    }
    logger.debug("Setted paths:\n   %s" , ", \n    ".join(str(paths).split(", ")))

def load_jsons():
    logger.info("Loading jsons...")
    global json
    json = load_dir(paths["json"]) #loading the path


def load_dir(dir):
    result = dict()
    logger.debug("Navigating %s...", dir)
    for name in os.listdir(dir):
        file = os.path.join(dir, name)
        if os.path.isfile(file):
            result[name] = load_file(file)
        elif os.path.isdir(file):
            result[name] = load_dir(file)
    return BunchDict(result)

def load_file(file):
    logger.debug("Loading %s", file)