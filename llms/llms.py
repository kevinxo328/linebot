from langchain import HuggingFaceHub
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import OPENAI_API_KEY, HUGGINGFACEHUB_API_TOKEN


class LLMService:
    repo_id = "google/flan-t5-xl"
    llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0, "max_length": 64})
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)

    @classmethod
    def chain_run(cls, product: str) -> str:
        if not product:
            return "No product provided"
        else:
            return cls.chain.run(product=product)


if __name__ == '__main__':
    print(LLMService.chain_run(product='Tesla'))
