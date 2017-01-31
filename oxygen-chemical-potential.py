
# coding: utf-8

# In[1]:

#/usr/bin/env python

##This is a script to calculate the oxygen chemical potential
import numpy as np
import os, math
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from matplotlib import style
plt.switch_backend('agg')

# In[2]:

###Define the possible parameter
delta_u=[0,-0.15,-0.171,-0.274,-0.383,-0.495,-0.617,-0.73,-0.851,-0.975,-1.10,-1.227,-1.355,-1.486,-1.618,-1.751]
         #changes in oxygen chemical potential with respect to 0K value from experimental table, from 0 K to 1500 K
u_0=-4.25            #oxygen-rich chemical potential
u_T_p=[]           #oxygen chemical potential as a function of T and p
p=[]                 #oxygen partial pressure, from 0 to 1
kb=8.617332478e-5    #Boltzmann constant
T=np.linspace(0, 1500, 16)


# In[3]:

###Define a function to interpolate the delta_u value as a function of temperature
import sys
from scipy.interpolate import interp1d
f = interp1d(T, delta_u, kind='slinear')
ex_T=np.linspace(0, 1500, 200)
ex_u=[]
for t in ex_T:
    ex_u.append(f(t))
plt.plot(ex_T, ex_u,'o')
#plt.show()


# In[47]:

###Chemical potential
Z=[]
P=np.logspace(-10,1,200)
Temp=np.linspace(0,1500,200)
X, Y = np.meshgrid(Temp, P)   #Build two matrixs, X and Y
for p in P:
    for t in Temp:
        a=0.5*kb*t*np.log(p)
        u_T_p=u_0+f(t)+a
        Z.append(u_T_p)

Z = np.array(Z)  #transform U list into array
Z.shape = X.shape  #rebuild the Z matrix based on the shape of X matrix


# In[48]:

im = plt.pcolor(X,Y,Z,vmin=-7.8, vmax=-4.25)
axes=plt.subplot(111)
plt.yscale('log')
#plt.colorbar(im)#, orientation='horizontal')
plt.xlim([0, 1500])
#ax.xaxis.set_label_position('below')  #set the label position
#ax.yaxis.set_label_position('left')

#ax.set_xlabel(r'$\Delta\mu_{O}(eV)$',fontsize=15)
plt.xlabel('Temperature (K)',fontsize=18)
plt.ylabel('Oxygen partial pressure (atm)',fontsize=18)
#plt.text(10, 1000, r'$\Delta\mu (eV)$',fontsize=18)
cbar=plt.colorbar(im)
cbar.set_label(r'$\Delta\mu_O$(eV)',fontsize=18),#rotation=270)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()
plt.savefig('text.png',dpi=600)
# In[ ]:



