from distributed.utils_test import gen_cluster
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
rois = np.ones((L, L), dtype=np.int)

print('building graph')
res = c.multi_tau_auto_corr(6, 4, rois, img_stack)

from tornado import gen

@gen_cluster(client=True)
def test_multitau(c, s, a, b):
    futures = c.compute(delayed(res))

    while not s.task_state:
        yield gen.sleep(0.1)

    for i in range(20):
        yield gen.sleep(1)
        import pdb; pdb.set_trace()
    result = yield futures
