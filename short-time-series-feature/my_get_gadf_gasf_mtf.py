# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 20:20:45 2016

@author: cs-wanghh
"""

import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable
import cPickle

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
            plt.ioff();fig= plt.figure();plt.suptitle(datafile+'_'+str(label[p]));ax1 = plt.subplot(121);plt.imshow(image[p]);divider = make_axes_locatable(ax1);cax = divider.append_axes("right", size="5%", pad=0.1);plt.colorbar(cax = cax);ax2 = plt.subplot(122);plt.imshow(paaimage[p]);divider = make_axes_locatable(ax2);cax = divider.append_axes("right", size="5%", pad=0.1);plt.colorbar(cax = cax);
            pdf.savefig(fig)
            plt.close(fig)
    pdf.close

def pickle3data(mat, label, train, name):
    print '..pickling data:',name
    traintp = (mat[:train], label[:train])
    validtp = (mat[:train], label[:train])
    testtp = (mat[train:], label[train:])
    f = file(name+'.pkl', 'wb')
    pickletp = [traintp, validtp, testtp]
    cPickle.dump(pickletp, f, protocol=cPickle.HIGHEST_PROTOCOL)
    
datafiles = ['Lighting2', 'Lighting7', 'Coffee','Beef','ECG200','50words'
            ,'Adiac','FaceAll', 'OliveOil', 'OSULeaf','SwedishLeaf', 'CBF'
            ,'FaceFour', 'FISH', 'Gun_Point', 'synthetic_control', 'Trace', 'Two_Patterns', 'wafer', 'yoga']#'synthetic_control', 
datafiles = ['Lighting2', 'Lighting7', 'Coffee','Beef','ECG200','50words'
            ,'Adiac','FaceAll', 'OliveOil', 'OSULeaf','SwedishLeaf', 'CBF'
            ,'FaceFour', 'FISH', 'Gun_Point',  'Trace', 'Two_Patterns', 'wafer', 'yoga']

trains = [60, 70, 28, 30, 100, 450, 390, 560, 30, 200, 500, 30
        , 24, 175, 50, 300, 100, 1000, 1000, 300]
trains = [61, 73, 28, 30, 100, 455, 391, 1690, 30, 242, 626, 900
        , 88, 175, 150,  100, 4000, 6174, 3000]#test
#size = [16, 24, 32, 40, 48]
#quantile = [8, 16, 32, 64] 

#datafiles = ['Adiac']
#trains = [28]

size = [64]
quantile = [64]

for datafile, train in zip(datafiles,trains):
    print '#-----------------------------'
    fn = './UCRdata/'+datafile+'/' +datafile+'_TEST' # change "_TEST" to "_TRAIN"
    for s in size:  
        for Q in quantile:
            print 'read file', datafile, 'size',s
            with open(fn,'r') as f:
                raw=f.readlines()
            raw = [map(float, each.strip().split(',')) for each in raw]
            length = len(raw[0])-1
            
            print 'format data'
            label = []
            image = []
            paaimage = []
            patchimage = []
            matmatrix = []
            i=0
            for each in raw:
                label.append(each[0])
                #std_data = rescaleminus(each[1:])
                std_data = rescale(each[1:])
                #std_data = each[1:]
                #std_data = standardize(each[1:])
                #std_data = rescaleminus(std_data)
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
                #matrix = np.array(datacos.T*datacos-datasin.T*datasin)
                ##matrix = np.array(datasin.T*datacos - datacos.T*datasin)
                ##image.append(matrix)
                #paasumimage.append(np.array(paasummatrix))
                #paadifimage.append(np.array(paadifmatrix))
                
                ############### Markov Matrix #######################
                mat, matindex, level = QMeq(std_data, Q)
                ##paamat,paamatindex = QMeq(paalist,Q)
                #paamatindex = paaMarkovMatrix(paalistcos, level)
                column = []
                paacolumn = []
                for p in range(len(std_data)):
                    for q in range(len(std_data)):
                        column.append(mat[matindex[p]][matindex[(q)]])
                        
                ##for p in range(s):
                ##    for q in range(s):
                ##        paacolumn.append(mat[paamatindex[p]][paamatindex[(q)]])
                        
                column = np.array(column)
                ##paacolumn = np.array(paacolumn)
                columnmatrix = column.reshape(len(std_data),len(std_data))
                image.append(columnmatrix)
                ##paaimage.append(paacolumn.reshape(s,s))
                ##matmatrix.append(paacolumn)
                
                batch = len(std_data)/s
                patch = []
                for p in range(s):
                    for q in range(s):
                        patch.append(np.mean(columnmatrix[p*batch:(p+1)*batch,q*batch:(q+1)*batch]))
                i = i+1
                print i       
                
                
                patchimage.append(np.array(patch).reshape(s,s))
                matmatrix.append(list(paasummatrix.flatten())+list(paadifmatrix.flatten())+patch)
                
                
            label = np.array(label)
            image = np.array(image)
            paacolumn = np.array(paacolumn)
            patchimage = np.array(patchimage)
            matmatrix = np.array(matmatrix)

    sio.savemat('mat3d/'+datafile+'_test.mat',{'data':matmatrix})
