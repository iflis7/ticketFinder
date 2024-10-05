import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch

# Load the pre-trained SBERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the ServiceNow tickets from Excel
def load_tickets(file_path):
    df = pd.read_excel(file_path)
    # Ensure the DataFrame isn't empty before processing
    if df.empty:
        raise ValueError("The ticket file is empty.")
    return df[['Ticket', 'Description']]

# Function to get similarity score using SBERT embeddings
def get_similarity(input_text, ticket_descriptions):
    # Encode the input query and ticket descriptions using SBERT
    query_embedding = model.encode(input_text, convert_to_tensor=True)
    ticket_embeddings = model.encode(ticket_descriptions, convert_to_tensor=True)

    # Compute cosine similarity between the query and the tickets
    cosine_scores = util.pytorch_cos_sim(query_embedding, ticket_embeddings)
    return cosine_scores

# Function to find the most relevant tickets
def find_relevant_tickets(input_text, tickets, top_n=5):
    descriptions = tickets['Description'].tolist()  # Get all ticket descriptions
    ticket_ids = tickets['Ticket'].tolist()  # Get all ticket IDs
    
    # Get similarity scores between input_text and all tickets
    similarity_scores = get_similarity(input_text, descriptions)

    # Prepare ticket scores
    ticket_scores = [(ticket_ids[i], descriptions[i], similarity_scores[0][i].item()) for i in range(len(ticket_ids))]
    
    # Filter results where score > 0.50
    filtered_tickets = [ticket for ticket in ticket_scores if ticket[2] > 0.20]
    
    # Sort by score and return top N results
    sorted_tickets = sorted(filtered_tickets, key=lambda x: x[2], reverse=True)[:top_n]
    return sorted_tickets
