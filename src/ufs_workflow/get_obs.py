from solo.date import Hour, JediDate, DateIncrement
from solo.logger import Logger
from solo.configuration import Configuration
from solo.basic_files import mkdir
from r2d2 import store, fetch, date_sequence

logger = Logger('getObs')
config = Configuration(sys.argv[1])
dates = date_sequence(config.cycle_begin, config.cycle_end, config.cycle_step)

# Retrieve obs to working directory
logger.info('Preparing to copy observations to working directory.')
for date in dates:
    window_start = str(JediDate(date) - DateIncrement(config.cycle_step)/2.)
    for obtype in config.observations:
        filename = config['observations'][obtype]['obsdatain']
        r2d2.fetch(
        type='ob',
        provider=config.ob_src,
        experiment=config.ob_dump,
        date=config.window_begin,
        obs_type=obtype,
        time_window=config.cycle_step,
        target_file=filename,
        ignore_missing=True,
        database=config.r2d2_database
    )
