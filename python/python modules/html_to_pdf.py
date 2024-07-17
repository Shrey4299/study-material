import requests


def html_to_pdf(html_content):
    """
    Converts an HTML string to a PDF and saves it to the given output path using the Sejda HTML to PDF converter API with an API key configuration.
    """
    # Build the request URL and headers
    url = "https://api.sejda.com/v2/html-pdf"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token: {sejda_api_key}" # type: ignore
    }

    # Build the request data
    data = {
        "htmlCode": html_content
    }

    # Make the API request
    response = requests.post(url, headers=headers, json=data)
    
        # Save the PDF file to disk
    return response.content