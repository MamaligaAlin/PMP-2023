from scipy import stats


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


