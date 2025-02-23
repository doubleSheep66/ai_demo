import os

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["OPENAI_API_KEY"] = "sk-yakwcupisqcgqxtnpdtqnlnptkzcyurxgimxzavgzoxnosmk"
os.environ["LANGCHAIN_API_KEY"] = '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'
model = ChatOpenAI(base_url="https://api.siliconflow.cn/v1",model='deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B')
prompt_template = ChatPromptTemplate.from_messages([
   ("system","你是数学家"),
   ("user","{input}")
])
parser = StrOutputParser()
chain = prompt_template | model | parser
result = chain.invoke({'input': "计算1+1=？"})
print(result)

