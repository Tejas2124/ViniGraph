from langchain_core.messages import HumanMessage
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import  load_dotenv
load_dotenv()
import  os
key  = os.getenv('GOOGLE_API_KEY')
MODEL = ChatGoogleGenerativeAI(model = "gemini-2.0-flash",api_key = key)


#MODEL =  "gemini-2.0-flash"