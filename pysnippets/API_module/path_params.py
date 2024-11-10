from urllib.parse import quote

def construct_url(base_url, path_params):
    """
    Construct a URL by appending path parameters to a base URL.
    Path parameters are URL-encoded to handle special characters.

    Args:
        base_url (str): The base URL to which path parameters will be appended.
        path_params (list or tuple): A sequence of path parameters to append to the URL.

    Returns:
        str: The fully constructed URL.
    """
    encoded_params = [quote(str(param)) for param in path_params]
    return f"{base_url}/{'/'.join(encoded_params)}" 