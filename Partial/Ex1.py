import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
import arviz as az


primul = 0
al_doilea =0
for i in range(20000):

  m = 0
  n = 0
  P0 = np.random.uniform(0,1,1)
  
  if P0 >= 0.33333:
    n = 1
  else:
    n = 0

  print(n)

  P1 = np.random.randint(0,2,n+1)
  x = len(P1)
  for i in range(0,x):
    if P1[i]==1:
      m=m+1
  
  if n>=m :
    primul = primul+1
  else:
    al_doilea = al_doilea+1


print(primul)
print(al_doilea)
if primul > al_doilea:
  print("Jucatorul P0 are mai multe sanse")
elif primul == al_doilea:
  print("Au sanse egale")
else:
  print("Jucatorul P1 are sanse mai mari")


    
#----------2)  
aruncare_moneda = BayesianNetwork([('P0 arunca', 'stema'), ('P0 arunca', 'pajura'), ('stema', 'P1 arunca de 2 ori'),
('pajura', 'P1 arunca odata'), ('L','A'),('S','A')])
pos = nx.circular_layout(aruncare_moneda)
nx.draw(aruncare_moneda, with_labels=True, pos=pos, alpha=0.5, node_size=3500)
plt.show()
   

 CPD_P0 = TabularCPD(variable='P0 arunca', variable_card=2, values=[[0.3], [0.7]]) # probabilitatea ca P0 arunca stema sau pajura
 CPD_P1 = TabularCPD(variable='P1 arunca', variable_card=2,values=[[0.5, 0.5],[0.25, 0.25,0.25,0.25],],evidence=['P0 a aruncat '],evidence_card=[2]) # probabilitatea sa cada ss,sp,ps,pp care depinde de ce a picat la P0

model.add_cpds(CPD_P0,CPD_P1)



