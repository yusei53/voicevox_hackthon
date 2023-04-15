import openai
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
dotenv_path = os.path.join(os.path.dirname(__file__),"../api/.env")
load_dotenv(dotenv_path)

openai.api_key = os.getenv("OPENAI_API_KEY")

def callChatGPT(reply_text, role_text_file, past_messages_list):
    
    # 最初の会話ならrole_text_fileをrole_messageに読み込んでpast_messages_listに追加
    if len(past_messages_list) == 0:
        role_message = ""
        
        with open(role_text_file, 'r') as file:
            dialogue = file.readlines()
        
        for line in dialogue:
                role_message += line
                
        past_messages_list.append({"role": "system", "content": role_message})
        
    # ユーザーからのリプライをpast_messages_listに追加
    past_messages_list.append({"role": "user", "content": reply_text})
    

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=role_messages
        )
    # ChatGPTからの回答をreturn
    return completion["choices"][0]["message"]["content"], past_messages_list