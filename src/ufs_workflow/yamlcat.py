from solo.logger import Logger
from solo.configuration import Configuration
from solo.template import TemplateConstants, Template
import sys

incstr = '$<<'
# read in the root YAML file
config = Configuration(sys.argv[1])
print(config)
print('-----------')
# replace variables
config = Template.substitute_structure_from_environment(config)
config = Template.substitute_with_dependencies(config, TemplateConstants.DOLLAR_PARENTHESES)
print(config)
print('-----------')
# 'include' includes
for rootkey, rootval in config.items():
    if type(rootval) is list:
        newlist = []
        for item in rootval:
            if incstr in item:
                itemstr = item.replace(incstr,'')
                incpath = itemstr.strip()
                newconfig = Configuration(incpath)
                newlist.append(newconfig)
            else:
                newlist.append(item)
        config[rootkey] = newlist
    else:
        if incstr in rootval:
            itemstr = rootval.replace(incstr,'')
            incpath = itemstr.strip()
            newconfig = Configuration(incpath)
            config[rootkey] = newconfig
print('-----------')
print(config)
print('-----------')
# replace variables again
config = Template.substitute_structure_from_environment(config)
config = Template.substitute_with_dependencies(config, TemplateConstants.DOLLAR_PARENTHESES)
# add in runtime var replacement
config['window_begin'] = '2021-05-20T09:00:00Z'
config['background_time'] = '2021-05-20T12:00:00Z'
config['current_cycle'] = config['background_time']
config = Template.substitute_structure(config, TemplateConstants.DOUBLE_CURLY_BRACES, config.get)
print(config)
print('-----------')
# save to file
config.save(target_dir='./', target_name='testout.yaml')
