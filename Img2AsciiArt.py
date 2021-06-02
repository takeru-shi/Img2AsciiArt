import PIL.Image

def resize(img, new_width):
    width, height = img.size
    new_height = new_width * height // width
    return img.resize((new_width, new_height))

def pixel_to_ascii(img, chars):
    pixels = img.getdata() #[0:255]
    ascii_str = ""
    for pixel in pixels:
        ascii_str += chars[pixel // 25] # [n] < len(chars)
    return ascii_str

def make_ascii_img(ascii_str, new_width):
    ascii_img = ""
    for i in range(0, len(ascii_str), new_width):
        ascii_img += ascii_str[i : i + new_width] + "\n"
    return ascii_img

def main():
    img_path = "" # jpg, jpeg, png, etc.
    ascii_path = "" # txt
    chars = list("")  #	arbitrary strring

    original_img = PIL.Image.open(img_path)
    grey_img = original_img.convert("L")
    new_width = 300 # arbitrary integer
    resized_img = resize(grey_img, new_width)
    ascii_str = pixel_to_ascii(resized_img, chars)
    ascii_img = make_ascii_img(ascii_str, new_width)

    with open(ascii_path, "w") as f:
        f.write(ascii_img)

if __name__=="__main__":
    main()