import data_utils

x, y = data_utils.load_gtsrb_data(data_utils.FLAGS.data_dir)

print x.shape
print y.shape


