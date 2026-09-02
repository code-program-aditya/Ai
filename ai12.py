import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])
model = Sequential([
    Dense(2, input_shape=(2,), activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x, y, epochs=500, verbose=0)

predictions = model.predict(x, verbose=0)
print("XOR Predictions:")
for input, predictions, actual in zip(x.astype(int), predictions, y.astype(int)):
    predictions_class = int(predictions[0] >= 0.5)
    print(f"input: {input.tolist()}"
          f"Probability: {predictions[0]:.4f}"
          f"Predicted: {predictions_class}"
          f"Actual: {actual[0]}"
          )