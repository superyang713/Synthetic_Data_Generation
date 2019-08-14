import math


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
