from scipy import stats
from scipy.stats import gamma
# EX - 1

lambda_p = 20
poisson_dist = stats.poisson(mu=lambda_p)

comanda = 2 
dev_comanda = 0.5 
normal_dist = stats.norm(loc=comanda, scale=dev_comanda)

alpha = 5  
beta = 1 / alpha  
exponential_dist = stats.expon(scale=1/beta)


num_customers = poisson_dist.rvs()
print(f"Numar da clienti: {num_customers}")


order_time = normal_dist.rvs()
print(f"Timpul de plasare si plată a unei comenzi: {order_time} min")

prep_time = exponential_dist.rvs()
print(f"impul de gatit comanda: {prep_time} min")


#--------------------------2--------------------------
prob_dorita = 0.95
timpul_maxim = 0.25
nr_clienti = lambda_p

max_alpha = gamma.ppf(prob_dorita, nr_clienti, scale=timpul_maxim)

#--------------------------3--------------------------
avg_time = 1 / max_alpha

print(f"Timpul mediu de așteptare pentru a fi servit unui client este: {avg_time}")
