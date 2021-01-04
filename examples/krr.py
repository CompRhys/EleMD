# A simple pre-computed KRR example.
# NOTE this does not appear to be a good choice of kernel

# %%
import json
import pandas as pd
import itertools
import numpy as np

from EleMD import EleMD
from tqdm import tqdm
from sklearn.kernel_ridge import KernelRidge


# %%
# Load the data

filename = "data/matbench_expt_gap.json"

with open(filename, 'rb') as f:
    dataframe_data = json.load(f)

df = pd.DataFrame(**dataframe_data)
df = df.sample(frac=1).reset_index(drop=True)

# %%
# Eval train distances

n = 1000

x = df["composition"][:n].values
y = df["gap expt"][:n].values

K = np.zeros((n, n))

mod_petti = EleMD()

iterator = itertools.combinations(range(n), 2)
for i, j in tqdm(iterator):
    K[i, j] = mod_petti.elemd(x[i], x[j])

K = K + K.T

# %%
# Eval test distances

m = 200

x_test = df["composition"][n:n+m].values
y_test = df["gap expt"][n:n+m].values

K_test = np.zeros((m, n))

iterator = itertools.product(range(m), range(n))
for i, j in tqdm(iterator):
    K_test[i, j] = mod_petti.elemd(x[i], x[j])

# %%
# fit KRR
krr = KernelRidge(kernel="precomputed")
lam = 2e-4


def W(K, lam=lam):
    # return np.exp(-K**2/l)
    return lam/(K**2+lam)


krr.fit(W(K), y)

tr_y = krr.predict(W(K))
te_y = krr.predict(W(K_test))

print(f"Train MAE: {np.mean(np.abs(tr_y - y)):.3f}")
print(f"Test MAE: {np.mean(np.abs(te_y - y_test)):.3f}")

print(f"Train RMSE: {np.sqrt(np.mean((tr_y - y)**2)):.3f}")
print(f"Test RMSE: {np.sqrt(np.mean((te_y - y_test)**2)):.3f}")

# %%
