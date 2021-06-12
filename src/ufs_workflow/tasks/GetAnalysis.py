#customize GetAnalysis job

import sys
import os
import r2d2
from solo.logger import Logger
from ewok.runtime import Configuration

logger = Logger(os.environ['EWOK_TASK'])
config = Configuration(sys.argv[1])

print("I have to write my own GetAnalysis")
