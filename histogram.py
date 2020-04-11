from random import randint

"""
    custom addition
"""
import matplotlib.pyplot as plt
import numpy as np
from math import *

def compute_histogram_bins(data=[], bins=[]):
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted number that represents your histogram
              bin thresdholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins. 
        You are not allowed to use 
    """
    B=[]
    bin_width=10;
    bins.append(bins[len(bins)-1]+bin_width);
    for j in range(len(bins)-2):
        B.append(str(bins[j])+'-'+str(bins[j+1]))
    B.append(str(bins[j+1])+'+')
    
    data= [np.histogram(data,bins)[0][i] for i in range(len(bins)-1)];
 
    return [data,B];
    

def plot_histogram(bins_count):
    """
        Quesion 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommand using 
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(bins_count[1],bins_count[0])
    ax.set_title("Distribution of something");
    ax.set_xlabel('some metrics bins')
    ax.set_ylabel('count')
    plt.show();

if __name__ == "__main__":
    
    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
