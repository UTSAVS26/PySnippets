from Property import user

# Test Cases
def test_dynamic_property_creation():
    assert user.name == "Alice", "Test case failed: Incorrect name"
    assert user.age == 25, "Test case failed: Incorrect age"

# Running test cases
test_dynamic_property_creation()
print("Test cases passed for dynamic property creation.")
