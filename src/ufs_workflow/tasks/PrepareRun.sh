set -eux

eval $(ewok_source_config $CONFIG_FILE current_dir stage_dir)
mkdir -p $current_dir || true
cp -r $stage_dir/* $current_dir
cd $current_dir

module use /home/jkuang/opt/modulefiles/apps
module load ufs_test/1.0.0

cat << EOF > conf_var.py
import sys
import os
from ewok.runtime import Configuration
from solo.template import TemplateConstants, Template
config = Configuration(sys.argv[1], silent=True)
with open('input.nml','r+') as fd:
    temp = fd.read()
    input_nml = Template.substitute_structure(temp, TemplateConstants.AT_SQUARE_BRACES, config.get)
    fd.write(input_nml)

fd.close()

with open('model_configure','r+') as fd:
    temp = fd.read()
    input_nml = Template.substitute_structure(temp, TemplateConstants.AT_SQUARE_BRACES, config.get)
    fd.write(input_nml)

fd.close()

EOF

python conf_var.py $suite_dir/ufs.yaml
