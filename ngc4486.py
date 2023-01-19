#Necessary Modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spo

#Data Fetching
data = pd.read_csv('https://raw.githubusercontent.com/kmshariat/BHMass/main/data/ngc4486.csv')

#Observed Data
wave_obs = np.array(data.spectral_axis)
intensity_obs = np.array(data.intensity)

#constants
z = 0.00428 #from http://ned.ipac.caltech.edu/
d = 18.5 #Mpc #from https://astro.ucla.edu/~wright/CosmoCalc.html
d = 18.5*3.086e+24

#Source Data
wave_src = wave_obs/(1+z)
intensity_src = intensity_obs*(1+z)
lum_src = intensity_src*wave_src*4*np.pi*d**2

#Spectrum
#plt.plot(wave_src,lum_src)
#plt.show()

#Determining Full Width at Half-Max
X = wave_src[990:1090]
Y = lum_src[990:1090]

plt.plot(X,Y)
plt.show()
#more lines left but lets take a break
