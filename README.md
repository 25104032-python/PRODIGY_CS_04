🔐 Simple Keylogger

PRODIGY_CS_04 - Prodigy InfoTech Cybersecurity Internship Task 04

Description

This project is a Python-based keyboard monitoring application developed to understand the working principles of keyloggers in cybersecurity. The program captures keyboard events, records the pressed keys, and stores the information in a log file. It demonstrates concepts such as event handling, file operations, and security awareness.

Note: This project is intended only for educational purposes and should be used with proper authorization.

Features

- Monitors keyboard inputs in real-time
- Records both normal and special keys
- Stores captured keystrokes in a text file
- Handles keys like Space, Enter, Esc, and Function keys
- Uses a simple and lightweight implementation
- Provides a safe exit option using F9 key

How It Works

- The "pynput.keyboard.Listener" module continuously monitors keyboard events.
- The "on_press()" function is called whenever a key is pressed.
- The pressed key information is converted into text format.
- The recorded data is stored in "keylog.txt" using file handling.
- Special keys are identified and saved with their key names.
- Pressing the F9 key stops the monitoring process.

Code Explanation

- "Listener()" → Creates a keyboard event listener that runs in the background.
- "on_press(key)" → Detects and captures every key pressed by the user.
- "open("keylog.txt", "a")" → Opens the log file in append mode to store data.
- "str(key)" → Converts keyboard events into readable text.
- "return False" → Terminates the listener when the stop key is pressed

Technologies Used

- Programming Language: Python 3.13
- Library: pynput (Keyboard Event Listener)
- Concepts: Event Handling, File Handling, Keyboard Monitoring

How to Run

1. Install the required library:

py -m pip install pynput

2. Open the "keylogger.py" file in Python IDLE or any code editor.

3. Run the program using:

F5

4. Type any text using the keyboard.

5. Press F9 to stop the keylogger.

6. Open "keylog.txt" to view the recorded keystrokes.


Example

Input (Keys Pressed):

Dream learn achieve

Output (keylog.txt):

'D'

'r'

'e'

'a'

'm'

Key.space

'l'

'e'

'a'

'r'

'n'

Key.space

'a'

'c'


'h'

'i'

'e'

'v'

'e'

Output Explanation:

- Letters are stored as individual key entries.
- Spaces are recorded as "Key.space".
- Special keys are stored using their respective key names.
