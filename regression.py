import numpy as np
from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt

import tap_access

data = tap_access.get_planetary_data("select pl_masse,pl_orbper,st_mass,st_rad from ps where default_flag = 1 and pl_controv_flag = 0 order by ra,dec desc")
data = data.dropna(axis=0, how="any")
x = data[data.columns[1:]].values.tolist()
y = data[data.columns[0]].values.tolist()

reg = linear_model.RidgeCV(alphas=np.logspace(-6, 6, 13))
reg.fit(x, y)
print(reg.alpha_)
print(reg.coef_)
print(reg.predict([[11.5, 0.455, 0.46]]))

labels = ("Orbital Period", "Stellar Mass", "Stellar Radius (Suns)")

for i in range(0,3):
    plt.xlabel(labels[i])
    plt.ylabel("Planet Mass (Earths)")
    plt.plot([row[i] for row in x], y, ".")
    plt.show()