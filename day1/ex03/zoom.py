import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt
from load_image import image_to_grayscale


def zoom(arr: np.array):
	try:
		plt.imshow(arr, cmap='gray')
		plt.xlabel('X Axis')
		plt.ylabel('Y Axis')
		plt.title('Image with Added Axis')
		plt.show()
	except TypeError as e:
		print(e)


def main():
	arr = ft_load("/Users/fgiuliano/Downloads/animal.jpg")
	print(arr)
	arr = image_to_grayscale("/Users/fgiuliano/Downloads/animal.jpg")
	print(arr)
	zoom(arr)


if __name__ == '__main__':
	main()
