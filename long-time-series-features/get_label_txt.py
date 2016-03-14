import os

#fjpg = 'val_spl'

def generate_txt(fjpg):
	n = '056196'
	print 'processing',fjpg
	out_txt = fjpg + '.txt'
	if os.path.exists(out_txt):
		os.remove(out_txt)
		print out_txt,'already exists, and will be removed!'
	
	f = os.listdir(fjpg)
	fid = open(out_txt,'a')
	
	for i in range(len(f)):
		print i
		if f[i][:6] <= n:
			label = '0'
		else:
			label = '1'
		content = f[i] + ' ' + label +'\n'
		fid.write(content)
	
	fid.close()

fjpg = 'train_spl'
generate_txt(fjpg)

fjpg = 'test_spl'
generate_txt(fjpg)

