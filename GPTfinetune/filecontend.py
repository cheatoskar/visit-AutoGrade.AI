import os
import openai
openai.api_key = "API-KEY"
content = openai.File.download("file-ID")
print(content)