import sys
import os
from solo.logger import Logger
from solo.stage import Stage
from ewok.runtime import Configuration


logger = Logger(os.environ['EWOK_TASK'])
config = Configuration(sys.argv[1], silent=True)

model_info = config.get_model_info()

if 'STAGE' in model_info:
    logger.info('staging data found, processing it')
    stage_file = os.path.join(config.suite_files, 'ufs-workflow', 'ewok')
    for staging in model_info['STAGE_MODEL']:
        path = os.path.dirname(stage_file)
        stage = Stage(path, config.stage_dir, staging, config)
