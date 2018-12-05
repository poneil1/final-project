# Lotka-Volterra model

#import packages
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

#define function
def LV(y,t0,b,a,e,s):
	H=y[0]
	P=y[1]
	dHdt=(b*H)-(a*P*H)
	dPdt=(e*a*P*H)-(s*P)
	return [dHdt,dPdt]

#Enter original parameters
y0=[25,5]
times=range(0,100)
params=(0.5,0.02,0.1,0.2)

#run and plot model
modelLV=spint.odeint(func=LV,y0=y0,t=times,args=params)
modelLVDF=pandas.DataFrame({"t":times,"H":modelLV[:,0],"P":modelLV[:,1]})
ggplot(modelLVDF,aes(x="t",y="H"))+geom_line()+geom_line(modelLVDF,aes(x="t",y="P"),color='red')+theme_classic()+ylab("Population size")+xlab("time")

#we changed parameters manually, one by one
#here's an example of changing one parameter
#and running the model

params=(1.0,0.02,0.1,0.2)
modelLV=spint.odeint(func=LV,y0=y0,t=times,args=params)
modelLVDF=pandas.DataFrame({"t":times,"H":modelLV[:,0],"P":modelLV[:,1]})
ggplot(modelLVDF,aes(x="t",y="H"))+geom_line()+geom_line(modelLVDF,aes(x="t",y="P"),color='red')+theme_classic()+ylab("Population size")+xlab("time")



# Rosenzweig-MacArthur model

#import packages
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

#define function
def RM(y,t0,b,e,s,w,d,a):
	H=y[0]
	P=y[1]
	dHdt=(b*H)*(1-(a*H))-(w*(H/(d+H))*P)
	dPdt=(e*w)*(H/(d+H))*P-(s*P)
	return [dHdt,dPdt]

#enter original parameters
times=range(0,100)
y0=[500,120]
params=(0.8,0.07,0.2,5,400,0.001)

#run and plot model
modelRM=spint.odeint(func=RM,y0=y0,t=times,args=params)
modelRMDF=pandas.DataFrame({"t":times,"H":modelRM[:,0],"P":modelRM[:,1]})
ggplot(modelRMDF,aes(x="t",y="H"))+geom_line()+geom_line(modelRMDF,aes(x="t",y="P"),color='red')+theme_classic()+ylab("Population size")+xlab("time")

#example of changing parameter
#and running the model

params=(0.8,0.07,0.2,5,400,0.001)
modelRM=spint.odeint(func=RM,y0=y0,t=times,args=params)
modelRMDF=pandas.DataFrame({"t":times,"H":modelRM[:,0],"P":modelRM[:,1]})
ggplot(modelRMDF,aes(x="t",y="H"))+geom_line()+geom_line(modelRMDF,aes(x="t",y="P"),color='red')+theme_classic()+ylab("Population size")+xlab("time")
 
