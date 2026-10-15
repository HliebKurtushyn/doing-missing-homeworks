import numpy as np
import pandas as pd
import plotly.graph_objects as go

# ==========================================
# Завдання 1: 3D Scatter Plot
# ==========================================

np.random.seed(42)

df = pd.DataFrame({
    "Feature1": np.random.randn(150),
    "Feature2": np.random.randn(150),
    "Feature3": np.random.randn(150),
    "Category": np.random.choice(["A", "B", "C"], 150)
})

colors = {"A": "red", "B": "green", "C": "blue"}

fig1 = go.Figure()

for category in ["A", "B", "C"]:
    data = df[df["Category"] == category]

    fig1.add_trace(go.Scatter3d(
        x=data["Feature1"],
        y=data["Feature2"],
        z=data["Feature3"],
        mode="markers",
        marker=dict(size=5, color=colors[category]),
        name=category
    ))

fig1.update_layout(
    title="3D Scatter Plot",
    scene=dict(
        xaxis_title="Feature1",
        yaxis_title="Feature2",
        zaxis_title="Feature3"
    )
)

fig1.show()


# ==========================================
# Завдання 2: 3D Histogram
# ==========================================

x = np.random.randn(1000)
y = np.random.randn(1000)
z = np.random.randn(1000)

fig2 = go.Figure(data=[
    go.Histogram3d(
        x=x,
        y=y,
        z=z,
        colorscale="Blues"
    )
])

fig2.update_layout(
    title="3D Histogram",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z"
    )
)

fig2.show()


# ==========================================
# Завдання 3: 3D Scatter Plot
# ==========================================

df3 = pd.DataFrame({
    "Feature1": np.random.randn(150),
    "Feature2": np.random.randn(150),
    "Feature3": np.random.randn(150),
    "Category": np.random.choice(["A", "B", "C"], 150)
})

colors = {"A": "orange", "B": "purple", "C": "cyan"}

fig3 = go.Figure()

for category in ["A", "B", "C"]:
    data = df3[df3["Category"] == category]

    fig3.add_trace(go.Scatter3d(
        x=data["Feature1"],
        y=data["Feature2"],
        z=data["Feature3"],
        mode="markers",
        marker=dict(size=5, color=colors[category]),
        name=category
    ))

fig3.update_layout(
    title="3D Scatter Plot by Category",
    scene=dict(
        xaxis_title="Feature1",
        yaxis_title="Feature2",
        zaxis_title="Feature3"
    )
)

fig3.show()