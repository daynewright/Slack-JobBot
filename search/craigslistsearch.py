from craigslist import CraigslistJobs
from datetime import datetime

def get_craigslist():
    cl = CraigslistJobs(site='nashville', category='sof',
                                filters={'posted_today': True })

    results = cl.get_results(sort_by='newest', limit=20)

    returnArray = []
    print("Checking for Craigslist Jobs...")
    if any(True for _ in results):
        jobCount = 0
        foundJobs = ":rocket: :rocket: *I found Craigslist jobs!* :rocket: :rocket:"
        returnArray.append(foundJobs)
        for result in results:
            if 'nashville' in result['url']:
                jobCount += 1
                datePosted = datetime.strptime(result["datetime"],'%Y-%m-%d %H:%M')
                desc = ":desktop_computer:  A new JOB was posted on *CraigsList*: \n>>> <{1}|{0}> Located in *{2}* \n Listed on *{3}*".format(result["name"], result["url"], result["where"], datePosted.strftime('%b %d at %I:%M %p'))
                returnArray.append(desc)
        print("Done checking Craigslist jobs and {0} new jobs added to slack.".format(jobCount))
    else:
        desc ="*No new jobs were added today on Craigslist.* :thumbsdown:"
        returnArray.append(desc)
        print("Done checking Craigslist jobs and none found.")

    return returnArray
