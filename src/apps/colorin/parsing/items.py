import requests

url = "https://www.instagram.com/" + "bohemnaya" + "/?__a=1"

r = requests.get(url, headers={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})
instagram_json = r.json()

inst_user = instagram_json["graphql"]["user"]
inst_list_of_photo = inst_user["edge_owner_to_timeline_media"]["edges"]

inst_photo = []
for item in range(10):
    try:
        inst_photo.append(inst_list_of_photo[item]["node"]["display_url"])
    except IndexError:
        pass
print(inst_photo)
