from craigslist import CraigslistHousing
from slackclient import SlackClient
from aspscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

SLACK_TOKEN = "TOKEN_GOES_HERE"
SLACK_CHANNEL = "test_channel"

def check_job():
    print("Checking for new jobs...")
    SLACK_TOKEN = "TOKEN_GOES_HERE"
    SLACK_CHANNEL = "test_channel"

    sc = SlackClient(SLACK_TOKEN)

    cl = CraigslistHousing(site='nashville', category='sof',
                            filters={'posted_today': True })

    results = cl.get_results(sort_by='newest', limit=20)

    if any(True for _ in results):
        for result in results:
            if 'nashville' in result['url']:
                desc = ":desktop_computer:  A new JOB was posted on CraigsList: \n <{1}|{0}> Located in *{2}* Listed on *{3}*".format(result["name"], result["url"], result["where"], result["datetime"])

                sc.api_call(
                    "chat.postMessage", channel=SLACK_CHANNEL, text=desc,
                    username='JobBot', icon_emoji=':nerd_face:'
                )
        print("Done checking jobs and new jobs added to slack.")
    else:
        desc ="No new jobs were added today. :thumbsdown:"
        sc.api_call(
            "chat.postMessage", channel=SLACK_CHANNEL, text=desc,
            username='JobBot', icon_emoji=':unamused:'
        )
        print("Done checking jobs and no new jobs added so far today. Checking again in 12 hours! :)")

sched.add_job(check_job, 'interval', hours=12)
sched.start()
