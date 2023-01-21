import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo

#Data observer frame
data = pd.read_csv('https://raw.githubusercontent.com/kmshariat/AGNMass/main/data/3c273.csv')
wave_obs = np.array(data.spectral_axis) #[Angstorm]
flux_den_obs = np.array(data.intensity) #[erg/cm^2/s/A]

#constants
z = 0.15834
d = 762.3 #Mpc
d = 762.3* 3.08567758e24 #cm

#Data Source frame
wave_src = wave_obs/(1+z)
flux_den_src = flux_den_obs*(1+z)
lum_src = flux_den_src*4*np.pi*d**2*wave_src

#Fitting the graph to a range to detect the H [II] and O [III] line
X = wave_src[360:480] #get the slicing index using trial&error
Y = lum_src[360:480] #get the slicing index using trial&error

#Plotting the spectra
plt.plot(X,Y,marker="+")
plt.grid()
plt.xticks(np.linspace(4700,5150, 26), rotation = 90)
plt.show()
