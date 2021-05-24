#!/bin/bash
source /work/noaa/da/Cory.R.Martin/noscrub/UFO_eval/env/ioda_diags.env.bash

ulimit -s unlimited

gitdir=/work/noaa/da/Cory.R.Martin/noscrub/git/ufs-workflow/
hofxexe=/work/noaa/da/Cory.R.Martin/noscrub/JEDI/stable/fv3-bundle/build/bin/fv3jedi_hofx_nomodel.x

cd $gitdir/sandbox

python stage_bkg.py ./
python stage_obs.py ./
python stage_fv3jedi.py ./
python genyaml.py hofx ./ hofxyaml.yaml
srun -n6 $hofxexe hofxyaml.yaml
python archive_hofx.py ./
