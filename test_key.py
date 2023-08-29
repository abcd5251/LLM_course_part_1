import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def openai_model(question):
    messages = [{"role":"system","content": f"You are a proficient problem solver, Expertise in finding the answer to the given context information, organizing the answer appropriately, and extracting the key points from the given context information."}]
    messages.append({"role":"user", "content": f"{question}"})

    while True:
        try : 
            response = openai.ChatCompletion.create(
                            model = "gpt-3.5-turbo",
                            messages = messages,
                            temperature = 0.9,
                            max_tokens = 2000
                        )
            break
        except Exception as err:
            print(err)
            
    answer = response.choices[0].message['content'].strip()
    return answer
aa = openai_model("請問1 + 1 = ?")
print(aa)