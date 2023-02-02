import requests

def shorten_url(full_link):
    # Initializing the base url and api key 
    base_url = " https://cutt.ly/api/api.php"
    API_key = "7e714c94131d1438f9dcb276a6b98695a817d"

    payload = {'key': API_key, 'short': full_link}
    # Getting the data from the given url 
    request = requests.get(base_url, params=payload)
    # Converting the data into json format 
    data = request.json()

    print('')

    try:
        # extracting the title and short_link from the json data 
        title = data['url']['title']
        short_link = data['url']['shortLink']
        # printing the title and short_link
        print("Title: ", title)
        print("Link: ", short_link)
    except:
        # getting the status if any error occurs 
        status = data['url']['status']
        print("Error status: ", status)


# Getting link from the user
input_link = input("Enter the link here: ")
# Calling our function
shorten_url(input_link)
