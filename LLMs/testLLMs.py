from langchain.llms import OpenAI
import os
from dotenv import load_dotenv 

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


def main():
   #llm = OpenAI(model_name="text-davinci-003")
    llm = OpenAI(model_name="text-davinci-003")
    response = llm("日本の歴代総理大臣を3名教えて。")
    print(response)

if __name__ == "__main__":
    main()
