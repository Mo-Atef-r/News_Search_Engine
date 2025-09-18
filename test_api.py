import requests
import json
import codecs

api_url = 'http://127.0.0.1:8000/api/search/'
query = "computer graphics technology"

# Create the data payload for the request
data = {
    'query': query
}

print(f"Sending request for query: '{query}'")

try:
    # Send a POST request to the API
    response = requests.post(api_url, json=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()
        print("\nAPI Call Successful! Here are the top results:")
        
        for i, result in enumerate(results):
            score = result['score']
            content = result['content']
            
            print(f"\n--- Result {i + 1} (Score: {score:.2f}) ---")
            print(content[:200] + '...') # Print a snippet of the content
            
    else:
        print(f"\nAPI Call Failed. Status Code: {response.status_code}")
        # Write the response content to a file with UTF-8 encoding to avoid the print error
        with codecs.open("error_log.txt", "w", "utf-8") as f:
            f.write(response.text)
        print("Error details saved to error_log.txt. Check the file for the full traceback.")
        
except requests.exceptions.RequestException as e:
    print(f"\nAn error occurred: {e}")