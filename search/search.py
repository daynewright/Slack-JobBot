from craigslist import CraigslistHousing
from slackclient import SlackClient
from apscheduler.schedulers.blocking import BlockingScheduler
from dicesearch import get_dice
from craigslistsearch import get_craigslist
import time

sched = BlockingScheduler()

SLACK_TOKEN = "TOKEN_GOES_HERE"
SLACK_CHANNEL = "check_jobs_test"

sc = SlackClient(SLACK_TOKEN)

def check_job():
    print("Checking for new jobs...")

    introMessage= "\n :point_right: `NEW JOBS FOR {0}` :point_left: \n".format(time.strftime("%x"))

    sc.api_call(
        "chat.postMessage", channel=SLACK_CHANNEL, text=introMessage,
        username='JobBot', icon_emoji=':nerd_face:'
    )

    craigslist_jobs = get_craigslist()

    for job in craigslist_jobs:
        sc.api_call(
            "chat.postMessage", channel=SLACK_CHANNEL, text=job,
            username='JobBot', icon_emoji=':nerd_face:'
        )
    
    dice_jobs = get_dice()

    for job in dice_jobs:
        sc.api_call(
            "chat.postMessage", channel=SLACK_CHANNEL, text=job,
            username='JobBot', icon_emoji=':nerd_face:'
        )
    
    goodbye = ":wave: *My job here is done. I will be back tomorrow!* :wave:"
    sc.api_call(
        "chat.postMessage", channel=SLACK_CHANNEL, text=goodbye,
        username='JobBot', icon_emoji=':nerd_face:'
    )
    print("Waiting to run job search again...")

message = ":wave: *I am here and working!*"

sc.api_call(
        "chat.postMessage", channel=SLACK_CHANNEL, text=message,
        username='JobBot', icon_emoji=':nerd_face:'
)

check_job()

sched.add_job(check_job, 'interval', hours=24)
sched.start()

