import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("Flipkart_mobiles_data.csv")
P = df.Price_in_Rupees
B = df.Battery_details

plt.plot(B, color='blue')
plt.plot(P, color='g')

plt.title("Flipkart_Mobiles_Data(Rossum)")
plt.xlabel("Price_in_Rupees(X)")
plt.ylabel("Battery_details(Y)")
plt.show()
