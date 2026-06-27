import argparse
from pathlib import Path
import yaml

from data_builder import merge_inputs

# Replace this placeholder with the full CNN-LSTM training script.
# This repository is intentionally restricted to Objective 1 training inputs only.

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', required=True)
    args = ap.parse_args()
    cfg = yaml.safe_load(open(args.config))
    sat, cpcb, met = merge_inputs(
        cfg['input_files']['satellite'],
        cfg['input_files']['cpcb'],
        cfg['input_files']['met'],
    )
    out = Path('outputs')
    out.mkdir(exist_ok=True)
    with open(out / 'config_used.yaml', 'w') as f:
        yaml.safe_dump(cfg, f)
    print('Loaded:', sat.shape, cpcb.shape, met.shape)

if __name__ == '__main__':
    main()
