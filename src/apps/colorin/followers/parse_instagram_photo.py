import requests
from dynaconf import settings

url = "https://www.instagram.com/" + settings.INST_USERNAME + "/?__a=1"

r = requests.get(url, headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"})
instagram_json = r.json()

inst_user = instagram_json["graphql"]["user"]
inst_profile_pic = inst_user["profile_pic_url_hd"]
inst_full_name = inst_user["full_name"]
inst_biography = inst_user["biography"]

inst_list_of_photo = inst_user["edge_owner_to_timeline_media"]["edges"]

inst_photo = [inst_list_of_photo[item]["node"]["display_url"] for item in range(11)]


