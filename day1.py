import numpy as np
import pandas as pd

data = pd.read_csv('input_files/day1.txt', header=None, skip_blank_lines=False)
lis = np.array(data[0])
missing_val_indices = np.where(np.isnan(lis))[0]
split_lis = np.split(lis, missing_val_indices)
out = list(map(np.nansum, split_lis))
out = np.sort(np.array(out))[::-1][0:3]
print(np.sum(out))