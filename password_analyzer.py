import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 20

    if re.search("[A-Z]", password):
        score += 10

    if re.search("[a-z]", password):
        score += 10

    if re.search("[0-9]", password):
        score += 10

    if re.search("[!@#$%^&*]", password):
        score += 10

    return score
