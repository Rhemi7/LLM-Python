import os
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

if __name__ == "__main__":
    print("hello langchain")

    linkedin_profile_url = linkedin_lookup_agent(name="Eden marco udemy")

    summary_template = """
        given the Linkedin information {information} about a person, I want you to create:
        1. A short summary
        2. Two interesting facts about time
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(profile_url=linkedin_profile_url)

    res = chain.invoke(input={"information": linkedin_data})

    print(f"Result {res}")
