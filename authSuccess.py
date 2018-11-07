# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 21:23:19 2018

@author: Lorne

Created with Spyder using Anaconda3

Copyright Lorne N. Hanson
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt


def authSuccess():
 
    with open(input('Output File Location: '), 'wU', newline = '') as outfile:  # open the results file
        writer = csv.writer(outfile)                                # instantiate the csv writer
        fieldnames = ['Time','Source User','Destination User','Source Computer',    # define field names
                      'Destination Computer','Authentication Type','Logon Type',
                      'Authentication Orientation','Logon Success']
        writer.writerow(fieldnames)                     # write header row
        with open(input('Input File Location :'), 'rU') as inputfile:                 # open the input file
            reader = csv.reader(inputfile)              # read the input file
           
            for row in reader:                  # for each row in the csv file

                if row[8] != 'Success':         # if the logon is unsuccessful
                    logon_success = 0           # set binary value
                else:
                    logon_success = 1                # set binary value to true

                writer.writerow([row[0],row[1],row[2],   # write the row to the ouput file
                                row[3],row[4],
                                row[5],row[6],
                                row[7],logon_success])
    inputfile.close()
    outfile.close()

    reader = pd.read_csv("D:/authbin.csv", encoding = "latin-1") # read the file

    mcounts = reader['Logon Success'].value_counts() # count success/failures
    
    mcounts.plot.bar()                          # plot the counts
    plt.show()                                  # show the chart
    
    
if __name__ == '__main__':
    authSuccess()

    