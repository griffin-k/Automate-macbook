import speech_recognition as sr
import pyautogui

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        return None

import pyautogui

def control_mac(command):
    if "scroll up" in command:
        pyautogui.scroll(3)  # You can adjust the scroll amount as needed
    elif "scroll down" in command:
        pyautogui.scroll(-3)  # You can adjust the scroll amount as needed
    elif "open new tab" in command:
        pyautogui.hotkey('command', 't')
    elif "close tab" in command:
        pyautogui.hotkey('command', 'w')
    elif "go back" in command:
        pyautogui.hotkey('command', '[')
    elif "go forward" in command:
        pyautogui.hotkey('command', ']')
    elif "refresh" in command:
        pyautogui.hotkey('command', 'r')
    elif "open history" in command:
        pyautogui.hotkey('command', 'y')
    elif "open downloads" in command:
        pyautogui.hotkey('command', 'shift', 'j')
    elif "zoom in" in command:
        pyautogui.hotkey('command', '=')
    elif "zoom out" in command:
        pyautogui.hotkey('command', '-')
    elif "reset zoom" in command:
        pyautogui.hotkey('command', '0')
    elif "find" in command:
        pyautogui.hotkey('command', 'f')
    elif "open developer tools" in command:
        pyautogui.hotkey('command', 'option', 'i')
    elif "open finder" in command:
        pyautogui.hotkey('command', 'space')  
        pyautogui.write('finder')
        pyautogui.press('return')
    elif "close finder" in command:
        pyautogui.hotkey('command', 'w')  
    elif "open whatsapp" in command:
        pyautogui.hotkey('command', 'space')  
        pyautogui.write('whatsapp')
        pyautogui.press('return')
    elif "close whatsapp" in command:
        pyautogui.hotkey('command', 'w') 
    elif "open launchpad" in command:
        pyautogui.hotkey('command', 'space') 
        pyautogui.write('launchpad')
        pyautogui.press('return')
    elif "close launchpad" in command:
        pyautogui.hotkey('esc') 
    elif "hide window" in command:
        pyautogui.hotkey('command', 'h')
    elif "show window" in command:
        pyautogui.hotkey('command', 'option', 'h')  
    elif "quit application" in command:
        pyautogui.hotkey('command', 'q')
    elif "minimize window" in command:
        pyautogui.hotkey('command', 'm')
    elif "minimize all windows" in command:
        pyautogui.hotkey('command', 'option', 'm')
    elif "take screenshot" in command:
        pyautogui.hotkey('command', 'shift', '3')
    elif "close window" in command:
        pyautogui.hotkey('command', 'w')
    elif "full screen" in command:
        pyautogui.hotkey('control', 'command', 'f')
    elif "sleep" in command:
        pyautogui.hotkey('control', 'shift', 'power') 
    elif "lock screen" in command:
        pyautogui.hotkey('control', 'command', 'q')
    elif "log out" in command:
        pyautogui.hotkey('command', 'shift', 'q')    
        
    else:
        print("Command not recognized.")


if __name__ == "__main__":
    while True:
        user_input = speech_to_text()
        if user_input:
            control_mac(user_input)
