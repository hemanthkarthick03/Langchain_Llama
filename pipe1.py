from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("I feel strong after watching today's One pice episode")

print("Answer: ", result)