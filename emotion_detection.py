def detect_emotion(typing_time):

    if typing_time < 2:
        return 5
    elif typing_time < 5:
        return 10
    else:
        return 20
