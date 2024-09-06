'''Utils'''
import base64

def encode_image(image_path):
    """
    Encodes an image to a base64 string.

    This function reads an image file from the specified path,
    encodes the image in base64 format, and returns the encoded
    string.

    Parameters:
    image_path (str): The path to the image file to be encoded.

    Returns:
    str: A base64 encoded string of the image content.

    Example:
    --------
    >>> encoded_string = encode_image('path/to/image.jpg')
    >>> print(encoded_string)
    'iVBORw0KGgoAAAANSUhEUgAA...'

    Note:
    -----
    The example assumes that 'path/to/image.jpg' is a valid path to an image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
