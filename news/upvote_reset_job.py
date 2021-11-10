from apscheduler.schedulers.background import BackgroundScheduler

from .models import Post


def post_upvote_reset():
    """
    Post upvote count reset function
    """
    Post.objects.all().update(upvote_count=0)


def start():
    """
    Recurring job starter function
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(post_upvote_reset, "interval", days=1)
    scheduler.start()
