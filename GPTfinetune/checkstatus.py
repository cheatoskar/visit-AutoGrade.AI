import openai

# API Key (private)
openai.api_key = "API-KEY"

# File ID, aendert sich, je nach Modell
file_id = "file-ID"

file_info = openai.File.retrieve(id=file_id)
print("File Status:", file_info.status)
print("Status Details:", file_info.status_details)
