from pydantic import BaseModel, field_validator, model_validator
import re

# 1. Validate password strength
class UserWithValidation(BaseModel):
    username: str
    password: str

    @field_validator('password')
    def check_password_strength(cls, value):
        if len(value) < 8 or not re.search(r"[A-Z]", value) or not re.search(r"[0-9]", value):
            raise ValueError("Password must be at least 8 characters long and contain a number and an uppercase letter.")
        return value

# 2. Validate all numbers are even
class EvenNumbers(BaseModel):
    numbers: list[int]

    @model_validator(mode='after')
    def validate_even_numbers(cls, values):
        if any(n % 2 != 0 for n in values.numbers):
            raise ValueError("All numbers must be even")
        return values

#  Usage
print("\n Validating Strong Password")
user_valid = UserWithValidation(username="bob", password="StrongPass123")
print(user_valid)

print("\n Validating Even Numbers")
even_valid = EvenNumbers(numbers=[2, 4, 6])
print(even_valid)
