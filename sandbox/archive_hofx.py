#!/usr/bin/env python
from solo.logger import Logger
from r2d2 import store
from genyaml import gen_yaml as get_config
import click
from solo.netcdf import NetCDF
from netCDF4 import Dataset
import glob
import os
import shutil

logger = Logger('archHofx')
@click.command()
@click.argument('expdir', required=True)

def archiveHofx(expdir):
    # concatenate H(x) output files and store them in
    # a specified R2D2 database
    # get config
    config = get_config('archHofx', expdir, quiet=True)
    logger.info(f"Preparing to concatenate and archive H(x) output files")
    for ob in config['observations']:
        obname = ob['obs space']['name'].lower()
        logger.info(f"Processing {obname}...")
        # output is current_dir in JEDI-GDAS, not an ideal name, but using it for compatibility
        hofxdir = config['current_dir']
        netcdf_files = []
        filenames = sorted(glob.glib(os.path.join(hofxdir,f"*{obname}*_????.nc4")))
        print(filenames)   
