#!/usr/bin/env python
from solo.logger import Logger
from solo.basic_files import mkdir
from r2d2 import fetch
from genyaml import gen_yaml as get_config
import click

logger = Logger('stageBkg')
@click.command()
@click.argument('expdir', required=True)
def stage_bkg(expdir):
    # stage model backgrounds based on environment vars
    # and vars set in config YAMLs in experiment dir
    # get config
    config = get_config('stageBkg', expdir, quiet=True)
    logger.info(f"Preparing to stage backgrounds for {config['cycle']}")
    mkdir(config['bkg_dir'])
    # fetch the coupler file first
    fetch(
        type='fc',
        model='gfs_metadata',
        experiment=config['bkg_exp'],
        date=config['cycle'],
        step=config['forecast_steps'],
        resolution=config['model_resolution'],
        user_date_format='%Y%m%d.%H%M%S',
        fc_date_rendering='analysis',
        database=config['bkg_dir'],
        target_file=f"{config['bkg_dir']}/$(valid_date).coupler.res",
    )
    # fetch the tile files
    fetch(
        type='fc',
        model='gfs',
        experiment=config['bkg_exp'],
        date=config['cycle'],
        step=config['forecast_steps'],
        resolution=config['model_resolution'],
        user_date_format='%Y%m%d.%H%M%S',
        fc_date_rendering='analysis',
        database=config['bkg_dir'],
        target_file=f"{config['bkg_dir']}/$(valid_date).$(file_type).tile$(tile).nc",
        tile=config['bkg_tiles'],
        file_type=['fv_core.res', 'fv_srf_wnd.res', 'fv_tracer.res', 'phy_data', 'sfc_data'],
    )

if __name__ == '__main__':
    stage_bkg()
