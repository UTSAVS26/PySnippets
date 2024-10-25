import random
import string

def generate_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

#example usage
#password_length = 12
#print("Generated password:", generate_password(password_length))
