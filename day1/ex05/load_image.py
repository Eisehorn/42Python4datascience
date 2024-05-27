import sys
import numpy as np
from PIL import Image


def image_to_grayscale(path: str) -> np.array:
	try:
		img = Image.open(path)
		img = img.convert("L")
		width, height = img.size
		img_array = np.array(img)
		sliced_array = img_array[100:500, -600:-200]
		arr_with_axis = sliced_array[..., np.newaxis]
		print(sliced_array.shape, "or", arr_with_axis.shape)
		return sliced_array
	except AssertionError as e:
		print(e)
		sys.exit(1)
	except IOError as e:
		print(f"IOError: {e}")
		sys.exit(1)


def ft_load(path: str) -> np.array:
	try:
		img = Image.open(path)
		width, height = img.size
		channel = img.mode
		assert channel == "RGB", 'Only RGB images are supported'
		print(f"The shape of the image is ({height}, {width}, {len(channel)})")
		return np.array(img)
	except AssertionError as e:
		print(e)
		sys.exit(1)
	except IOError as e:
		print(f"IOError: {e}")
		sys.exit(1)
