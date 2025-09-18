from transformers import pipeline

model = pipeline("summarization", model="facebook/bart-large-cnn")
response = model("Summarize one of the chapters in Harry Potter's first book")

print(response)