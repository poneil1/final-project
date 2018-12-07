# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:49:30 2018


"""
#Code to visulaize changes in the LV and RM models through the use of ggplot.


#Library imports
import pandas
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.integrate as spint
from plotnine import *

# Lotka-Volterra model
def Scenerios1(b,a,e,s):
    def LV(y,t0,b,a,e,s):
        H1=y[0]
        P1=y[1]
        dHdt1=(b*H1)-(a*P1*H1)
        dPdt1=(e*a*P1*H1)-(s*P1)
	return np.array([dHdt1,dPdt1])
    y0=[25,5] #Initial populations
    times=range(0,100)
    params=(b,a,e,s) #Parameters given
    modelLV=spint.odeint(func=LV,y0=y0,t=times,args=params)
    modelLVDF=pandas.DataFrame({"t":times,"H":modelLV[:,0],"P":modelLV[:,1]})
    a=ggplot(modelLVDF,aes(x="t",y="H"))+geom_line(color='black')+theme_classic()#plots
    a=a+geom_line(aes(x="t",y="P"),color='red')
    return(a)
    
# Rosenzweig-MacArthur model
def Scenerios2(b,e,s,w,d,a):
    def RM(y,t0,b,e,s,w,d,a):
        H2=y[0]
        P2=y[1]
        dHdt2=(b*H2)*(1-(a*H2))-(w*(H2/(d+H2))*P2)   
        dPdt2=(((e*w)*(H2/(d+H2)))*P2)-(s*P2)
        return np.array([dHdt2,dPdt2])
    times=range(0,100)
    y0=[500,120] #initial populations
    params=(b,e,s,w,d,a) #Parameters given
    modelRM=spint.odeint(func=RM,y0=y0,t=times,args=params)
    modelRMDF=pandas.DataFrame({"t":times,"H":modelRM[:,0],"P":modelRM[:,1]})
    b=ggplot(modelRMDF,aes(x="t",y="H"))+geom_line(color='black')+theme_classic()#plots
    b=b+geom_line(aes(x="t",y="P"),color='red')
    b=b+xlab("Time")+ylab("Population size")
    return b
#Lotka-Volterra model scenerios (b,a,e,s)
OriginalLV=Scenerios1(0.5,0.02,0.1,0.2)
print(OriginalLV)
#Changing Prey birth rate parameter 
Prey_Birth_LV=Scenerios1(1.5,0.02,0.1,0.2)
print(Prey_Birth_LV)
#Changing Attack Rate parameter
Attack_Rate_LV=Scenerios1(0.5,0.04,0.1,0.2)
print(Attack_Rate_LV)
#Changing conversion eff parameter
Conversion_eff_LV=Scenerios1(0.5,0.02,0.5,0.2)
print(Conversion_eff_LV)
#Changing Predator Rate parameter
Predator_Rate_LV=Scenerios1(0.5,0.02,0.1,1)
print(Predator_Rate_LV)

# Rosenzweig-MacArthur model scenerios (b,e,s,w,d,a)
OriginalRM=Scenerios2(.8,.07,.2,5,400,.001)
print(OriginalRM)
#Changing Prey birth rate parameter
Prey_Birth_RM=Scenerios2(1.6,.07,.2,5,400,.001)
print(Prey_Birth_RM)
#Changing Conversion eff parameter
Conversion_eff_RM=Scenerios2(.8,.14,.2,5,400,.001)
print(Conversion_eff_RM)
#Changing Death rate parameter
Predator_Death_RM=Scenerios2(.8,.07,.4,5,400,.001)
print(Predator_Death_RM)
#Changing Self limiting parameter
Self_Limiting_RM=Scenerios2(.8,.07,.2,10,400,.001)
print(Self_Limiting_RM)
#Changing Saturation effect parameter
Saturation_Effect_RM=Scenerios2(.8,.07,.2,5,800,.001)
print(Saturation_Effect_RM)
#Changing Inverse Carrying Capacity parameter
Inverse_Carrying_Cap_RM=Scenerios2(.8,.07,.2,5,400,.002)
print(Inverse_Carrying_Cap_RM)