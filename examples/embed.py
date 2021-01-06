# A simple pre-computed UMAP example.

# %%
import json
import pandas as pd
import itertools
import numpy as np

from EleMD import EleMD
from tqdm import tqdm

import umap

import plotly.graph_objs as go
import plotly.offline as py

# %%
# Load the data

filename = "examples/data/matbench_expt_gap.json"
# filename = "data/matbench_expt_gap.json"

with open(filename, 'rb') as f:
    dataframe_data = json.load(f)

df = pd.DataFrame(**dataframe_data)
df = df.sample(frac=1).reset_index(drop=True)

# %%
# Create the distance matrix
# NOTE this will take around 30-40 minutes to do full data set

n = 1000

x = df["composition"][:n].values

D = np.zeros((n, n))

mod_petti = EleMD()

# TODO allow this to parallelise?
iterator = itertools.combinations(range(n), 2)
for i, j in tqdm(iterator):
    D[i, j] = mod_petti.elemd(x[i], x[j])

D = D + D.T

# %%
# UMAP with precomputed distance matrix

emb = umap.UMAP(
    n_neighbors=10,
    min_dist=0.0,
    n_components=3,
    metric="precomputed"
)
u = emb.fit_transform(D)

# %%
# Plot using plotly

inc_js = 'cdn'

trace_list = []

trace = go.Scatter3d(
    x=u[:, 0],
    y=u[:, 1],
    z=u[:, 2],
    mode='markers',
    text=x,
    hoverinfo='text',
)

trace_list.append(trace)

layout = go.Layout(
    title=go.layout.Title(
            text='UMAP embedding based on EleMD',
            xref='paper',
            x=0.5,),
    scene=dict(
        xaxis=dict(title='Dim 1'),
        yaxis=dict(title='Dim 2'),
        zaxis=dict(title='Dim 3'),
    ),
    hovermode='closest',
)


fig = go.Figure(data=trace_list, layout=layout)
py.plot(fig, filename='examples/plotly/embed.html', include_plotlyjs=inc_js,)

# %%