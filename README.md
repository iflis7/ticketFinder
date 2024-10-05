# Ticket Finder with SBERT

This project is a **Ticket Finder** that uses **Sentence-BERT (SBERT)** to match user input queries with the most relevant ServiceNow tickets. The system computes the similarity between the user query and ticket descriptions and returns the most relevant tickets based on cosine similarity.

## Features

- **Semantic Search**: Utilizes SBERT to perform a semantic search across tickets.
- **Similarity Scoring**: Ranks tickets by their similarity score to the input query.
- **Thresholding**: Only returns results with a similarity score greater than 0.50.

## Technology Stack

- Python 3
- [Sentence-BERT (SBERT)](https://www.sbert.net/)
- Hugging Face's [transformers](https://huggingface.co/transformers/) library
- Pandas
- PyTorch

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ticket-finder.git
    cd ticket-finder
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

    **Note**: Make sure that you have the following packages in your `requirements.txt` file:
    ```
    pandas
    sentence-transformers
    torch
    transformers
    ```

3. Download or prepare the ticket data (Excel file) and place it in the project directory.

## Usage

1. Run the script to load tickets from an Excel file and perform a search:

    ```python
    python search.py
    ```

    Example usage in Python:
    ```python
    from search import load_tickets, find_relevant_tickets

    # Load tickets from an Excel file
    tickets = load_tickets('tickets.xlsx')

    # User query
    user_input = "spacing issue in fund balance"

    # Find relevant tickets
    relevant_tickets = find_relevant_tickets(user_input, tickets)

    # Print the results
    for ticket in relevant_tickets:
        print(f"Ticket ID: {ticket[0]}\nDescription: {ticket[1]}\nScore: {ticket[2]:.4f}\n")
    ```

2. **Results**: The system will output the most relevant tickets and their similarity scores. Only tickets with a score above 0.50 are shown.

## Project Structure


## How It Works

1. **Ticket Loading**: The tickets are loaded from an Excel file using Pandas.
2. **Sentence Embeddings**: The system encodes both the query and ticket descriptions into sentence embeddings using SBERT (`all-MiniLM-L6-v2` model).
3. **Similarity Calculation**: Cosine similarity is used to measure the relevance of each ticket to the query.
4. **Result Filtering**: Only tickets with a score greater than 0.50 are displayed, and the top N results (default is 5) are shown.

## Example Output

```plaintext
Query: spacing issue in fund balance
Ticket ID: INC0322979
Description: Spacing and subtotal column under statement of change in fund balance.
Score: 0.8623

Ticket ID: INC0322980
Description: Network latency in data center
Score: 0.6942


### How to Use It:
- Save this content as `README.md` in the root of your project.
- Adjust the project name, repository URL (`git clone`), and any other specific details to match your repository.
- Make sure the paths (like `tickets.xlsx` and `search.py`) reflect your actual project structure.

Let me know if you need any further modifications!
