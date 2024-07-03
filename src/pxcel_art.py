from PIL import Image

def pixelate_image(image_path, pixel_size):
	# 画像を開く
	image = Image.open(image_path)
	
	# 画像の元のサイズを取得
	width, height = image.size
	
	# ピクセル化のための新しいサイズを計算
	width = (width // pixel_size) * pixel_size
	height = (height // pixel_size) * pixel_size
	
	# 画像をリサイズ
	image = image.resize((width//pixel_size, height//pixel_size), Image.NEAREST)
	image = image.resize((width, height), Image.NEAREST)
	

	pixels = image.load()
	width, height = image.size
	# 画像データの書き換え
	for x in range(width):
		for y in range(height):
			# image/AIcat02.pngのサンプル画像のみa(透明度)が必要
			# r, g, b, a = pixels[x, y]
			r, g, b = pixels[x, y]
			# 下四桁を0にするためにANDビット演算子を使います。0xF0=240は16進数で0b11110000です。
			pixels[x, y] = (r & 0b11110000, g & 0b11100000, b & 0b11110000)

	image.save("image/OUTcat.png")
	
	# ピクセル化された画像を返す
	return image

# 使用例
pixelated_image = pixelate_image('image/AIcat00.png', 2**4)
pixelated_image.show()

