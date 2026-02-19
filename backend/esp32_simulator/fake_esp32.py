import requests
import random
import time

URL = "http://127.0.0.1:8000/sensor"

print("Fake ESP32 started...")

while True:

    # -------- NORMAL --------
    print("\nNORMAL STATE")
    for i in range(3):
        payload = {
            "heart_rate": random.randint(70, 100),
            "temperature": 36.6,
            "motion": 2,
            "voice": "",
            "lat": 17.3850,
            "lon": 78.4867
        }

        r = requests.post(URL, json=payload)
        print("Normal:", r.json())
        time.sleep(2)

    # -------- GESTURE --------
    print("\nGESTURE TRIGGER")

    payload["motion"] = 12
    payload["voice"] = ""
    r = requests.post(URL, json=payload)
    print("Gesture spike 1:", r.json())
    time.sleep(1)

    payload["motion"] = 13
    r = requests.post(URL, json=payload)
    print("Gesture spike 2:", r.json())
    time.sleep(4)

    # -------- PANIC VOICE --------
    print("\nPANIC VOICE")

    payload["motion"] = 2
    payload["voice"] = "help"
    r = requests.post(URL, json=payload)
    print("Help 1:", r.json())
    time.sleep(1)

    r = requests.post(URL, json=payload)
    print("Help 2:", r.json())
    time.sleep(6)
