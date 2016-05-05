import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.examples.tutorials.mnist import mnist

# Loads training/validation/test sets
mnist_data = input_data.read_data_sets('MNIST_data', one_hot=True)

session = tf.InteractiveSession()


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
