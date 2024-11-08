import os

def get_env_variable(var_name):
    """
    Get the value of an environment variable.
    
    Args:
        var_name (str): The name of the environment variable.
    
    Returns:
        str: The value of the environment variable or None if not found.
    """
    value = os.environ.get(var_name)
    if value is None:
        print(f"Warning: Environment variable '{var_name}' not found.")
    return value

def set_env_variable(var_name, value):
    """
    Set a new environment variable.
    
    Args:
        var_name (str): The name of the environment variable.
        value (str): The value to set for the environment variable.
    
    Returns:
        None
    """
    if not value:
        raise ValueError("Value for environment variable cannot be empty.")
    
    os.environ[var_name] = value
    print(f"Environment variable '{var_name}' set to '{value}'.")

def delete_env_variable(var_name):
    """
    Delete an environment variable.
    
    Args:
        var_name (str): The name of the environment variable to delete.
    
    Returns:
        None
    """
    if var_name in os.environ:
        os.environ.pop(var_name)
        print(f"Environment variable '{var_name}' deleted.")
    else:
        print(f"Warning: Environment variable '{var_name}' does not exist.")
        
# Example usage
if __name__ == "__main__":
    set_env_variable('MY_VAR', 'some_value')
    print(get_env_variable('MY_VAR'))
    delete_env_variable('MY_VAR')