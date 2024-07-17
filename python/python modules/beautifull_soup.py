from bs4 import BeautifulSoup
import requests


# Function to fetch content from a given URL
def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


# Function to extract post data from a page
def extract_post_data(soup):
    home_titles = soup.find_all(class_="home-title")
    home_descs = soup.find_all(class_="home-desc")
    home_images = soup.find_all(class_="home-img-src lazyload")
    home_urls = soup.find_all(class_="story-link")

    post_data = []

    for i in range(len(home_titles)):
        title = home_titles[i].text.strip()
        desc = home_descs[i].text.strip()
        image_src = (
            home_images[i]["data-src"]
            if home_images[i].has_attr("data-src")
            else home_images[i]["src"]
        )
        url = home_urls[i]["href"]

        post_data.append(
            {"title": title, "description": desc, "image_source": image_src, "url": url}
        )

    return post_data


# Initial URL
url = "https://thehackernews.com/"
soup = fetch_content(url)

# Initialize list to store post data
all_post_data = []

# Input number of pages to fetch
n = int(input("Enter the number of pages to fetch: "))

# Loop through each page and extract data
for _ in range(n):
    post_data = extract_post_data(soup)
    all_post_data.extend(post_data)

    # Find the URL of the next page
    next_page_url = soup.find(class_="blog-pager-older-link-mobile")["href"]

    # Fetch content from the next page
    soup = fetch_content(next_page_url)

# Print the collected data
# for post in all_post_data:
#     print("Title:", post["title"])
#     print("Description:", post["description"])
#     print("Image Source:", post["image_source"])
#     print("URL:", post["url"])
#     print()
    
print(all_post_data)
