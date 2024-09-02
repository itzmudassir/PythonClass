import requests

# Define the API endpoint
url = 'https://api.openweathermap.org/data/2.5/weather?lat=30.551&lon=73.391&appid=94e563d7ef8e826858cdfbc6165868a2'

# Make the GET request to the API
response = requests.get(url)
# print(response)
posts = response.json()
print(posts)
# print(f"Title of the first post: {posts[1]['title']}")
# for post in posts:
#         print(f"\nPost ID: {post['id']}")
#         print(f"Title: {post['title']}")
#         print(f"Body: {post['body']}")

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the JSON data
#     posts = response.json()
    
#     # Print the title of the first post
#     print(f"Title of the first post: {posts[0]['title']}")
    
#     # Optionally, print all posts
#     for post in posts:
#         print(f"\nPost ID: {post['id']}")
#         print(f"Title: {post['title']}")
#         print(f"Body: {post['body']}")
# else:
#     print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
