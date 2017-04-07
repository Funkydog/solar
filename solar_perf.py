#//****** Fill Factor and Open-Circuit Voltage *********//

#//The fill factor FF is defined as:

#//FF=(Jmp*Vmp)/(Jsc*Voc) //(1)

#// Jmp //current density at maximum power point
#// Vmp //voltage at maximum power point
#// Jsc //short-circuit current density
#// Voc //open-circuit voltage

#//default values
Jph=35 #//mA/cm2
J0=1.95e-10 #//mA/cm2
T=int(input('La température par défault est de 300 K\nVeuillez saisire une température : ')) #//K
n=1
V=np.linspace(0,1,100) #//V

alpha=cst.q/(n*cst.k*T)
J=Jph-J0*(np.exp(alpha*V)-1); #//(3)
plt.plot(J,V)
plt.show()