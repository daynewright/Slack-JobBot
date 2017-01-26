import requests
from datetime import datetime, date, timedelta

def get_dice():
    response = requests.get("http://service.dice.com/api/rest/jobsearch/v1/simple.json?text=junior+software+developer&age=1&state=TN&city=37115")
    results = response.json()
    returnArray = []
    print("Checking for Dice Jobs...")
    if any(True for _ in results):
        jobCount = 0
        foundJobs = ":rocket: :rocket: *I found Dice jobs!* :rocket: :rocket:"
        returnArray.append(foundJobs)
        for result in results['resultItemList']:
            if 'CyberCoders' not in result['company'] and 'Robert Half' not in result['company'] and 'TEKsystems' not in result['company'] and 'Vaco' not in result['company'] and 'V-Soft' not in result['company'] and 'Staffing' not in result['company']:
                datePosted = datetime.strptime(result["date"],'%Y-%m-%d').strftime('%b %d')
                todayDate = (date.today()).strftime('%b %d')
                if datePosted == todayDate:
                    jobCount += 1
                    desc = ":game_die: A new job was found on *Dice*: \n>>>  <{0}|{1}> Located in *{3}* at *{2}* \n Posted on *{4}*".format(result["detailUrl"], result["jobTitle"], result["company"], result["location"], datePosted)
                    returnArray.append(desc)
        print("Done checking Dice jobs and {0} new jobs added to slack.".format(jobCount))
    else:
        desc = "*No new jobs were added today on Dice* :thumbs_down:"
        returnArray.append(desc)
        print("Done checking Dice jobs and new jobs added to slack.")
    return returnArray