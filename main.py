# main.py

from logger.keylogger import simulate_keylogger

if __name__ == "__main__":
    print("Starting Enhanced Keylogger Simulation...")
    simulate_keylogger()

# Package initialization

import time
import random
from logger.analytics import calculate_typing_speed, detect_repeated_patterns
from logger.security import encrypt_logs, detect_keywords
from logger.storage import log_to_file, log_to_json
from logger.system_simulation import get_active_window, get_clipboard_content, capture_screen
from logger.emailer import send_logs_via_email

def simulate_keylogger():
    print("Simulated Keylogger is running. Type 'exit' to stop.\n")
    start_time = None
    log_file = "keylog_colab.txt"
    total_keystrokes = ""
    
    with open(log_file, "a") as file:
        while True:
            user_input = input("Enter some text (type 'exit' to stop): ")
            
            if user_input.lower() == "exit":
                print("Keylogger simulation stopped.")
                break
            
            if start_time is None:
                start_time = time.time()
            
            end_time = time.time()
            typing_speed = calculate_typing_speed(start_time, end_time, user_input)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            active_window = get_active_window()
            clipboard_content = get_clipboard_content()
            detected_keyword = detect_keywords(user_input)
            repeated_patterns = detect_repeated_patterns(user_input)
            encrypted_input = encrypt_logs(user_input)
            log_to_file(file, timestamp, active_window, encrypted_input, clipboard_content, typing_speed, detected_keyword, repeated_patterns)
            log_to_json({
                "timestamp": timestamp,
                "active_window": active_window,
                "keystroke": encrypted_input,
                "clipboard": clipboard_content,
                "typing_speed": typing_speed,
                "keyword_detected": detected_keyword,
                "repeated_patterns": list(repeated_patterns) if repeated_patterns else None
            })

            if random.randint(1, 5) == 3:
                capture_screen()
            
            if random.randint(1, 10) == 5:
                send_logs_via_email()

            print(f"Logged: {user_input} (Window: {active_window}, Clipboard: {clipboard_content}, Speed: {typing_speed:.2f} chars/sec)")
 

def calculate_typing_speed(start_time, end_time, keystrokes):
    elapsed_time = end_time - start_time
    if elapsed_time > 0:
        return len(keystrokes) / elapsed_time
    return 0

def detect_repeated_patterns(keystroke):
    words = keystroke.split()
    repeated_words = {word for word in words if words.count(word) > 1}
    return repeated_words if repeated_words else None

def encrypt_logs(data):
    return "".join(reversed(data))

def detect_keywords(keystroke, keywords=["password", "secret", "confidential"]):
    for keyword in keywords:
        if keyword in keystroke.lower():
            return keyword
    return None

import json

def log_to_file(file, timestamp, active_window, keystroke, clipboard, typing_speed, keyword, patterns):
    file.write(f"{timestamp} - Active Window: {active_window}\n")
    file.write(f"{timestamp} - Keystroke (Encrypted): {keystroke}\n")
    file.write(f"{timestamp} - Clipboard: {clipboard}\n")
    file.write(f"{timestamp} - Typing Speed: {typing_speed:.2f} chars/sec\n")
    if keyword:
        file.write(f"{timestamp} - ALERT: Detected sensitive keyword '{keyword}'\n")
    if patterns:
        file.write(f"{timestamp} - WARNING: Repeated patterns detected: {patterns}\n")

def log_to_json(data):
    log_json_file = "keylog_colab.json"
    with open(log_json_file, "w") as json_file:
        json.dump({"logs": [data]}, json_file, indent=4)
import random
import string
import time

def get_active_window():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def get_clipboard_content():
    return "Simulated Clipboard Content"

def capture_screen(file_name="screenshot.txt"):
    with open(file_name, "a") as screenshot_file:
        screenshot_file.write(f"Screenshot taken at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")

def send_logs_via_email():
    print("Simulated: Logs sent via email")
