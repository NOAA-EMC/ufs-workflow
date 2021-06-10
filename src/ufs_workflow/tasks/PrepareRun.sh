set -eux

eval $(ewok_source_config $CONFIG_FILE current_dir stage_dir)
mkdir -p $current_dir || true
cp -r $stage_dir/* $current_dir
cd $current_dir

module use /home/jkuang/opt/modulefiles/apps
module load ufs_test/1.0.0

cat << EOF > conf_var.py
#!/usr/bin/python3
import sys
import os
from ewok.configuration import processing as ps
from solo.template import TemplateConstants, Template
config = Configuration(sys.argv[1], silent=True)
with open('input.nml','w+') as fd:
    temp = fd.readlines()
    input_nml = Template.substitute_structure(temp, TemplateConstants.AT_SQUARE_BRACES, config.get)
    fd.write(input_nml)

fd.close()

EOF

chmod 755 conf_var.py

./conf_var.py
