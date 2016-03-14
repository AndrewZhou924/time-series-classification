# -*- coding: utf-8 -*-


import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from mpl_toolkits.axes_grid1 import make_axes_locatable
import cPickle
import os

def paa(series, now, opw):
    if now == None:
        now = len(series) / opw
    if opw == None:
        opw = len(series) / now
    return [sum(series[i * opw : (i + 1) * opw]) / float(opw) for i in range(now)]

def window_time_series(series, n, step = 1):
#    print "in window_time_series",series
    if step < 1.0:
        step = max(int(step * n), 1)
    return [series[i:i+n] for i in range(0, len(series) - n + 1, step)]
    
def standardize(serie):
    dev = np.sqrt(np.var(serie))
    mean = np.mean(serie)
    return [(each-mean)/dev for each in serie]

def rescale(serie):
    maxval = max(serie)
    minval = min(serie)
    gap = float(maxval-minval)
    return [(each-minval)/gap for each in serie]
    
def rescaleminus(serie):
    maxval = max(serie)
    minval = min(serie)
    gap = float(maxval-minval)
    return [(each-minval)/gap*2-1 for each in serie]

def QMeq(series, Q):
    q = pd.qcut(list(set(series)), Q)
    dic = dict(zip(set(series), q.codes))
    MSM = np.zeros([Q,Q])
    label = []
    for each in series:
        label.append(dic[each])
    for i in range(0, len(label)-1):
        MSM[label[i]][label[i+1]] += 1
    for i in xrange(Q):
        if sum(MSM[i][:]) == 0:
            continue
        MSM[i][:] = MSM[i][:]/sum(MSM[i][:])
#    MSM = MSM/float(np.sum(MSM))
    return np.array(MSM), label, q.categories

def QVeq(series, Q):
    q = pd.qcut(list(set(series)), Q)
    dic = dict(zip(set(series), q.labels))
    qv = np.zeros([1,Q])
    label = []
    for each in series:
        label.append(dic[each])
    for i in range(0,len(label)):
        qv[0][label[i]] += 1.0        
    return np.array(qv[0][:]/sum(qv[0][:])), label
    
def paaMarkovMatrix(paalist,level):
    paaindex = []
    for each in paalist:    
        for k in range(len(level)):
            lower = float(level[k][1:-1].split(',')[0])
            upper = float(level[k][1:-1].split(',')[-1])
            if each >=lower and each <= upper:
                paaindex.append(k)
    return paaindex
        
def gengrampdfs(image,paaimage,label,name):
    import matplotlib.backends.backend_pdf as bpdf
    import operator
    index = zip(range(len(label)),label)
    index.sort(key = operator.itemgetter(1))
    with bpdf.PdfPages(name) as pdf:
        for p,q in index:
            print 'generate fig of pdfs:',p
            plt.ioff();fig= plt.figure();#plt.suptitle(datafile+'_'+str(label[p]));ax1 = plt.subplot(121);plt.imshow(image[p]);divider = make_axes_locatable(ax1);cax = divider.append_axes("right", size="5%", pad=0.1);plt.colorbar(cax = cax);ax2 = plt.subplot(122);plt.imshow(paaimage[p]);divider = make_axes_locatable(ax2);cax = divider.append_axes("right", size="5%", pad=0.1);plt.colorbar(cax = cax);
            pdf.savefig(fig)
            #plt.close(fig)
    #pdf.close

def pickle3data(mat, label, train, name):
    print '..pickling data:',name
    traintp = (mat[:train], label[:train])
    validtp = (mat[:train], label[:train])
    testtp = (mat[train:], label[train:])
    f = file(name+'.pkl', 'wb')
    pickletp = [traintp, validtp, testtp]
    cPickle.dump(pickletp, f, protocol=cPickle.HIGHEST_PROTOCOL)
    
    
