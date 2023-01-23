import requests

def shorten_url(full_link):
    base_url = " https://cutt.ly/api/api.php"
    API_key = "7e714c94131d1438f9dcb276a6b98695a817d"

    payload = {'key': API_key, 'short': full_link}
    request = requests.get(base_url, params=payload)
    data = request.json()

    print('')

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        print("Title: ", title)
        print("Link: ", short_link)
    except:
        status = data['url']['status']
        print("Error status: ", status)

input_link = input("Enter the link here: ")


shorten_url(input_link)

