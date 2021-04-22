from solo.date import Hour
from solo.logger import Logger
from solo.configuration import Configuration
from solo.basic_files import mkdir
from r2d2 import store, fetch, date_sequence


logger = Logger('soca-obs-db')
config = Configuration('soca-obs-db.yaml')
dates = date_sequence(config.start, config.end, config.step)

# First archive into the local database
logger.info('preparing to copy files to local database')
for obs_type in config.obs_type:
    store(
        type='ob',
        experiment=config.experiment,
        provider=config.ob_src,
        date=dates,
        obs_type=config.obs_type,
        source_file=f'{config.ob_root}/$(year)/$(year)$(month)$(day)/{obs_type}_$(year)$(month)$(day).nc',
        time_window=config.step,
        database=config.database
    )
logger.info(f'finished copying files from to database {config.database}')

# Now retrieve from archive into the local directory

logger.info('create target directory to stage files into')
for date in dates:
    year = Hour(date).format('%Y')
    ymd = Hour(date).format('%Y%m%d')
    directory = f'{config.stage}/{year}/{ymd}'
    mkdir(directory)

logger.info('preparing to copy files from database')
for obs_type in config.obs_type:
    fetch(
        type='ob',
        provider=config.ob_src,
        experiment=config.experiment,
        date=dates,
        obs_type=obs_type,
        time_window=config.step,
        target_file=f'{config.stage}/$(year)/$(year)$(month)$(day)/{obs_type}_$(year)$(month)$(day).nc',
    )
logger.info('finished copying files from local database')
