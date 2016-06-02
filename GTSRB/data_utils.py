import cPickle as pickle
import numpy as np


def load_gtsrb_batch(filename):
    """ load single batch """
    with open(filename, 'rb') as f:
        datadict = pickle.load(f)
        x = datadict['data']
        y = datadict['labels']
        x = x.reshape(10000, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
        y = np.array(y)
        return x, y
