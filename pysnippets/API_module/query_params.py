from urllib.parse import urlencode

def serialize_params(params):
    """
    Serialize complex query parameters into a URL-encoded string.
    Handles lists, dictionaries, and nested combinations.

    Args:
        params (dict): The dictionary of parameters to serialize.

    Returns:
        str: URL-encoded query parameters.
    """
    # Recursively encode parameters
    def encode_dict(data):
        for key, value in data.items():
            if isinstance(value, dict):
                for subkey, subvalue in encode_dict(value).items():
                    yield f"{key}[{subkey}]", subvalue
            elif isinstance(value, list):
                for subvalue in value:
                    yield f"{key}[]", subvalue
            else:
                yield key, value

    encoded_params = dict(encode_dict(params))
    return urlencode(encoded_params, doseq=True) 