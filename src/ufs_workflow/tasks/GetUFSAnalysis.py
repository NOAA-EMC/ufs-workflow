import sys
import os
import shutil
import r2d2
import yaml
from solo.logger import Logger
from ewok.runtime import Configuration, EwokR2d2

config = Configuration(sys.argv[1])

print("I have to write my own task for IC staging")

#INPUT folder
EwokR2d2.fetch(
    config.get('R2D2'),
    experiment=config.init_exp,
    date=config.current_cycle,
    model=config.model,
    type='an',
    resolution=config.horizontal_resolution,
    target_file=config.AN_TEMPLATE.filename,
    database=config.r2d2_fetch_database
)

# shutil.copyfile('/work/noaa/stmp/jkuang/stmp/jkuang/FV3_RT/rt_hold/control_c192/INPUT/gfs_data.tile1.nc', config['current_dir'])
