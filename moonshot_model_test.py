from langchain_community.langchain_moonshot.moonshot import ChatMoonshot
import os


llm = ChatMoonshot(
    moonshot_api_key=os.environ['MOONSHOT_API_KEY']
)

res = llm.invoke("15*16=?")
print(res.content)
