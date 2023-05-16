import os
from dotenv import load_dotenv
import streamlit as st
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.llms import OpenAI


def main():
    load_dotenv()

    # Загрузка ключа API OpenAI из переменной окружения
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY не установлен")
        exit(1)
    else:
        print("OPENAI_API_KEY установлен")

    if os.getenv("SERPAPI_API_KEY") is None or os.getenv("SERPAPI_API_KEY") == "":
        print("SERPAPI_API_KEY не установлен")
        exit(1)
    else:
        print("SERPAPI_API_KEY установлен")

    st.set_page_config(page_title="Узнать техинфо")
    st.header('Узнать техинфо')
    
    ic = st.text_input('Введите микросхему:')
    if ic.strip() != '':
        llm = OpenAI(temperature=0)
        tools = load_tools(["serpapi", "llm-math"], llm=llm)
        agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

        response = agent.run(f"For the chip {ic}, provide: 1) Type of package or case; 2) Type of factory packaging (i.e., reel, tray, tube, etc.); 3) Moisture Sensitivity Level (MSL). Only provide the raw data.")
        st.write(response)


if __name__ == '__main__':
    main()
