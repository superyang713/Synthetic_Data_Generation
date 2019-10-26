"""
This python script is used to merge all the parquet data files into one single
csv file.
"""
import itertools
import math
from pathlib import Path
import pandas as pd


# TransUnion data needs to be partitioned into 10 different csv files due to
# the memory limitation.
num_partition = 10
data_dir = Path("data/transunion/")
num_files = math.ceil(len(list(data_dir.glob("*.parquet"))) / num_partition)

for i in range(num_partition):

    df = pd.concat(
        pd.read_parquet(parquet_file, engine="pyarrow")
        for parquet_file in itertools.islice(data_dir.glob("*.parquet"), i *
                                             num_files, (i + 1) * num_files))
    df.to_csv("data/transunion_{}.csv".format(i))
