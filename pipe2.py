from transformers import pipeline
import transformers import AutoTokenizer, AutoModeForSequenceClassification, BertTokenizer, BertModel

classifier = pipeline("sentiment-analysis")

result = classifier("I feel depressed about my rejection in Presidio final round.")

print("Answer: ", result)