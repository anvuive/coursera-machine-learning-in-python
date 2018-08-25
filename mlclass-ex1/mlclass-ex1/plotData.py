import matplotlib.pyplot as plt
import numpy as np

def plotData(x, y):
    # PLOTDATA Plots the data points x and y into a new figure
    #   PLOTDATA(x,y) plots the data points and gives the figure axes labels of
    #   population and profit.

    # ====================== YOUR CODE HERE ======================
    # Instructions: Plot the training data into a figure using the
    #               "figure" and "plot" commands. Set the axes labels using
    #               the "xlabel" and "ylabel" commands. Assume the
    #               population and revenue data have been passed in
    #               as the x and y arguments of this function.

    # fig = plt.figure() # open a new figure window
    # ============================================================

    X, y = np.loadtxt ("ex1data1.txt",delimiter = ",", unpack = True)
    fig = plt.figure ()
    ax = fig.add_subplot (111)
    ax.scatter (X, y, color = "r", marker = "+")
    plt.title ("Population and Profit")
    plt.xlabel ("Population")
    plt.ylabel ("Profit")
    plt.savefig ("plotdata.png")