from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()


intent_classifier = pipeline(
    task='text-classification',
    model='distilbert-base-uncased',
    tokenizer='distilbert-base-uncased',
)

responses = {
    "refund": "Visit our refund portal at https://example.com/refunds",
    "password_reset": "Go to 'Account Settings' > 'Reset Password'",
    "track_order": "Track your order at https://example.com/tracking",
    "default": "Sorry, I couldn’t understand your query. Contact support at help@example.com."
}


@app.get("/")
def home():
    return {"message": "Hello, World!"}


@app.post("/chat")
def chat(query: str):
    result = intent_classifier(query)
    intent = result
    return {"response": "This is a placeholder response. "}
ss=pipeline