import pandas as pd

def load_csv(path):
    return pd.read_csv(path)

def merge_inputs(sat_path, cpcb_path, met_path):
    sat = load_csv(sat_path)
    cpcb = load_csv(cpcb_path)
    met = load_csv(met_path)
    return sat, cpcb, met
