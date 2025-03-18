## datasets_searchpath_plugins

SearchPath plugins are automatically discovered and enabled after installation. They provide configuration files (*.yaml) for datasets corresponding to specific tasks.

### Key Features

- **Automatic Configuration Discovery**: Users can easily discover and create configurations tailored to their needs.

- **Hydra Integration**: Automatically extends Hydra with the keyword **"base"**, allowing for the addition of extra configurations within existing configuration groups.

- **Configuration Priority**: Hydra prepends its configurations, ensuring they take precedence over any configurations they are intended to replace.

- **Flexible Overrides**: Configurations can be replaced flexibly to suit various requirements.

This setup simplifies the management of datasets and enhances the flexibility of configuration management.


### Usage
To install the package, run:
```
pip install -e .
```

Then, execute:

```
udl_share_conf /path/to/your/conf
```

In your your_work_cfg.yaml, look for base: xxx, which indicates that you can find the configuration file in the conf directory.

```yaml
defaults:
  - base: xxx
  - _self_
```

base.yaml
```yaml
# * UDL_CIL configuration
# command: python
retry_count: 0
failed_trial_id: -1
n_jobs: 1 # "concurrency number"
debug: false
merge_keys: ["base", "args"]

# * Base configuration
backend: "accelerate"
seed: 10
accumulated_step: 1
grad_clip_norm: null
grad_clip_value: null
find_unused_parameters: false
reg: true
crop_batch_size: 32

# Log configuration
use_log: true
log_dir: "logs"
use_colorlog: true
tfb_dir: null
use_tfb: false
by_epoch: true
eval_flag: false
formatter: "model_{epoch}_{iter}_{metrics}"
validate: false

# Save configurationq
use_save: true
reset_lr: false
save_top_k: 1
save_latest_limit: 1
load_model_strict: true
load_optimizer_strict: true
use_post_train: false # whether to reset the model parameters before training in engine
resume_mode: "latest" # auto load latest model, then convert latest+best for saving model during the training process
start_save_epoch: 1
earlyStopping: true
save_fmt: ["png"]
code_dir: []
start_epoch: 1
start_iter: 1
start_save_best_epoch: 200
revise_keys: '[(r"^module\.", "")]'
prefix_model: ""

# Accelerate Training configuration
fp16_cfg: {}
fp16: false
fp_scaler: false
mixed_precision: null # options: null, fp16, bf16, fp8

# Test configuration
once_epoch: false

# Runner configuration
runner_mode: "epoch"
img_range: 1
precision: 5
mode: null
detect_anomalous_params: false
launcher: "pytorch"
ema_decay: 0.999
use_ema: false

# Distributed configuration
global_rank: 0
dist_params:
  backend: "nccl"
```


pansharpening.yaml
```yaml
defaults:
  - runtime

task: "pansharpening"
scale: [1]
metrics: { "train": "loss"}
save_fmt: ["mat", "png"] # options: mat, not mat
test_mode: ["reduce", "full"] # options: reduce, full experiment
test_samples_per_gpu: 20
img_scale: { "wv3": 2047.0, "gf2": 1023.0, "qb": 2047.0 }
```



---

Feel free to contact me:  
**Email**: [Xiao.Wu@mbzuai.ac.ae](mailto:Xiao.Wu@mbzuai.ac.ae)

## License & Copyright

Copyright (c) 2025 Xiao Wu, MBZUAI and UESTC.

This project is open sourced under GNU General Public License v3.0.


