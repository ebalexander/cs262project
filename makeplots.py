# TODO: document

import numpy as np
import matplotlib.pyplot as plt
#from scipy.interpolate import interp1d

# filenames
root = '/Users/ealexander/Desktop/262/cs262project/log/'

# plot each process's score versus update
def mainplot():
    oracle = root + 'oracle'
    cent0 = root + 'central_port2000'
    cent1 = root + 'central_port2001'
    cent2 = root + 'central_port2002'
    cent3 = root + 'central_port2003'
    cent4 = root + 'central_port2004'
    #cent5 = root + 'central_port2005'

    # open files and put systime and f scores into array
    ora = np.loadtxt(oracle,skiprows=0,usecols=(0,2))
    c0 = np.loadtxt(cent0,skiprows=1,usecols=(0,2))
    c1 = np.loadtxt(cent1,skiprows=1,usecols=(0,2))
    c2 = np.loadtxt(cent2,skiprows=1,usecols=(0,2))
    c3 = np.loadtxt(cent3,skiprows=1,usecols=(0,2))
    c4 = np.loadtxt(cent4,skiprows=1,usecols=(0,2))
    #c5 = np.loadtxt(cent5,skiprows=1,usecols=(0,2))
    
    plt.scatter(ora[:,0],ora[:,1],color='k',s=5,label='oracle')
    plt.scatter(c0[:,0],c0[:,1],color='r',s=5,label='0')
    plt.scatter(c1[:,0],c1[:,1],color='g',s=5,label='1')
    plt.scatter(c2[:,0],c2[:,1],color='b',s=5,label='2')
    plt.scatter(c3[:,0],c3[:,1],color='c',s=5,label='3')
    plt.scatter(c4[:,0],c4[:,1],color='m',s=5,label='4')
    #    plt.scatter(c5[:,0],c5[:,1],color='y',s=5,label='5')
    plt.xlabel('system time')
    plt.ylabel('f score')
    plt.title('Global versus central solutions')
    plt.legend(loc='best',title='threshold')
    plt.show()

def normplot():
    oracle = root + 'oracle'
    baseport = 2100
    thresholds = [0,1,2,4,6,8,100]
    cent0 = root + 'central_score_' + str(baseport+thresholds[0])
    cent1 = root + 'central_score_' + str(baseport+thresholds[1])
    cent2 = root + 'central_score_' + str(baseport+thresholds[2])
    cent3 = root + 'central_score_' + str(baseport+thresholds[3])
    cent4 = root + 'central_score_' + str(baseport+thresholds[4])
    cent5 = root + 'central_score_' + str(baseport+thresholds[5])
    cent6 = root + 'central_score_' + str(baseport+thresholds[6])

    ora = np.loadtxt(oracle,skiprows=0,usecols=(1,2))
    c0 = np.loadtxt(cent0,skiprows=0,usecols=(1,2))
    c1 = np.loadtxt(cent1,skiprows=0,usecols=(1,2))
    c2 = np.loadtxt(cent2,skiprows=0,usecols=(1,2))
    c3 = np.loadtxt(cent3,skiprows=0,usecols=(1,2))
    c4 = np.loadtxt(cent4,skiprows=0,usecols=(1,2))
    c5 = np.loadtxt(cent5,skiprows=0,usecols=(1,2))
    c6 = np.loadtxt(cent6,skiprows=0,usecols=(1,2))
    
    plt.subplot(3,1,1)
    plt.plot(ora[:,0],ora[:,1],color='k',label='oracle')
    plt.plot(c0[:,0],c0[:,1],color='r',label=str(thresholds[0]))
    plt.plot(c1[:,0],c1[:,1],color='g',label=str(thresholds[1]))
    plt.plot(c2[:,0],c2[:,1],color='b',label=str(thresholds[2]))
    plt.plot(c3[:,0],c3[:,1],color='c',label=str(thresholds[3]))
    plt.plot(c4[:,0],c4[:,1],color='m',label=str(thresholds[4]))
    plt.plot(c5[:,0],c5[:,1],color='y',label=str(thresholds[5]))
    plt.plot(c6[:,0],c6[:,1],color='k',marker='*',label=str(thresholds[6]))
    plt.xlabel('num points')
    plt.ylabel('f score')
    plt.title('Global versus central solutions')
    plt.legend(loc='best',title='threshold')

    plt.subplot(3,1,2)
    plt.plot(ora[:,0],ora[:,1]/np.sqrt(ora[:,0]),color='k',label='oracle')
    plt.plot(c0[:,0],c0[:,1]/np.sqrt(c0[:,0]),color='r',label=str(thresholds[0]))
    plt.plot(c1[:,0],c1[:,1]/np.sqrt(c1[:,0]),color='g',label=str(thresholds[1]))
    plt.plot(c2[:,0],c2[:,1]/np.sqrt(c2[:,0]),color='b',label=str(thresholds[2]))
    plt.plot(c3[:,0],c3[:,1]/np.sqrt(c3[:,0]),color='c',label=str(thresholds[3]))
    plt.plot(c4[:,0],c4[:,1]/np.sqrt(c4[:,0]),color='m',label=str(thresholds[4]))
    plt.plot(c5[:,0],c5[:,1]/np.sqrt(c5[:,0]),color='y',label=str(thresholds[5]))
    plt.plot(c6[:,0],c6[:,1]/np.sqrt(c6[:,0]),color='k',marker='*',label=str(thresholds[6]))
    plt.xlabel('num points')
    plt.ylabel('f score, normalized by num points')
    plt.title('Global versus central solutions')
    plt.legend(loc='best',title='threshold')

    plt.subplot(3,1,3)
    plt.plot(c0[:,0],ora[:,1]/c0[:,1],color='r',label=str(thresholds[0])+',ratio')
    plt.plot(c1[:,0],ora[:,1]/c1[:,1],color='g',label=str(thresholds[1])+',ratio')
    plt.plot(c2[:,0],ora[:,1]/c2[:,1],color='b',label=str(thresholds[2])+',ratio')
    plt.plot(c3[:,0],ora[:,1]/c3[:,1],color='c',label=str(thresholds[3])+',ratio')
    plt.plot(c4[:,0],ora[:,1]/c4[:,1],color='m',label=str(thresholds[4])+',ratio')
    plt.plot(c5[:,0],ora[:,1]/c5[:,1],color='y',label=str(thresholds[5])+',ratio')
    plt.plot(c6[:,0],ora[:,1]/c6[:,1],color='k',marker='*',label=str(thresholds[6])+',ratio')
    plt.xlabel('num points')
    plt.ylabel('f score ratio')
    plt.title('Global versus central solutions')
    plt.legend(loc='best',title='threshold')
    plt.show()

normplot()