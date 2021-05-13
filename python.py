import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = np.array[[1, 2, 3],[2, 3, 4]]
df = pd.dataframe(data,index = [1,2])
fig, ax = plt.subplot()
ax.plot(df)
ax.set_title('practice')
plt.show()
