#!/bin/sh
#SBATCH --job-name=Forecast
#SBATCH --account=da-cpu
#SBATCH --partition=orion
#SBATCH --qos=batch
#SBATCH --ntasks-per-node=12
#SBATCH --cpus-per-task=12
#SBATCH --nodes=1
#SBATCH --time=00:30:00

set -eux

eval $(ewok_source_config $CONFIG_FILE current_dir stage_dir)
cd $current_dir
pwd
cp /work/noaa/marine/Jian.Kuang/ufs-weather-model/build/ufs_model .

srun ufs_model
