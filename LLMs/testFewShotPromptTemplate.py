from langchain import PromptTemplate, FewShotPromptTemplate
from langchain.llms import OpenAI

import os
from dotenv import load_dotenv 

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

def main():
    examples = [
    {"name": "フシギダネ", "type": "草"},
    {"name": "ヒトカゲ", "type": "炎"},
    {"name": "ミズガメ", "type": "水"},
    ]

    example_formatter_template = """
    ポケモンの名前: {name}
    タイプ: {type}\n
    """
    example_prompt = PromptTemplate(
        template=example_formatter_template,
        input_variables=["name", "type"]
    )

    few_shot_prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix="このポケモンのタイプを教えて",
        suffix="ポケモンの名前: {input}\n",
        input_variables=["input"],
        example_separator="\n\n",

    )

    prompt_text = few_shot_prompt.format(input="ピカチュウ")
    print(prompt_text)

    llm = OpenAI(model_name="text-davinci-003")
    print(llm(prompt_text))

if __name__ == "__main__":
    main()

