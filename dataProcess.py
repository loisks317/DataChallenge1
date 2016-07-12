# dataProcess.py
#
#
import numpy as np
import glob
import matplotlib.pyplot as plt

data=np.genfromtxt(glob.glob('cancerData.txt')[0], delimiter=',')
#
# column 11 is what tells us if cancer is present or not
#
dataSwap=np.swapaxes(data, 1, 0)
cancerColumn=dataSwap[-1]
iYesCancer=np.where(cancerColumn==4)[0]
iNoCancer=np.where(cancerColumn==2)[0]
#
# loop over rest of parameters and plot regression and correlation coefficients
#
ParamNames=['','Clump Thickness', 'Uniformity of Cell Size',
            'Uniformity of Cell Shape', 'Marginal Adhesion',
            'Single Epitheilial Cell Size', 'Bare Nuclei',
            'Bland Chromatin', 'Normal Nucleoli', 'Mitoses']
for ii in range(1,9):
    paramDataCancer=dataSwap[ii][iYesCancer]
    paramDataNoCancer=dataSwap[ii][iNoCancer]
    #
    # print out number of points
    print("Number of Points with Cancer: " + str(len(paramDataCancer)))
    print("Number of Points with No Cancer: " + str(len(paramDataNoCancer)))
    #
    # make scatter plot of each and calculate correlation coefficients
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.boxplot([paramDataCancer, paramDataNoCancer])
    #ax.boxplot(paramDataNoCancer)
    ax.set_ylim(0,12)
    ax.set_xticks([0,1], ['Cancer', 'No Cancer'])
    fig.savefig(ParamNames[ii]+'.png')
    #
    # print out a correlation coefficient
    cancerMedian=np.nanmedian(paramDataCancer)
    noCancerMedian=np.nanmedian(paramDataNoCancer)
    print(len(paramDataCancer))
    print(len(paramDataNoCancer))
    difference=cancerMedian-noCancerMedian
    print('Param is: '+str(ParamNames[ii]))
    print('The difference between Cancer and No Cancer is: ' + str(difference))
    print('The stddev for Cancer is: ' + str(np.nanstd(paramDataCancer)))
    print('The stddev for No Cancer is: ' + str(np.nanstd(paramDataNoCancer)))

    #
    # now determine correlation coefficient between two parameters
    # with cancer vs without
    #
    # remove rows with nans
    aa=np.where(np.isnan(dataSwap[6])==True)[0]
    
    

#
# T-tests in Python
confPar={}
import scipy.stats
for ii in range(1,9):
    ttest=scipy.stats.ttest_ind(dataSwap[ii][iYesCancer], dataSwap[ii][iNoCancer])
    print(ttest)
    if ttest[1] < 0.01:
        print("We can reject the null for "+ str(ParamNames[ii]) + ' at the 1% level')
        
        lboundCancer=np.nanmedian(scipy.stats.poisson.ppf([0.025, 0.95],
                                                         dataSwap[ii][iYesCancer][:,None])[0])
        uboundCancer=np.nanmedian(scipy.stats.poisson.ppf([0.05, 0.95],
                                                         dataSwap[ii][iYesCancer][:,None])[1])
        lboundNoCancer=np.nanmedian(scipy.stats.poisson.ppf([0.05, 0.95],
                                                         dataSwap[ii][iNoCancer][:,None])[0])
        uboundNoCancer=np.nanmedian(scipy.stats.poisson.ppf([0.05, 0.95],
                                                         dataSwap[ii][iNoCancer][:,None])[1])
        print("90 Percent Confidence Interval for Cancer: " + str(lboundCancer) +
              ' to ' +str(uboundCancer))
        print("90 Percent Confidence Interval for No Cancer: " + str(lboundNoCancer) + ' to ' +
              str(uboundCancer))
    
    
for ii in range(1,9):
    for jj in range(1,9):
       
        param1DataCancer=dataSwap[ii][iYesCancer]
        param1DataNoCancer=dataSwap[ii][iNoCancer]
        param2DataCancer=dataSwap[jj][iYesCancer]
        param2DataNoCancer=dataSwap[jj][iNoCancer]


        if ii == 6:
           # this is the nan set
           param2DataCancer=param2DataCancer[~np.isnan(param1DataCancer)]
           param1DataCancer=param1DataCancer[~np.isnan(param1DataCancer)]
           param2DataNoCancer=param2DataNoCancer[~np.isnan(param1DataNoCancer)]
           param1DataNoCancer=param1DataNoCancer[~np.isnan(param1DataNoCancer)]
        if jj == 6:
           # this is the nan set
           
           param1DataCancer=param1DataCancer[~np.isnan(param2DataCancer)]
           param2DataCancer=param2DataCancer[~np.isnan(param2DataCancer)]
           param1DataNoCancer=param1DataNoCancer[~np.isnan(param2DataNoCancer)]
           param2DataNoCancer=param2DataNoCancer[~np.isnan(param2DataNoCancer)]
          
        
        
        print('Cancer Correlation between ' + ParamNames[ii] +' and ' +
              ParamNames[jj] + ' is ' + str(np.corrcoef(param1DataCancer,
                                                       param2DataCancer)))
        print('Non Cancer Correlation between ' + ParamNames[ii]+' and ' +
              ParamNames[jj] + ' is ' + str(np.corrcoef(param1DataNoCancer,
                                                       param2DataNoCancer)))
        
        