'''    
datafiles = ['Lighting2', 'Lighting7', 'Coffee','Beef','ECG200','50words'
            ,'Adiac','FaceAll', 'OliveOil', 'OSULeaf','SwedishLeaf', 'CBF'
            ,'FaceFour', 'fish', 'Gun_Point', 'synthetic_control', 'Trace', 'Two_Patterns', 'wafer', 'yoga']
trains = [60, 70, 28, 30, 100, 450, 390, 560, 30, 200, 500, 30
        , 24, 175, 50, 300, 100, 1000, 1000, 300]
#size = [16, 24, 32, 40, 48]
#quantile = [8, 16, 32, 64] 

datafiles = ['Coffee']
trains = [28]
'''

#size = [256]
#quantile = [256]

#--------------------------------------

if __name__ == '__main__':
    

    s= 256
    Q = 64
    
    
    # change this part begin--------------------------
    
    mat_dir = 'cough_mat'   # change to 'noncough_mat'
    
    # change this part end ---------------------------
    
    mat_name = os.listdir(mat_dir)
    
    out_path = 'gaf_mtf_'+mat_dir
    i=0
    
    
    for i_mat in mat_name:
    
        i = i+1
        print len(mat_name),':',i ,'\t', mat_dir+'/'+i_mat
        
        
        mat_path = mat_dir + '/' + i_mat
        data_wav = sio.loadmat(mat_path)
        data_y = data_wav['y']
        #data_y = data_y[::data_y.size/300] #resample
        data_y = data_y[1000:2000] #resample
        raw = [x[0] for x in data_y]
        
        std_data = rescale(raw)
        
        paalistcos = paa(std_data,s,None) 
        
        ################ raw ###################                
        paalistcos = np.array(paalistcos)
        paalistsin = np.sqrt(1-paalistcos**2)
        
        ##datacos = np.matrix(datacos)
        ##datasin = np.matrix(datasin)            
        
        paalistcos = np.matrix(paalistcos)
        paalistsin = np.matrix(paalistsin)            
    
        paasummatrix = paalistcos.T*paalistcos-paalistsin.T*paalistsin
        paadifmatrix = paalistsin.T*paalistcos-paalistcos.T*paalistsin
        paasummatrix = np.array(paasummatrix)
        paadifmatrix = np.array(paadifmatrix)
    
        
        ############### Markov Matrix #######################
        #resample
        #std_data = paa(std_data,1000,None)
        std_data = std_data #[::10]
        
        mat, matindex, level = QMeq(std_data, Q)
        ##paamat,paamatindex = QMeq(paalist,Q)
        #paamatindex = paaMarkovMatrix(paalistcos, level)
        column = []
        paacolumn = []
        
        
        for p in range(len(std_data)):#
            for q in range(len(std_data)):
                column.append(mat[matindex[p]][matindex[(q)]])
                
        ##for p in range(s):
        ##    for q in range(s):
        ##        paacolumn.append(mat[paamatindex[p]][paamatindex[(q)]])
         
        column = np.array(column)
        ##paacolumn = np.array(paacolumn)
        columnmatrix = column.reshape(len(std_data),len(std_data))
        #image.append(columnmatrix)
        ##paaimage.append(paacolumn.reshape(s,s))
        ##matmatrix.append(paacolumn)
        
        batch = len(std_data)/s
        patch = []
        for p in range(s):
            for q in range(s):
                patch.append(np.mean(columnmatrix[p*batch:(p+1)*batch,q*batch:(q+1)*batch]))
          
        
        
        #patchimage.append(np.array(patch).reshape(s,s))
        matmatrix = []
        matmatrix.append(list(paasummatrix.flatten())+list(paadifmatrix.flatten())+patch)
        
    
        #image = np.array(image)
        paacolumn = np.array(paacolumn)
        #patchimage = np.array(patchimage)
        matmatrix = np.array(matmatrix)
        
        #print '\t',out_path+'/'+i_mat    
        #if not os.path.exists(out_path):
        #    os.mkdir(out_path)
            
        #sio.savemat(out_path+'/'+i_mat,{'data':matmatrix})
    
