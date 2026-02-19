import joblib
import numpy as np
import time

model = joblib.load("ml/model.pkl")

last_motion_time = 0
motion_count = 0

last_help_time = 0
help_count = 0


def detect_gesture(motion):
    global last_motion_time, motion_count
    now = time.time()

    if motion > 10:
        if now - last_motion_time < 3:
            motion_count += 1
        else:
            motion_count = 1
        last_motion_time = now

    if motion_count >= 2:
        motion_count = 0
        return True

    return False


def detect_help(word):
    global last_help_time, help_count
    now = time.time()

    if word == "help":
        if now - last_help_time < 5:
            help_count += 1
        else:
            help_count = 1
        last_help_time = now

    if help_count >= 2:
        help_count = 0
        return True

    return False


def predict_risk(data):

    motion = data["motion"]
    voice = data.get("voice", "")

    X = np.array([[data["heart_rate"], data["temperature"], motion]])
    pred = model.predict(X)

    gesture = detect_gesture(motion)
    panic = detect_help(voice)

    # Immediate emergency if user explicitly signals
    if gesture or panic:
        return "EMERGENCY"

    if data["heart_rate"] > 120 and data["motion"] > 2:
        return "EMERGENCY"

    # Otherwise ML based risk
    if pred[0] == -1:
        return "HIGH"

    return "NORMAL"
