import matplotlib.pyplot as plt
import numpy as np

def view_images(dataset, class_names):
	plt.figure(figsize=(15, 10))
	for images, labels in dataset.take(1):
		for i in range(12):
			plt.subplot(3, 4, i + 1)
			plt.imshow(images[i].numpy().astype('uint8'))
			plt.title(class_names[labels[i]])
			plt.axis('off')
			