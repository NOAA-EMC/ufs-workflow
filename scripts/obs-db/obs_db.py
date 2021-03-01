#!/usr/bin/env python3

from solo.date import Hour
from solo.logger import Logger
from solo.configuration import Configuration
from solo.basic_files import mkdir
from r2d2 import store, fetch, date_sequence


logger = Logger('obs-db')
config = Configuration('obs-db.yaml')
dates = date_sequence(config.start, config.end, config.step)

# First archive into the local database
logger.info('preparing to copy files to local database')
store(
    type='ob',
    provider=config.ob_src,
    experiment=config.cdump,
    date=dates,
    obs_type=config.obs_type,
    _extensions='bufr_d',
    source_file=f'{config.ob_root}/{config.cdump}.$(year)$(month)$(day)/$(hour)/{config.cdump}.t$(hour)z.$(obs_type).tm00.bufr_d',
    database=config.database
)
logger.info(f'finished copying files from to database {config.database}')

# Now retrieve from archive into the local directory

logger.info('preparing to copy files from database')
for date in dates:
    ymd = Hour(date).format('%Y%m%d')
    hh = Hour(date).format('%H')
    directory = f'{config.stage}/{config.cdump}.{ymd}/{hh}'
    mkdir(directory)
    fetch(
        type='ob',
        provider=config.ob_src,
        experiment=config.cdump,
        date=date,
        obs_type=config.obs_type,
        time_window=config.step,
        file_format='bufr_d',
        target_file=f'{directory}/{config.cdump}.t$(hour)z.$(obs_type).tm00.bufr_d',
    )
    logger.info('finished copying files from local database')
