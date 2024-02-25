import random
import string
from PIL import Image
import os

def setip(request):
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return(ip)

def random_string(length):
    # Define the characters to choose from
    characters = string.digits

    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string

def resize_image(image,nwidth):
    img = Image.open(image)
    width, height = img.size
    new_width = nwidth
    new_height = int(height * (new_width / width))
    img = img.resize((new_width, new_height))
    string = random_string(6)
    image_path = os.path.join('images', f'{string}-{image.name}')
    img.save(os.path.join('media', image_path), optimize=True, quality=30)

    return image_path