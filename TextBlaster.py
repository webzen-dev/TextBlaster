import os
import pyautogui
import pyperclip  # For copying to clipboard
import time

# File path
file_path = "file.txt"

# Check if the file exists
if not os.path.exists(file_path):
    print("File not found at:", os.path.abspath(file_path))
    exit()

# Read the file
with open(file_path, "r", encoding="utf-8") as file:
    links = [line.strip() for line in file if line.strip()]  # Remove empty lines

# Notify the user
print(f"Total links to send: {len(links)}")
print("Please click on the input field. The program will start in 3 seconds...")
time.sleep(3)  # Initial delay

# Send the links
for index, link in enumerate(links, start=1):
    pyperclip.copy(link)  # Copy link to clipboard
    pyautogui.hotkey("ctrl", "v")  # Paste the link
    pyautogui.press("enter")  # Send the message
    print(f"Link {index} sent: {link}")  # Display progress for debugging

    # Short delay to prevent potential issues
    time.sleep(0.05)

print("All messages have been sent!")
