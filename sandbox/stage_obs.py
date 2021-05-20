#!/usr/bin/env python
from solo.date import Hour, JediDate, DateIncrement
from solo.logger import Logger
from solo.basic_files import mkdir
from r2d2 import fetch, date_sequence
import .genyaml.gen_yaml as get_config

logger = Logger('stageObs')
@click.command()
@click.argument('expdir', required=True)
def stage_obs(expdir):
    # stage observations based on environment vars
    # and vars set in config YAMLs in experiment dir
    # get config
    config = get_config('stageObs', expdir, quiet=True, readonly=True)
    print(config)
    #logger.info('Preparing to stage observations for {cycle}')

if __name__ == '__main__':
    stage_obs()
