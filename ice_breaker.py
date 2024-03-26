import os
from fastapi import FastAPI
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
# from third_parties.twitter import scrape_user_tweets
from output_parsers import PersonIntel, person_intel_parser


def ice_break(name: str) -> PersonIntel:
# "Eric Marco Udemy"
    linkedin_profile_url = linkedin_lookup_agent(name= name)
    linkedin_data = scrape_linkedin_profile(profile_url=linkedin_profile_url)

    # twitter_username = twitter_lookup_agent(name=name)
    # tweets = scrape_user_tweets(username=twitter_username, num_tweets=100)

    summary_template = """
        given the Linkedin information {linkedin_information} about a person, I want you to create:
        1. A short summary
        2. Two interesting facts about them
      

        \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    res = chain.invoke(
        input={"linkedin_information": linkedin_data}
    )

    print(res["text"])

    return person_intel_parser.parse(res["text"])




    
