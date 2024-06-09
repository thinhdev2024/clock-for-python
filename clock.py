import time

def clock():
    while True:
        current_time = time.strftime("%H:%M")
        print("==time==")
        print(current_time, end="\r")
        print("========")
        print("thinhdev2024")
        time.sleep(60)

if __name__ == "__main__":
    clock()