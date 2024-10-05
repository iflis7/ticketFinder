import webview

# HTML for the interface
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ticket Search</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
            display: flex;
            flex-direction: column;

            align-items: center;
            min-height: 100vh;
        }
        .container {
            min-width: 600px;
            margin: 10px;  /* Adds top margin of 20px */
            background-color: white;
            padding: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            text-align: center;  /* Center contents horizontally */
        }
        #search_text {
            width: 80%;  /* Makes the input box larger */
            padding: 15px;  /* Increase padding for a bigger input */
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 1.2em;  /* Bigger font for the input */
        }
        button {
            padding: 10px;  /* Increase padding to match input height */
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1.2em;  /* Increase font size for the button */
            margin-top: 10px;
        }
        button:hover {
            background-color: #218838;
        }
        .results {
            margin-top: 20px;
        }
        .result-item {
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 6px;
            margin-bottom: 15px;
            background-color: #fdfdfd;
        }
        .result-item:hover {
            background-color: #f1f1f1;
        }
        .ticket-id {
            font-size: 1.1em;
            font-weight: bold;
            color: #007bff;
            user-select: text; /* Makes the ticket ID selectable */
            cursor: copy; /* Indicates that the text is selectable */
        }
        .description {
            font-size: 1em;
            color: #333;
            margin: 10px 0;
        }
        .score {
            font-size: 0.9em;
            color: #888;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        /* Spinner styles */
        .spinner {
            display: none; /* Hidden by default */
            border: 8px solid #f3f3f3; /* Light grey */
            border-top: 8px solid #28a745; /* Blue */
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 2s linear infinite;
            margin: 10px auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .loading-text {
            text-align: center;
            font-size: 1.1em;
            color: #333;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Ticket Search</h1>
    <input id="search_text" type="text" placeholder="Enter your search query"><br>
    <button onClick="searchTickets()">Search tickets</button>

    <div id="spinner-container" class="spinner"></div>
    <div id="results" class="results"></div>
</div>

<script>


    function showSpinner() {
        document.getElementById('spinner-container').style.display = 'block'; // Show the spinner
        document.getElementById('results').style.display = 'none';  // Hide results while loading
    }

    function hideSpinner() {
        document.getElementById('spinner-container').style.display = 'none';  // Hide the spinner
        document.getElementById('results').style.display = 'block';  // Show results after loading
    }

    function showResponse(response) {
        var container = document.getElementById('results');
        container.innerHTML = '';  // Clear the existing content

        // Display the message
        console.log("response.message:", response.message);
        container.innerHTML += `<p>${response.message}</p>`;  // Display the message at the top

        // Display each result in the results array
        if (response.results && response.results.length > 0) {
            response.results.forEach(function(ticket, index) {
                // Append each ticket to the container
                container.innerHTML += `<div class="result-item">
                    <div class="ticket-id">Ticket ID: ${ticket.id}</div>
                    <div class="description"><strong>Description:</strong> ${ticket.description}</div>
                    <div class="score"><strong>Score:</strong> ${ticket.score.toFixed(4)}</div>
                </div>`;
            });
        } else {
            // If no results, display a message
            container.innerHTML += '<p>No results found.</p>';
        }

        hideSpinner();  // Hide spinner once results are displayed
    }

    function searchTickets() {
        var search_text = document.getElementById('search_text').value;
        showSpinner();  // Show the spinner while the search is happening
        pywebview.api.search(search_text).then(showResponse).catch(function(error) {
            console.error("Error during search:", error);
            hideSpinner();  // Hide spinner even if there's an error
        });
    }
</script>
</body>
</html>

"""