import pandas as pd
import matplotlib.pyplot as plt

file_path = "C:/Users/Alin/Documents/GitHub/PMP-2023/Lab07/auto-mpg.csv"
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.scatter(df['mpg'], df['horsepower'], color='blue')
plt.title('Consumul unei masini pe baza cailor putere ')
plt.xlabel('Consum (mpg)')
plt.ylabel('Cai putere')
plt.subplot(2, 1, 2)
plt.hist(df['mpg'], bins=20, color='green', edgecolor='black')
plt.title('Distributia consumului ')
plt.xlabel('Consum (mpg)')
plt.ylabel('Distributia')


plt.tight_layout()

plt.show()