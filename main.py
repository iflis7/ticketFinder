import webview
from distilbert import load_tickets, find_relevant_tickets  # Import the necessary functions
# from miniLM import load_tickets, find_relevant_tickets  # Import the necessary functions
from interface import html
# import warnings


# warnings.filterwarnings("ignore", category=UserWarning)

class NotExposedApi:
    def notExposedMethod(self):
        return 'This method is not exposed'
   
class Api:
    # Uncomment and define as needed, for now it's commented
    _this_wont_be_exposed = None  # Placeholder for the NotExposedApi class, if necessary
    
    def __init__(self):
        # Initialize the tickets attribute as None for lazy loading
        self.tickets = None

    def load_tickets_if_needed(self):
        # Load the tickets only if they haven't been loaded already
        if self.tickets is None:
            # Ensure the correct path is provided
            file_path = 'tickets1.xlsx'  # Or use os.path.abspath for an absolute path
            print(f"Loading tickets from: {file_path}")
            self.tickets = load_tickets(file_path)
            print(f"Tickets loaded: {file_path}")

    def search(self, query):
        # Ensure tickets are loaded before performing search
        self.load_tickets_if_needed()
        relevant_tickets = find_relevant_tickets(query, self.tickets)
        results = [
            {
                "id": ticket[0],
                "description": ticket[1],
                "score": ticket[2]
            }
            for ticket in relevant_tickets
        ]
        # print("Results: ", results[0])
       
        response = {
        "message": "Found {0} relevant tickets for query '{1}'.".format(len(results), query),
        "results": results
    }
        
        return response


if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Ticket Finder', html=html, js_api=api)
    # webview.start(debug=True)
    webview.start()
    
    