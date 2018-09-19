"""Statistic for grouped data. 

All the functions support the formats:

- two arrays (the fists is the classes and the second is the frequency)
- A dict like (we sugest a counter)

"""

import numpy as np

def split_groups(dictlike):
    grp, cnt = [], []
    for k, v in dictlike.items():
        grp.append(k)
        cnt.append(v)
    return np.asarray(grp), np.asarray(cnt)


def mean(grp, cnt=None):
    if cnt is None:
        grp, cnt = split_groups(grp)
    num = np.sum(grp * cnt).astype(float)
    den = np.sum(cnt).astype(float)
    return num / den

"""def median(grp, cnt=None)
    if cnt is None:
        grp, cnt = split_groups(grp)"""
    