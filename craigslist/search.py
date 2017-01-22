from craigslist import CraigslistHousing
from slackclient import SlackClient

SLACK_TOKEN = "TOKEN_GOES_HERE"
SLACK_CHANNEL = "test_channel"

sc = SlackClient(SLACK_TOKEN)

cl = CraigslistHousing(site='nashville', category='sof',
                        filters={'posted_today': False })

results = cl.get_results(sort_by='newest', geotagged=True, limit=20)

for result in results:
    if 'nashville' in result['url']:

        desc = ":desktop_computer:  A new JOB was posted on CraigsList: \n <{1}|{0}> Located in *{2}* Listed on *{3}*".format(result["name"], result["url"], result["where"], result["datetime"])

        sc.api_call(
            "chat.postMessage", channel=SLACK_CHANNEL, text=desc,
            username='JobBot', icon_emoji=':nerd_face:'
        )
