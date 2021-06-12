#customize GetAnalysis job

import sys
import os
import r2d2
from solo.logger import Logger
from ewok.runtime import Configuration

config = Configuration(sys.argv[1])

print("I have to write my own task for IC staging")
