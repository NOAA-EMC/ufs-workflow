set -eux

eval $(ewok_source_config $CONFIG_FILE current_dir stage_dir suite_dir)
mkdir -p $current_dir || true
cp -r $stage_dir/* $current_dir
cd $current_dir

#module use /home/jkuang/opt/modulefiles/apps
#module load ufs_test/1.0.0

cat << EOF > conf_var.py
import sys
import os
from ewok.runtime import Configuration
from solo.template import TemplateConstants, Template
config_toplevel = Configuration(sys.argv[1], silent=True)

config = {}
def expand_config(d):
    for key, value in d.items():
        if isinstance(value, dict):
             expand_config(value)
        else:
             config[key] = value

expand_config(config_toplevel)

with open('input.nml','r') as fd:
    temp = fd.read()
    fd.close()

input_nml_content = Template.substitute_structure(temp, TemplateConstants.AT_SQUARE_BRACES, config.get)
with open('input.nml','w') as fd:
    fd.write(input_nml_content)
    fd.close()

with open('model_configure','r') as fd:
    temp = fd.read()
    fd.close()

model_configure_content = Template.substitute_structure(temp, TemplateConstants.AT_SQUARE_BRACES, config.get)
with open('model_configure','w') as fd:
    fd.write(model_configure_content)
    fd.close()

with open('diag_table','r') as fd:
    temp = fd.read()
    fd.close()

diag_table_content = Template.substitute_structure(temp, TemplateConstants.DOLLAR_PARENTHESES, config.get)
with open('diag_table','w') as fd:
    fd.write(diag_table_content)
    fd.close()

EOF

python conf_var.py $suite_dir/ufs.yaml
