from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import OPENAI_API_KEY


class LLMService:
    llm = OpenAI(temperature=0.9)
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
