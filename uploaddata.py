import openai
import os
openai.api_key = "API-KEY"

response = openai.File.create(
  file=open("trainingsdatagpt3.5v1.2.jsonl", "rb"),
  purpose='fine-tune'
)

print(response)

#Teile hiervon sind von diesem Tutorial: https://www.youtube.com/watch?v=_yzmQbez7gk&t