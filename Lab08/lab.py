import pandas as pd
import matplotlib.pyplot as plt
import arviz as az
import pymc as pm
import numpy as np
#a
df = pd.read_csv('Prices.csv')

price = df['Price']
speed = df['Speed']
hard_drive = df['HardDrive']
ram = df['Ram']
premium = df['Premium']

with pm.Model() as model:
    alpha = pm.Normal('alpha', mu=0, sigma = 10)
    beta1 = pm.Normal('beta1', mu=0, sigma = 1)
    beta2 = pm.Normal('beta2', mu=0, sigma = 1)

    eps = pm.HalfCauchy('eps', 5)
    niu = pm.Deterministic('niu', alpha + beta1 * speed + beta2 * np.log(hard_drive))
    y_pred = pm.Normal('price_pred', mu=niu, sigma=eps, observed=price)
    idata = pm.sample(2000, tune=2000, return_inferencedata=True)

az.plot_trace(idata, var_names=['alpha', 'beta1','beta2', 'eps'])
print(az.summary(idata, var_names=['alpha', 'beta1','beta2', 'eps']))
plt.show()
