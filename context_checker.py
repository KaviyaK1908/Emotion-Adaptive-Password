def check_context_similarity(username, password):

    score = 30

    if username.lower() in password.lower():
        score -= 20

    if "123" in password or "password" in password.lower():
        score -= 10

    return max(score,0)
