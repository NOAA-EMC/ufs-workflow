echo "sourcing the UFS forecast environment"

set +x
source ./module-setup.sh
module use .
module load modules.ufs_model
module list
set -x

ulimit -s unlimited

export OMP_STACKSIZE=512M
export KMP_AFFINITY=scatter
export OMP_NUM_THREADS=1
