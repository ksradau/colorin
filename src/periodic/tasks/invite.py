from celery.utils.log import get_task_logger
from django.db.models import Q

from periodic import tasks
from periodic.app import app
from periodic.utils.xmodels import get_auth_profile_model
from project.utils.date import utcnow
from project.utils.xmail import send_email

logger = get_task_logger(__name__)


@app.task
def invite_all_users():
    logger.debug(f"BEGIN | {invite_all_users.__name__}")

    auth_profile_model = get_auth_profile_model()

    criteria = Q(verified_at__isnull=True) & Q(notified_at__isnull=True)

    auth_profiles = auth_profile_model.objects.filter(criteria)

    logger.debug(
        f"IN | {invite_all_users.__name__} | auth profiles: {auth_profiles.count()}"
    )

    emails = {_prof.user.email for _prof in auth_profiles}

    for email in emails:
        tasks.invite_single_user.delay(email)
        logger.debug(f"IN | {invite_all_users.__name__} | sent {email} to processing")

    logger.debug(f"END | {invite_all_users.__name__}")


logger = get_task_logger(__name__)


@app.task
def invite_single_user(email: str):
    logger.debug(f"BEGIN | {invite_single_user.__name__} | {email}")

    auth_profile_model = get_auth_profile_model()
    auth_profile = auth_profile_model.objects.get(user__email=email)

    logger.debug(f"IN | {invite_single_user.__name__} | {auth_profile}")
    if not auth_profile.link:
        logger.debug(
            f"END |"
            f" {invite_single_user.__name__} |"
            f" skip {auth_profile}, reason: no link"
        )
        return

    service = "ksradau.herokuapp.com".capitalize()

    send_email(
        context={"link": auth_profile.link, "service": service},
        email_to=email,
        mail_template_name="invitation",
        subject=f"Registration at {service}",
    )

    auth_profile.notified_at = utcnow()
    auth_profile.save()

    logger.debug(
        f"END | {invite_single_user.__name__} | email for {auth_profile} has been sent"
    )
