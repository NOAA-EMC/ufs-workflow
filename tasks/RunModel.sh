#!/bin/bash

set -eux
echo -n " $( date +%s )," >  job_timestamp.txt

set +x
source ./module-setup.sh
module use $( pwd -P )
module load modules.ufs_model
module list

set -x

ulimit -s unlimited

echo "Model started:  " `date`

export OMP_STACKSIZE=512M
export KMP_AFFINITY=scatter
export OMP_NUM_THREADS=1

# Ideally something like:
# ntasks=$(ewok_source_config $CONFIG_FILE forecast:tasks)
# exec=$(ewok_source_config $CONFIG_FILE forecast:exec)
#srun --label -n $ntasks $exec

srun --label -n %EWOK_TASKS% ./ufs_model

echo "Model ended:    " `date`
echo -n " $( date +%s )," >> job_timestamp.txt
