from langchain import PromptTemplate
from langchain.llms import OpenAI

import os
from dotenv import load_dotenv 

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

def main():
    # 命令文のテンプレートを作成できる
    template = """
    {subject}について30文字で教えて。
    """

    prompt = PromptTemplate(
		    template=template,
        input_variables=["subject"]
    )
    prompt_text = prompt.format(subject="パイロット")
    print(prompt_text)


    llms = OpenAI(model_name="text-davinci-003")
    print(llms(prompt_text))

if __name__ == "__main__":
    main()

