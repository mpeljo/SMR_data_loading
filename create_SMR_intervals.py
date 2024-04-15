# Code written by Neil Symington. It reads depth and "Credible Interval"
#   info from probabilistic inversion SMR data, and formats it into
#   a nice output for use in generating GA Oracle ROCKPROPS database
#   Excel upload template files.

import os, glob
import pandas as pd
import numpy as np

infile = r"\\prod.lan\active\proj\futurex\DCD\Data\Processed\Geophysics\SMR\results\depths.csv"

depth_from = pd.read_csv(infile, header=None).values[:, 0]
depth_to = np.nan * np.ones(depth_from.shape, dtype=float)
depth_to[:-1] = depth_from[1:]
depth_to[-1] = depth_to[-2] + (depth_from[-1] - depth_from[-2]) * 1.028

indir = r"\\prod.lan\active\proj\futurex\DCD\Data\Processed\Geophysics\SMR\results"

df_smr = pd.DataFrame(
    columns=["site_name", "depth_from", "depth_to", "p5", "p50", "p95"]
)

for file in glob.glob(os.path.join(indir, "*CI_results.csv")):
    site_name = file.split("\\")[-1].split("_FID")[0]
    print(site_name)
    df_site = pd.read_csv(file, names=["p5", "p50", "p95"])
    df_site["depth_from"] = depth_from
    df_site["depth_to"] = depth_to
    df_site["site_name"] = site_name
    df_smr = df_smr.append(df_site)

outfile = r"\\prod.lan\active\proj\futurex\DCD\Data\Processed\Geophysics\SMR\results\SMR_data_for_registration-8April2024.csv"
df_smr.to_csv(outfile, index=False)
