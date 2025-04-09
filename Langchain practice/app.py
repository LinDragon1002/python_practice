# 必要的 imports
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.schema import HumanMessage
import os

load_dotenv()
# os.environ["GOOGLE_API_KEY"] = "AIzaSyA9PyXDHJQ8yrO-NCQV1e5sNJGPi0-x460"
# api = os.getenv("GOOGLE_API_KEY")
# chat = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key="你的_API_金鑰")
chat = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

response = chat([HumanMessage(content="幫我介紹一下台灣的製造產業")])
print(response.content)