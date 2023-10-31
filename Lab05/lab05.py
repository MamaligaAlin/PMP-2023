import pymc3 as pm
import numpy as np
import arviz as az
import matplotlib.pyplot as plt
import theano.tensor as tt


if __name__ == "__main__":
   data = np.genfromtxt('C:/Users/Alin/Desktop/PMP/Lab05/traffic.csv', delimiter=',', skip_header=1, usecols=1)


   ''' La care minute se schimba instensitatea traficului de masini '''
   change_points = [180,240,720,900]
   num_intervals = len(change_points) + 1

   with pm.Model() as traffic_model:
      
      lambdas = pm.Uniform('lambdas', lower=0, upper=10, shape=num_intervals)
      poisson_distributions = pm.Poisson('poisson_distributions', mu=lambdas, shape=num_intervals)

      for i in range(1, num_intervals):
        pm.Potential('lambda_change_{}'.format(i), tt.switch(i < 2, tt.gt(lambdas[i] - lambdas[i - 1], 0), tt.lt(lambdas[i] - lambdas[i - 1], 0)))

      traffic_observed = pm.Poisson('traffic_observed', mu=poisson_distributions, observed=data)

   with traffic_model:
      trace = pm.sample(2000, tune=1000, cores=2)

   az.plot.trace(trace)
   plt.show()

   az.summary(trace)
