import os

def get_env_variable(var_name):
    """
    Get the value of an environment variable.
    
    Args:
        var_name (str): The name of the environment variable.
    
    Returns:
        str: The value of the environment variable or None if not found.
    """
    return os.environ.get(var_name)

def set_env_variable(var_name, value):
    """
    Set a new environment variable.
    
    Args:
        var_name (str): The name of the environment variable.
        value (str): The value to set for the environment variable.
    
    Returns:
        None
    """
    os.environ[var_name] = value

def delete_env_variable(var_name):
    """
    Delete an environment variable.
    
    Args:
        var_name (str): The name of the environment variable to delete.
    
    Returns:
        None
    """
    os.environ.pop(var_name, None)
