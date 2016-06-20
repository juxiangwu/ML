import numpy as np
import tensorflow as tf
import os
import csv
import cv2

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string('data_dir', os.getcwd() + '/datasets/gtsrb_training',
                           """Path to the GTSRB data directory.""")

tf.app.flags.DEFINE_integer('num_classes', 43, """Number of classes in GTSRB training dataset""")


def load_gtsrb_data(path, cut_roi=True):
    x, y = [], []
    for i in xrange(1):
        prefix = path + '/' + format(i, '05d') + '/'
        # annotations file
        with open(prefix + 'GT-' + format(i, '05d') + '.csv') as gt_file:
            xx, yy = _parse_annotations(prefix, gt_file, cut_roi)
            x.append(xx), y.append(yy)

    x = np.concatenate(x)
    y = np.concatenate(y)
    return x, y


def _parse_annotations(prefix, gt_file, cut_roi):
    reader = csv.reader(gt_file, delimiter=';')
    # skip header
    reader.next()

    x, y = [], []
    for row in reader:
        # first column of csv file is filename
        image = cv2.imread(prefix + row[0])
        # remove regions surrounding the actual traffic sign
        if cut_roi:
            image = image[np.int(row[4]):np.int(row[6]), np.int(row[3]):np.int(row[5]), :]
        # scale each image to 32 * 32
        image = cv2.resize(image, (32, 32))
        x.append(image)
        y.append(row[7])

    return x, y
