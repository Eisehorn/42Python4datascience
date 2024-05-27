from load_image import image_to_grayscale
import numpy as np
import matplotlib.pyplot as plt


def ft_transpose(arr: np.array, rotation: int) -> np.array:
	print("New shape after Transpose:", arr.shape)
	height, width = arr.shape
	transposed_arr = np.zeros((width, height), int)
	if rotation == 90:
		for i in range(height):
			for j in range(width):
				transposed_arr[j, i] = arr[i, j]
	elif rotation == 180:
		for i in range(height):
			for j in range(width):
				transposed_arr[i, j] = arr[-i, -j]
	elif rotation == 270:
		for i in range(height):
			for j in range(width):
				transposed_arr[i, j] = arr[-j, -i]
	return transposed_arr


def main():
	arr = image_to_grayscale("/Users/fgiuliano/Downloads/animal.jpg")
	print(arr)
	arr = ft_transpose(arr, 270)
	print(arr)
	try:
		plt.imshow(arr, cmap='gray')
		plt.xlabel('X Axis')
		plt.ylabel('Y Axis')
		plt.title('Image with Added Axis')
		plt.show()
	except TypeError as e:
		print(e)


if __name__ == '__main__':
	main()
