from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
from dynaconf import settings

set_workspace(path=None)

session = InstaPy(username=settings.INST_USERNAME, password=settings.INST_PASSWORD, browser_executable_path=r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
print("Session created")

with smart_run(session):
    hide_followers = session.grab_followers(username="minskhide", amount="full", live_match=True, store_locally=True)
    print("Followers grabed!")
    with open("output.txt") as file:
        for item in hide_followers:
            file.write("%s\n" % item)
    print("Followers put into output file!")
