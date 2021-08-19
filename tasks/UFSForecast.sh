#!/bin/bash

set -eux
echo -n " $( date +%s )," >  job_timestamp.txt

eval $(ewok_source_config $CONFIG_FILE ufsforecast_tasks)

set +x
source ./module-setup.sh
module use .
module load modules.ufs_model
module list
set -x

ulimit -s unlimited

echo "Model started:  " `date`

export OMP_STACKSIZE=512M
export KMP_AFFINITY=scatter
export OMP_NUM_THREADS=1

srun --label -n $ufsforecast_tasks ./ufs_model

echo "Model ended:    " `date`
echo -n " $( date +%s )," >> job_timestamp.txt
