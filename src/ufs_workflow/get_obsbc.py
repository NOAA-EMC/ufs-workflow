from solo.date import Hour, JediDate, DateIncrement
from solo.logger import Logger
from solo.configuration import Configuration
from solo.basic_files import mkdir
from r2d2 import fetch, date_sequence
import sys

logger = Logger('getObsBC')
config = Configuration(sys.argv[1])
dates = date_sequence(config.cycle_begin, config.cycle_end, config.cycle_step)

# Retrieve obs to working directory
logger.info('Preparing to copy bias correction files to working directory.')
for date in dates:
    for obtype in config.observations:
        fetch(
            type='bc',
            provider=config.bc_src,
            experiment=config.bc_experiment,
            date=date,
            obs_type=obtype,
            target_file=f'{config.ob_dir}/$(obs_type).$(date).tlapse.txt',
            file_type='tlapse',
            ignore_missing=True,
            database=config.r2d2_database
        )
        fetch(
            type='bc',
            provider=config.bc_src,
            experiment=config.bc_experiment,
            date=date,
            obs_type=obtype,
            target_file=f'{config.ob_dir}/$(obs_type).$(date).satbias.nc4',
            file_type='satbias',
            ignore_missing=True,
            database=config.r2d2_database
        )
