from dask import delayed
import dask
import numpy as np
import skbeam.core.correlation as c
from imp import reload
reload(c)

L = 2048

print('making image stack')
# img_stack = np.cumsum(np.random.randn(10, L, L), 0)

img_stack = [delayed(np.random.random)((L, L)) for i in range(10)]
rois = np.zeros((L, L), dtype=np.int)
rois[10:20, 10:20] = 1

print('building graph')
res = c.multi_tau_auto_corr(6, 4, rois, img_stack)
