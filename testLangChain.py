
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain import LLMChain
import os
from dotenv import load_dotenv 

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

# OpenAIのモデルのインスタンスを作成
llm = OpenAI(model_name="text-davinci-003")

# プロンプトのテンプレート文章を定義
template = """
次の文章に誤字がないか調べて。誤字があれば訂正してください。
{sentences_before_check}
"""

# テンプレート文章にあるチェック対象の単語を変数化
prompt = PromptTemplate(
    input_variables=["sentences_before_check"],
    template=template,
)
# OpenAIのAPIにこのプロンプトを送信するためのチェーンを作成
chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

# チェーンを実行し、結果を表示
if __name__ == '__main__':
    sentence = "昨日、公園で友達と楽しく遊んだ後、近くのお店に行ってアイスクリムを食べました。アイスリムの種類が多く、迷ってしまったのですが、最終的にはチョコレート味を選択しました。帰りみちに、空を見上げると虹がかかっていました。"
    print(chain(sentence))



