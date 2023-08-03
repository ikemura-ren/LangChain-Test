from langchain.embeddings import OpenAIEmbeddings

import os
from dotenv import load_dotenv 

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


def main():
    embeddings = OpenAIEmbeddings()
    query_result = embeddings.embed_query("ITエンジニアについて30文字で教えて。")

    print(query_result)


if __name__ == "__main__":
    main()
