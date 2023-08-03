from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
)

import os
from dotenv import load_dotenv 

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


def main():
    chat = ChatOpenAI(model_name="gpt-3.5-turbo")
    response = chat([
	    SystemMessage(content="日本語で回答して。"),
	    HumanMessage(content="ITエンジニアの平均年収を教えて。"),
    ])
    print(response)

if __name__ == "__main__":
    main()
