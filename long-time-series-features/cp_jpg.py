# -*- coding: utf-8 -*-
import os
from shutil import copy

'''
# change this part------/
fname = 'noncough_jpg/'
n_min = '000000'
n_max = '043000'
fout = 'train_spl'
# change this part ----/
'''

def copy_file(fname,n_min,n_max,fout):
	f = os.listdir(fname)
	j = 0
	for i in range(len(f)):
		if f[i][:6] <= n_max and f[i][:6] >= n_min:
			j = j+1
			#print '%06d'%j,fname+f[i],fout
			copy(fname+f[i],fout)
	
if __name__ == '__main__':
	# copy 000001-043000 noncough to train
	
	print 'noncough val_spl----------------------'
	# copy 043001-049196 noncough to val
	fname = 'noncough_jpg/'
	n_min = '043001'
	n_max = '049196'
	fout = 'val_spl'
	copy_file(fname,n_min,n_max,fout)

	print 'noncough test_spl----------------------'
	# copy 049197-056196 noncough to test
	fname = 'noncough_jpg/'
	n_min = '049197'
	n_max = '056196'
	fout = 'test_spl'
	copy_file(fname,n_min,n_max,fout)

	print 'cough train_spl------------------------'
	# copy 056197-063196 cough to train
	fname = 'cough_jpg/'
	n_min = '056197'
	n_max = '063196'
	fout = 'train_spl'
	copy_file(fname,n_min,n_max,fout)

	print 'cough val_spl-------------------------'
	# copy 063197-067000 cough to val
	fname = 'cough_jpg/'
	n_min = '063197'
	n_max = '067000'
	fout = 'val_spl'
	copy_file(fname,n_min,n_max,fout)

	print 'cough test_spl-------------------------'
	# copy 067001-070000 cough to test
	fname = 'cough_jpg/'
	n_min = '067001'
	n_max = '070000'
	fout = 'test_spl'
	copy_file(fname,n_min,n_max,fout)


