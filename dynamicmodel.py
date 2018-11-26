## FIRST MODEL WORKS
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

def ddSim(y,t0,b,a,e,s):
	H=y[0]
	P=y[1]
	dHdt=(b*H)-(a*P*H)
	dPdt=(e*a*P*H)-(s*P)
	return [dHdt,dPdt]
y0=[25,5]
times=range(0,100)
params=(0.5,0.02,0.1,0.2)
model=spint.odeint(func=ddSim,y0=y0,t=times,args=params)
modelDF=pandas.DataFrame({"t":times,"H":model[:,0],"P":model[:,1]})
ggplot(modelDF,aes(x="t",y="H"))+geom_line()+geom_line(modelDF,aes(x="t",y="P"),color='red')+theme_classic()
