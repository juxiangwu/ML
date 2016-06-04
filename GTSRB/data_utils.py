import numpy as np
import tensorflow as tf
import os
import csv
import cv2

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_integer()
tf.app.flags.DEFINE_string('data_dir', os.getcwd() + '/datasets/gtsrb_training',
                           """Path to the GTSRB data directory.""")

tf.app.flags.DEFINE_integer('num_classes', 43, """Number of classes in GTSRB training dataset""")


def load_gtsrb_data(path, cut_roi=True):
    images = {'x': [], 'y': []}
    for i in xrange(FLAGS.num_classes):
        prefix = path + '/' + format(i, '05d') + '/'
        # annotations file
        with open(prefix + 'GT-' + format(i, '05d') + '.csv') as gt_file:
            datadict = _parse_annotations(prefix, gt_file, cut_roi)
            images['x'].extend(datadict['x']), images['y'].extend(datadict['y'])

    return images


def _parse_annotations(prefix, gt_file, cut_roi):
    reader = csv.reader(gt_file, delimiter=';')
    # skip header
    reader.next()

    images = {'x': [], 'y': []}
    for row in reader:
        # first column of csv file is filename
        image = cv2.imread(prefix + row[0])
        # remove regions surrounding the actual traffic sign
        if cut_roi:
            image = image[np.int(row[4]):np.int(row[6]), np.int(row[3]):np.int(row[5]), :]
        images['x'].append(image)
        images['y'].append(row[7])

    return images
