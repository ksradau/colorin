from periodic import tasks
from periodic.app import app
from project.utils.date import utcnow
from project.utils.xmail import send_email
from datetime import datetime
from delorean import Delorean

THE_END = Delorean(datetime=datetime(2020, 8, 1, 0, 0), timezone='UTC')

@app.task
def send_smile():

    time_left = str(THE_END - Delorean(utcnow())).split(",")[0]
    send_email(
        context={"time_left": time_left},
        email_to="sushei.ekaterina@gmail.com",
        mail_template_name="smile_message",
        subject="Smile!"
    )
