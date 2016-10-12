print("Loading interface...")

#define the modules loaded with "from start_ui import *"
__all__ = ["cli"]

#using cli
from .cli import Cli as Ui