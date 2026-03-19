import pandas as pd
import numpy as np
import plotly.express as px

# 1. Create dataset
epochs = list(range(1, 11))

# Generate synthetic training loss (decreasing trend)
np.random.seed(42)
loss = np.linspace(1.0, 0.2, 10) + np.random.normal(0, 0.05, 10)

# 2. Create DataFrame
df = pd.DataFrame({
    "Epoch": epochs,
    "Loss": loss
})

# 3. Create interactive line chart
fig = px.line(
    df,
    x="Epoch",
    y="Loss",
    title="Training Loss Over Epochs",
    markers=True
)

# 4. Add annotation (where loss stabilizes)
fig.add_annotation(
    x=8,
    y=df["Loss"][7],
    text="Loss Stabilizing",
    showarrow=True,
    arrowhead=2
)

# 5. Update axis labels
fig.update_layout(
    xaxis_title="Epoch",
    yaxis_title="Training Loss"
)

# 6. Show plot
fig.show()