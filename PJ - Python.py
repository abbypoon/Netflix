import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv(r"C:\Users\Abby\Desktop\Generation\Project\Q2.csv")

datawithoutmanager = data[data['JobTitle'] == 'Sales Representative']
print(datawithoutmanager)

# Plot a scatter chart
x = datawithoutmanager['Annual Leave Taken (hour)']
y = datawithoutmanager['Bonus']
plt.scatter(datawithoutmanager['Annual Leave Taken (hour)'],datawithoutmanager['Bonus'],marker= 's')

# Decorate
plt.xlabel('Annual Leave Taken (hour)')
plt.ylabel('Bonus')
plt.title('The relationship between annual leave taken and bonus')
plt.xlim(0, 40)
plt.grid()

# Calculate equation for trendline
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
# Add trendline to plot
plt.plot(x, p(x), color="purple")
plt.show()

# You can see that there is a negative linear relation between the points. As X increases, Y decreases.
# It means that the less hours the annual leave they took, the more the bonus they receive
# but that could be a coincidence, after all we only observed 14 Sales Representatives


