# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__.upper())

import os
import json
import pprint

class _BunchDict(dict):
    """This dict can be called with both ["item"] and .item notation"""
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
        "Transform a dict of list of dicts... in a Bunch"
        if issubclass(type(value), dict):
            value = _BunchDict(value)  # itero la transformazione
        if issubclass(type(value), list):
            for i, val in enumerate(value):
                value[i] = self.recursive_bunching(val) #se è un oggetto normale non gli farà niente
        return value


data = None
paths = None

def load(prj_path):
    "Load all setups. Receive the project path as argument"
    logger.info("Loading setups...")
    #create paths dictionary
    _mount_paths(prj_path)
    #load all jsons
    _load_setups()


def _mount_paths(prj_path):
    "Create paths dict"
    logger.info("Loading paths...")
    bin_path = os.path.join(prj_path, "bin")
    ass_path = os.path.join(prj_path, "assets")
    jsn_path = os.path.join(ass_path, "data")
    spr_path = os.path.join(ass_path, "sprite")
    global paths
    paths = {
        "bin": bin_path,
        "assets": ass_path,
        "data": jsn_path,
        "sprite": spr_path
    }
    logger.debug("Setted paths:\n%s" , pprint.pformat(paths))

def _load_setups():
    "loads all files from data directory"
    logger.info("Loading jsons...")
    global data
    data = _load_dir(paths["data"]) #loading the path
    logger.debug("Loaded data:\n%s", pprint.pformat(data))


def _load_dir(dir):
    "load all file and subdir in the memory"
    result = dict()
    logger.debug("Navigating %s...", dir)
    for name in os.listdir(dir):
        file = os.path.join(dir, name)
        if os.path.isfile(file):
            name_parts = name.split('.')
            if len(name_parts)>2:
                name_parts=["_".join(name_parts[:-1]),name_parts[-1]]
                logger.warn("Duble dots in %s. Will be saved as %s",file,name_parts[0])
            if name_parts[1]=="json": #can be added support to multiple file types
                result[name_parts[0]] = _load_json(file)
            else:
                logger.info("Ignored unknown file type %s: %s",name_parts[1],file)
        elif os.path.isdir(file):
            result[name] = _load_dir(file)
    return _BunchDict(result)

def _load_json(file):
    "load a file in the memory"
    logger.debug("Loading %s", file)
    try:
        with open(file, "r") as f:
            data = json.load(f)
            return _BunchDict(data)
    except ValueError as e:
        logger.exception("Problem in decoding %s:", file.name)
        return e #comunque il gioco contimua, forse ci si salva
    except IOError as e:
        logger.exception("Problem in reading %s:", file.name)
        return e #comunque il gioco contimua, forse ci si salva
    except Exception:
        logger.exception("Unknow exception in IO with %s", file.name)
        raise #non sappiamo che è, reinviamo
