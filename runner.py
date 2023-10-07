from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
import os
from dotenv import load_dotenv

from few_shots import few_shots

load_dotenv()

def configure():
    llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.2)

    # Connect to DB
    db_user = "root"
    db_password = "root"
    db_host = "localhost"
    db_name = "my_bookstore"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)

    to_vectorize = [" ".join(example.values()) for example in few_shots]
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    vectorestore = Chroma.from_texts(to_vectorize, embedding=embeddings, metadatas=few_shots)

    example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vectorestore,
    k=2,        # 2 select examples
    ) 

    example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}"
    )   

    few_shots_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=_mysql_prompt,
    suffix=PROMPT_SUFFIX,
    input_variables=["input", "table_info", "top_k"]
    )
    
    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shots_prompt)
    return chain



# chain = configure()
# print(chain.run("if i sold all the quantities in the store with discount, what book will make me the least money?"))



    




