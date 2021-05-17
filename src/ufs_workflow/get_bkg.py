from solo.date import Hour, DateIncrement
from solo.logger import Logger
from solo.configuration import Configuration
from solo.basic_files import mkdir
from r2d2 import fetch, date_sequence
import sys

logger = Logger('getBkg')
config = Configuration(sys.argv[1])
dates = date_sequence(config.cycle_begin, config.cycle_end, config.cycle_step)

logger.info('Preparing to copy RESTART files to working directory')
for date in dates:
    mkdir(config.bkg_dir)
    # fetch the metadata
    fetch(
        type='fc',
        model='gfs_metadata',
        experiment=config.experiment,
        date=date,
        step=config.forecast_steps,
        resolution=config.resolution,
        user_date_format='%Y%m%d.%H%M%S',
        fc_date_rendering='analysis',
        database=config.r2d2_database,
        target_file=f'{config.bkg_dir}/$(valid_date).coupler.res',
        )
    # fetch the tile files
    fetch(
        type='fc',
        model='gfs',
        experiment=config.experiment,
        date=date,
        step=config.forecast_steps,
        resolution=config.resolution,
        user_date_format='%Y%m%d.%H%M%S',
        fc_date_rendering='analysis',
        database=config.r2d2_database,
        target_file=f'{config.bkg_dir}/$(valid_date).$(file_type).tile$(tile).nc',
        tile=config.tiles,
        file_type=['fv_core.res', 'fv_srf_wnd.res', 'fv_tracer.res', 'phy_data', 'sfc_data'],
        )
