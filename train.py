import os
import openai
openai.api_key = "API-KEY"
file_id = "file-ID"
response = openai.FineTuningJob.create(training_file=file_id, model="gpt-3.5-turbo-0613")
print(response)