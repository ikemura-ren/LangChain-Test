from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv 

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


def main():
    system_template="あなたは、質問者からの質問を{language}で回答するAIです。"
    human_template="質問者：{question}"
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    prompt_message_list = chat_prompt.format_prompt(language="日本語", question="ITエンジニアについて30文字で教えて。").to_messages()

    print(prompt_message_list)

    chat = ChatOpenAI(model_name="gpt-3.5-turbo")
    chat(prompt_message_list)

if __name__ == "__main__":
    main()
