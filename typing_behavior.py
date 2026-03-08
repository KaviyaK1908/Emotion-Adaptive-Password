import time

def measure_typing_speed():
    start_time = time.time()
    password = input()
    end_time = time.time()

    typing_time = end_time - start_time
    return password, typing_time
