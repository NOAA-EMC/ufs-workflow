#!/usr/bin/env python
from solo.logger import Logger
from solo.basic_files import mkdir
from solo.stage import Stage
from genyaml import gen_yaml as get_config
import click


logger = Logger('stageFV3JEDI')
@click.command()
@click.argument('expdir', required=True)
def stage_fv3jedi(expdir):
    # stage fix files, etc. needed for FV3-JEDI
    # such as akbk, fieldsets, fms namelist
    # get config
    config = get_config('stageFV3JEDI', expdir, quiet=True)
    logger.info("Preparing to stage FV3-JEDI fix files")
    mkdir(config['stage_dir'])
    for stage,values in config['fv3jedi_stage_files'].items():
        print(stage, values)

if __name__ == '__main__':
    stage_fv3jedi()
