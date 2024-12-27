# TextBlaster

TextBlaster is a Python script designed to automate the process of sending lines of text from a `.txt` file to an active input field. This program can handle any type of text, making it versatile for tasks like bulk messaging, link sharing, or automating repetitive typing tasks.

## Features
- Reads lines of text from a `.txt` file.
- Automatically pastes each line into an active input field.
- Supports customizable delays between messages for flexibility.
- Easy to set up and use.

## Requirements
- Python 3.6+
- `pyautogui` library
- `pyperclip` library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/webzen-dev/TextBlaster.git
   ```
2. Navigate to the project directory:
   ```bash
   cd TextBlaster
   ```
3. Install the required libraries:
   ```bash
   pip install pyautogui pyperclip
   ```

## Usage
1. Place your `.txt` file in an accessible directory and note its path.
2. Open the script and update the `file_path` variable with the path to your `.txt` file:
   ```python
   file_path = "C:/path/to/your/file.txt"
   ```
3. Run the script:
   ```bash
   python textblaster.py
   ```
4. Focus on the input field where you want the text to be sent, and the program will handle the rest.

## Example
Suppose your `tld.txt` file contains the following lines:
```
Hello, this is the first message.
Automation is fun!
```
The program will sequentially send each line to the active input field, pressing `Enter` after each one.

## Customization
- **Delay Between Messages**: You can adjust the delay between messages by modifying the `time.sleep()` value in the script.
  ```python
  time.sleep(0.05)  # Adjust delay as needed
  ```
- **Debugging Output**: The script prints progress to the console. You can remove or customize these messages as needed.

## Notes
- Ensure that the input field is active before running the script.
- Avoid using this script for spam or activities that violate the terms of service of platforms.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.

## Author
https://github.com/webzen-dev
