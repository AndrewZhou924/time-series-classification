import numpy as np
import caffe
caffe_root = '/home/hhwang/software/caffe/'
import sys
sys.path.insert(0, caffe_root + 'python')
caffe.set_mode_cpu()
net = caffe.Net(caffe_root+'examples/12thPlpCepstrum/deploy.prototxt', caffe_root+'examples/12thPlpCepstrum/caffenet_train_iter_13000.caffemodel', caffe.TEST)


transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2, 0, 1))
transformer.set_mean('data', np.load(caffe_root+'data/12thPlpCepstrum/imagenet_mean.npy').mean(1).mean(1))
transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2, 1, 0))


TEST_FILE = caffe_root+'data/12thPlpCepstrum/test1.txt'
inputs = []
groundTruths = []
predictions = []
file = open(TEST_FILE)
for each_line in file:
	(i, g) = each_line.split(' ', 1)
	inputs.append(i)
	groundTruths.append(int(g))
net.blobs['data'].reshape(1, 3, 227, 227)
for idx in range(len(inputs)):
	net.blobs['data'].data[...] = transformer.preprocess('data', caffe.io.load_image(caffe_root+'data/12thPlpCepstrum/test1/' + inputs[idx]))
	out = net.forward()
	predictions.append(out['prob'].argmax())
	with open('results.txt','a') as f:
		f.write(inputs[idx]+' '+str(groundTruths[idx])+' '+str(predictions[idx])+'\n')
print predictions
table = np.zeros((2, 2))
for idx in range(len(predictions)):
	table[groundTruths[idx]][predictions[idx]] += 1
	
print table
col = np.sum(table, axis = 0)
row = np.sum(table, axis = 1)
presicion = table / col
recall = table / row
print presicion
print recall
print np.sum(predictions)/float(len(predictions))
