import numpy as np
import pymc3 as pm
import arviz as az

if __name__ == "__main__":

   def posterior(Y, thet):
      with pm.Model() as model:
         n = pm.Poisson('n', 10)
            
         y = pm.Binomial('y', n=n, p=thet, observed=Y)
         trace = pm.sample(2000, tune=1000, cores=2)
         
         return trace


   traces = []
   Y = [0, 5, 10]
   thet = [0.2, 0.5]
   combinations = np.array(np.meshgrid(Y, thet)).T.reshape(-1, 2)

   print(combinations)
   print(len(combinations))
       
   for i in range(len(combinations)):
       a,b = combinations[i]
       trace = posterior(a, b)
       traces.append(trace)
       print(a,b)


   az.plot_posterior(traces)