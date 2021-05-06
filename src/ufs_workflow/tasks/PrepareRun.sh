set -eux

eval $(ewok_source_config $CONFIG_FILE current_dir stage_dir)
mkdir -p $current_dir || true
cp -r $stage_dir/* $current_dir
