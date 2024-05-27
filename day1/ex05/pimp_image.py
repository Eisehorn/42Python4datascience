import sys

import numpy as np
from load_image import ft_load
from matplotlib import pyplot as plt
from PIL import Image


def ft_invert(array) -> np.array:
	for i in range(array.shape[0]):
		for j in range(array.shape[1]):
			array[i, j] = 255 - array[i, j]
	return array


def ft_red(array) -> np.array:
	for i in range(array.shape[0]):
		for j in range(array.shape[1]):
			red_channel = array[i, j, 0]
			array[i, j, 0] = red_channel
			array[i, j, 1] = 0
			array[i, j, 2] = 0
	return array


def ft_green(array) -> np.array:
	for i in range(array.shape[0]):
		for j in range(array.shape[1]):
			green_channel = array[i, j, 1]
			array[i, j, 0] = 0
			array[i, j, 1] = green_channel
			array[i, j, 2] = 0
	return array


def ft_blue(array) -> np.array:
	for i in range(array.shape[0]):
		for j in range(array.shape[1]):
			blue_channel = array[i, j, 2]
			array[i, j, 0] = 0
			array[i, j, 1] = 0
			array[i, j, 2] = blue_channel
	return array


def ft_grey(array) -> np.array:
	for i in range(array.shape[0]):
		for j in range(array.shape[1]):
			red_channel = array[i, j, 0]
			green_channel = array[i, j, 1]
			blue_channel = array[i, j, 2]
			gray_value = sum((red_channel // 3, green_channel // 3, blue_channel // 3))
			array[i, j] = [gray_value, gray_value, gray_value]
	return array


def main():
	try:
		img = Image.open('/Users/fgiuliano/Downloads/landscape.jpeg')
		arr = np.array(img)
		print(f'The shape of the image is {arr.shape}')
		if len(sys.argv) == 1:
			raise AssertionError('Not a valid command, insert as an argument original, invert, red, blue, green or gray')
		if sys.argv[1] == 'invert':
			arr = ft_invert(arr)
			print(arr)
			print('Inverts the color of the image')
		elif sys.argv[1] == 'red':
			arr = ft_red(arr)
			print(arr)
			print('Reduces the color of the image to reds')
		elif sys.argv[1] == 'green':
			arr = ft_green(arr)
			print(arr)
			print('Reduces the color of the image to greens')
		elif sys.argv[1] == 'blue':
			arr = ft_blue(arr)
			print(arr)
			print('Reduces the color of the image to blues')
		elif sys.argv[1] == 'gray':
			arr = ft_grey(arr)
			print(arr)
			print('Reduces the color of the image to a grayscale')
		elif sys.argv[1] == 'original':
			pass
		plt.imshow(arr)
		plt.xlabel('X Axis')
		plt.ylabel('Y Axis')
		plt.title('Image with Added Axis')
		plt.show()
	except IOError as e:
		print(e)
		sys.exit(1)
	except IndexError as e:
		print(e)
		sys.exit(1)
	except TypeError as e:
		print(e)
		sys.exit(1)
	except AssertionError as e:
		print(e)
		sys.exit(1)


if __name__ == '__main__':
	main()
