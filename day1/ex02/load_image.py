import sys
import numpy as np
from PIL import Image


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
