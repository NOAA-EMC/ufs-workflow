#!/usr/bin/env python
from solo.logger import Logger
from solo.configuration import Configuration
from solo.template import TemplateConstants, Template
import click
import os

config_dict = {
    'hofx': ['base', 'hofx'],
}

@click.command()
@click.argument('task', required=True)
@click.argument('expdir', required=True)
@click.argument('yamlout', required=True)
def gen_yaml(task, expdir, yamlout):
    # parse, concatenate, replace vars in YAML and write a new
    # YAML file for the specified task/executable/script
    # get list of config YAMLs to read
    config_list = get_config_list(task)
    # read all initial configs
    config = Configuration(os.path.join(expdir,'base.yaml'))
    for yamlfile in config_list:
        yamlpath = os.path.join(expdir,f'{yamlfile}.yaml')
        tmp_config = Configuration(yamlpath)
        config = config.update(tmp_config)
    print(config)

def get_config_list(task):
    # for the specified task, return a list of YAML files
    # that need to be 'sourced'
    config_list = config_dict[task]
    return config_list

if __name__ == '__main__':
    gen_yaml()
