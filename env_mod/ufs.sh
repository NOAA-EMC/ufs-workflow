echo "sourcing the UFS forecast environment"

#source ./module-setup.sh
module use .
module load modules.ufs_model
module list

ulimit -s unlimited

export OMP_STACKSIZE=512M
export KMP_AFFINITY=scatter
export OMP_NUM_THREADS=1
