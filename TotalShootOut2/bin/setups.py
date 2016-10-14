import os, logging
logger = logging.getLogger(__name__.upper())

class BunchDict(dict):
    def __init__(self,**kw):
        dict.__init__(self,kw)
        self.__dict__.update(kw)

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
    set_path = paths["json"]
    global json
    json = rec_load_jsons(set_path)


def rec_load_jsons(set_path):
    for f in os.listdir(set_path):
        f = os.path.join(set_path, f)
        if os.path.isfile(f):
            print("file", f)
        elif os.path.isdir(f):
            print("dir", f)