import numpy as np
import matplotlib.pyplot as plt

# 1. Create list of epochs (1 to 10)
epochs = list(range(1, 11))

# 2. Generate synthetic training loss values using NumPy
np.random.seed(42)
loss = np.linspace(1.0, 0.2, 10) + np.random.normal(0, 0.05, 10)

# 3. Line Plot: Loss vs Epoch
plt.figure(figsize=(8,5))
plt.plot(epochs, loss, marker='o', linestyle='-', color='blue')
plt.title("Training Loss vs Epoch")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# 4. Scatter Plot: Epoch vs Loss
plt.figure(figsize=(8,5))
plt.scatter(epochs, loss, color='orange')
plt.title("Epoch vs Loss (Scatter Plot)")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# 5. Bar Chart: Model Accuracy Comparison
models = ['Model A', 'Model B', 'Model C']
accuracy = [0.85, 0.90, 0.88]

plt.figure(figsize=(8,5))
plt.bar(models, accuracy, color=['blue','green','red'])
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.ylim(0,1)
plt.grid(axis='y')
plt.show()