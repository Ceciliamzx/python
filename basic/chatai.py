from langchain.agents import create_react_agent
from langchain.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage


async def planning_agent(user_input):
    llm = getLLM()
    tools = []
    agent = create_react_agent(llm, tools, debug=True)
    inputs = [
        HumanMessage(content=user_input)
    ]
    result = await agent.ainvoke(inputs)
    return result["message"][-1].content


# 增加一个tools 用来长训活动场地信息



async def chatGPT(user_input) -> str:
    llm = getLLM()
    input = [HumanMessage(content=user_input)]
    result = await llm.ainvoke(input)
    return str(result.content)


def getLLM():
    # return ChatOpenAI(
    #     model="gpt-4.1",
    #     base_url="https://api.ephone.chat/v1",
    #     openai_api_key="sk-FggmOewUVBBZZPa9db5sVYeBWBR7UlStTSLKqMSjyUWMf7Nd",
    # )
    return ChatOpenAI(
        model="gpt-5-mini",
        base_url="https://api.open-hk.com/v1",
        openai_api_key="hk-z5bof01000007714d74afb5e94ad74c19a88a4e5b072fca7",
    )