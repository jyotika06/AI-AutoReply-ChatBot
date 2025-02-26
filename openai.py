from openai import OpenAI
 

client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
[09:30, 26/02/2025] Jyo: Hey, did you complete the assignment?
[09:31, 26/02/2025] Nikki: Not yet, I got stuck on one part.
[09:32, 26/02/2025] Jyo: Which part? Maybe I can help.
[09:33, 26/02/2025] Nikki: The API integration part. It's giving an error.
[09:34, 26/02/2025] Jyo: Oh, I faced that too! Try this tutorial: https://www.youtube.com/watch?v=example
[09:35, 26/02/2025] Nikki: Thanks! I’ll check it out now.
[09:36, 26/02/2025] Jyo: Let me know if it works. We can debug together.
[09:37, 26/02/2025] Nikki: Sure! Appreciate it. 😊
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named jyo who speaks telugu as well as english. She is from India and is a coder. You analyze chat history and respond like jyo"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)
