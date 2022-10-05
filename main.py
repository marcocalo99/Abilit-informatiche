import matplotlib.pyplot as plt
import math
import numpy as np
import scipy
from scipy.stats import poisson
import statistics

giorni=[]
contagi=[]
for line in open('datiitalia.txt', 'r'):
    riga = [i for i in line.split()]
    giorni.append(i+36)
    contagi.append(int(riga[0])
                   
                   
                   
plt.title("Italy's datas 31 March 2020 - 31 July 2020 ")
plt.xlabel('Day')
plt.ylabel('Total positives')
plt.plot(x, y, marker = 'o', c = 'b')
  
plt.show()
