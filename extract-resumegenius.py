import requests
from bs4 import BeautifulSoup
import json

# Send a GET request
url = "https://resumegenius.com/resume-samples"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the div with class 'categories'
categories_div = soup.find("section", id="categories")

# Find the ul with class 'categories__list' inside the categories_div
ul = categories_div.find("ul", class_="category-list")

# Initialize a dictionary to store categories and their data
categories_data = {}

# Find and extract category information
for li in ul.find_all("li"):
    # Extract the category ID from the 'data-category' attribute
    category_id = li.find("a").get('href')[1:]

    # Extract the category title from the span with class 'categories__label'
    category_title = li.find("span").text

    # Store the relative URL only, no need to prepend the base URL
    category_data = {
        "id": category_id,
        "subcategories": {}
    }
    
    # Find the div with the corresponding category_id
    category_div = soup.find("div", id=category_id)

    # Find subcategories and extract the text and href
    subcategories = {}
    for sub_li in category_div.find_all("li"):
        li = sub_li.find("a")
        subcategory_text = li.text
        subcategory_relative_url = li.get('href')
        
        # Store the relative URL only, no need to prepend the base URL
        subcategory_data = {
            "url": subcategory_relative_url.replace('https://resumegenius.com', '')
        }
        subcategories[subcategory_text] = subcategory_data

    # Store subcategories in the category data
    category_data["subcategories"] = subcategories

    # Store category data in the dictionary
    categories_data[category_title] = category_data

# Save the categories_data dictionary as a JSON file
with open("data/resumegenius.json", "w") as json_file:
    json.dump(categories_data, json_file, indent=4)

print("Category data saved to categories.json")

# # Initialize a dictionary to store subcategory data with first lines of HTML
# subcategories_data = {}

# # Iterate through the categories and fetch HTML first lines for each subcategory
# for category_title, category_data in categories_data.items():
#     for subcategory_text, subcategory_data in category_data["subcategories"].items():
#         subcategory_relative_url = subcategory_data["url"]
#         subcategory_full_url = f"https://zety.com{subcategory_relative_url}"
        
#         # Fetch the HTML content of the subcategory URL
#         subcategory_response = requests.get(subcategory_full_url)
#         subcategory_html = subcategory_response.text
        
#         # Extract the first line of HTML content
#         first_line_of_html = subcategory_html.split("\n")[0]
        
#         # Store subcategory data with first line of HTML
#         subcategories_data[subcategory_text] = {
#             "id": category_data["id"],
#             "url": subcategory_relative_url,
#             "first_line_of_html": first_line_of_html
#         }

#         # Print the name of the current resume being fetched
#         print(f"Fetching first line for: {subcategory_text}")

# # Save the subcategories_data dictionary as a JSON file
# with open("data/resumes.json", "w") as json_file:
#     json.dump(subcategories_data, json_file, indent=4)

# print("Resume data saved to resumes.json")
