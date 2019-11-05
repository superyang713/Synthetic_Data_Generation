import itertools
import pandas as pd
import math
from pathlib import Path


def composite_SD(means, SDs, ncounts):
    '''Calculate combined standard deviation via ANOVA (ANalysis Of VAriance)
       See: http://www.burtonsys.com/climate/composite_standard_deviations.html
       Inputs are:
         means, the array of group means
         SDs, the array of group standard deviations
         ncounts, the array of number of samples in each group
       Result is the overall standard deviation.
    '''
    num_groups = len(means)
    if num_groups != len(SDs) or num_groups != len(ncounts):
        raise Exception('inconsistent list lengths')

    # calculate total number of samples, N, and grand mean, GM
    N = sum(ncounts)
    if N == 1:
        return SDs[0]
    GM = 0.0
    for i in range(num_groups):
        GM += means[i] * ncounts[i]
    GM /= N

    # calculate Error Sum of Squares
    ESS = 0.0
    for i in range(num_groups):
        ESS += ((SDs[i]) ** 2) * (ncounts[i] - 1)

    # calculate Total Group Sum of Squares
    TGSS = 0.0
    for i in range(num_groups):
        TGSS += ((means[i] - GM) ** 2) * ncounts[i]

    # calculate standard deviation as square root of grand variance
    result = math.sqrt((ESS + TGSS)/(N - 1))
    return result


def create_transunion_csv():
    """
    This python script is used to merge all the parquet data files into one
    single csv file. TransUnion data needs to be partitioned into 10 different
    csv files due to the memory limitation.
    """
    num_partition = 10
    data_dir = Path("data/transunion/")
    num_files = math.ceil(len(list(data_dir.glob("*.parquet"))) / num_partition)

    for i in range(num_partition):

        df = pd.concat(
            pd.read_parquet(parquet_file, engine="pyarrow")
            for parquet_file in itertools.islice(data_dir.glob("*.parquet"), i *
                                                num_files, (i + 1) * num_files))
        df.to_csv("data/transunion_{}.csv".format(i))


def expand_df(df, columns):
    """
    Parameters:
    ----------
    df: pd.series
    Each cell holds a 2d array.
    colums: list
    Column names for the expanded DataFrame.

    Return:
    -------
    A expanded DataFrame.
    """
    df = df.explode()
    df = df.apply(pd.Series)
    df.rename(columns=lambda x: columns[x], inplace=True)
    return df

