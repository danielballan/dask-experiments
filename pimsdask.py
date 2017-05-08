import dask.array as da
from skimage.io import imsave
import numpy as np
a = np.ones((100, 100))
for i in range(20):
    imsave('/tmp/pics/img{:02}.png'.format(i), i/100 * a)
    
import pims
imgs = pims.ImageSequence('/tmp/pics/*.png')
arr = da.from_array(imgs, chunks=(3, *imgs.frame_shape))
import dask
