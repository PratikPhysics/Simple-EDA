import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the data (scale between 0 and 1)
x_train = x_train / 255.0
x_test = x_test / 255.0

# Reshape data to include channel dimension (needed for CNNs)
x_train = x_train.reshape(-1, 28, 28, 1)  # 1 channel for grayscale
x_test = x_test.reshape(-1, 28, 28, 1)

# Build a simple CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),  # 32 filters, 3x3 kernel
    layers.MaxPooling2D((2, 2)),  # Downsample
    layers.Conv2D(64, (3, 3), activation='relu'),  # Second conv layer
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),  # Flatten to feed into dense layer
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 output classes
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")
