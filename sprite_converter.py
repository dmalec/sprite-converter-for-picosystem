# Copyright(c) 2021 Dan Malec
#
# MIT License (see LICENSE file for details)

from PIL import Image
import sys

try:
    file_name = sys.argv[1]
except IndexError:
    print("Usage:")
    print(f"  {sys.argv[0]} <file_name>")
    sys.exit()

image = Image.open(file_name)

pixel_width = image.size[0]
pixel_height = image.size[1]

if pixel_width % 8 != 0:
    new_pixel_width = int(pixel_width / 8) * 8
    print(f"WARNING: Width {pixel_width} is not evenly divisible by 8, "
          f"cropping to {new_pixel_width}")
    pixel_width = new_pixel_width

if pixel_height % 8 != 0:
    new_pixel_height = int(pixel_height / 8) * 8
    print(f"WARNING: Height {pixel_height} is not evenly divisible by 8, "
          f"cropping to {new_pixel_height}")
    pixel_height = new_pixel_height

print()
print("// Custom sprite sheet")
print(f"const color_t custom_sprite_sheet_data"
      f"[{pixel_width * pixel_height}] = {{")

c = 0
for row in range(pixel_height):
    for col in range(pixel_width):
        if c == 0:
            print("  ", end="")

        r, g, b, a = image.getpixel((col, row))

        scaled_r = int(float(r) / 255.0 * 15.0)
        scaled_g = int(float(g) / 255.0 * 15.0)
        scaled_b = int(float(b) / 255.0 * 15.0)
        scaled_a = int(float(a) / 255.0 * 15.0)

        gbar_pixel = (scaled_g << 12) | \
            (scaled_b << 8) | \
            (scaled_a << 4) | \
            scaled_r

        print(f"0x{gbar_pixel:04x},", end="")
        c = c + 1
        if c >= 8:
            print("")
            c = 0
        else:
            print(" ", end="")
print("};")

print(f"buffer_t CUSTOM_SPRITESHEET{{.w = {pixel_width}, .h = {pixel_height},"
      ".data = (color_t *)custom_sprite_sheet_data};")
print("buffer_t *custom_sprite_sheet = &CUSTOM_SPRITESHEET;")
print()
