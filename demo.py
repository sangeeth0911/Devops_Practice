import datetime
import platform

def check_environment():
    print("--- Environment Check ---")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Status: Ready for deployment!")

if __name__ == "__main__":
    check_environment()