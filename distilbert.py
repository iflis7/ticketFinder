import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the pre-trained BERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=1)

# Load the ServiceNow tickets from Excel
def load_tickets(file_path):
    df = pd.read_excel(file_path)
    # Ensure the DataFrame isn't empty before processing
    if df.empty:
        raise ValueError("The ticket file is empty.")
    return df[['Ticket', 'Description']]


# Function to get similarity score using BERT embeddings
def get_similarity(input_text, ticket_description):
    inputs = tokenizer(input_text, ticket_description, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    score = torch.sigmoid(outputs.logits).item()  # Similarity score between 0 and 1
    return score

# Function to find the most relevant tickets
def find_relevant_tickets(input_text, tickets, top_n=5):
    ticket_scores = []
    for _, row in tickets.iterrows():
        ticket_id = row['Ticket']
        description = row['Description']
        score = get_similarity(input_text, description)
        ticket_scores.append((ticket_id, description, score))

    # Sort by score and return top N results
    sorted_tickets = sorted(ticket_scores, key=lambda x: x[2], reverse=True)[:top_n]
    return sorted_tickets
