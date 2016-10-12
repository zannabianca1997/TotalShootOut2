import os

class BunchDict(dict):
    def __init__(self,**kw):
        dict.__init__(self,kw)
        self.__dict__.update(kw)

json = None
paths = None

def load_all(prj_path):
    #create paths dictionary
    mount_paths(prj_path)


def mount_paths(prj_path):
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