import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.examples.tutorials.mnist import mnist


def placeholder_inputs(batch_size):
    x = tf.placeholder(tf.float32, shape=[batch_size, mnist.IMAGE_PIXELS])
    y = tf.placeholder(tf.float32, shape=[batch_size])
    return x, y


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, [1, 1, 1, 1], 'SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, [1, 2, 2, 1], [1, 2, 2, 1], 'SAME')


# Loads training/validation/test sets
mnist_data = input_data.read_data_sets('MNIST_data', one_hot=True)
session = tf.InteractiveSession()

# conv - relu - pooling layer
w_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])
x, y = placeholder_inputs()
x_image = tf.reshape(x, [-1, 28, 28, 1])

h_conv1 = tf.nn.relu(conv2d(x_image, w_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

# conv - relu - pooling layer
w_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, w_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

# FC - relu layer
w_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, w_fc1) + b_fc1)

# Dropout
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# FC - softmax layer
w_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

scores = tf.nn.softmax(tf.matmul(h_fc1_drop, w_fc2) + b_fc2)
