import logging
logger = logging.getLogger(__name__.upper())

import os
import json as js

class _BunchDict(dict):
    def __init__(self,kw):
        super().__init__()
        for (key, value) in kw.items():
            assert isinstance(key,str)

            value = self.recursive_bunching(value)

            if key.find(".") == -1: #no dots in name
                self.__dict__[key] = value
            else:
                logger.warn("Ignored dotted key '%s'",key)
            self[key] = value

    def recursive_bunching(self, value):
        if issubclass(type(value), dict):
            value = _BunchDict(value)  # itero la transformazione
        if issubclass(type(value), list):
            for i, val in enumerate(value):
                value[i] = self.recursive_bunching(val)
        return value


json = None
paths = None

def load_all(prj_path):
    logger.info("Loading setups...")
    #create paths dictionary
    _mount_paths(prj_path)
    #load all jsons
    _load_jsons()


def _mount_paths(prj_path):
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

def _load_jsons():
    logger.info("Loading jsons...")
    global json
    json = _load_dir(paths["json"]) #loading the path
    logger.debug("Loaded data: %s",str(json))


def _load_dir(dir):
    result = dict()
    logger.debug("Navigating %s...", dir)
    for name in os.listdir(dir):
        file = os.path.join(dir, name)
        if os.path.isfile(file):
            result[name] = _load_file(file)
        elif os.path.isdir(file):
            result[name] = _load_dir(file)
    return _BunchDict(result)

def _load_file(file):
    logger.debug("Loading %s", file)
    try:
        with open(file, "r") as f:
            data = js.load(f)
            return _BunchDict(data)
    except ValueError as e:
        logger.exception("Problem in decoding %s:", file.name)
        return e #comunque il gioco contimua, forse ci si salva
    except IOError as e:
        logger.exception("Problem in reading %s:", file.name)
        return e #comunque il gioco contimua, forse ci si salva
    except Exception
        logger.exception("Unknow exception in IO with %s", file.name)
        raise #non sappiamo che è, reinviamo
