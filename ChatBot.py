import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
  api_key="<Your Key Here>",
)
def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False
pyautogui.click(1639, 1412)

time.sleep(1)  
while True:
    time.sleep(5)
    pyautogui.moveTo(1299,1057)
    pyautogui.dragTo(987, 1061, duration=2.0, button='left')  
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  
    pyautogui.click(1294, 462)
    chat_history = pyperclip.paste()
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named jyo who speaks telugu as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this [9:02, 26/02/2025] Nikki: "},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)
        pyautogui.click(1808, 1328)
        time.sleep(1)  
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  
        pyautogui.press('enter')
