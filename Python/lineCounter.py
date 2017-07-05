import requests
import time

# only works with users with up to 100 repos
# hopefully when I have 100+ repos I will know how to properly do pagination

username = 'capalmer1013'

repos = requests.get('https://api.github.com/users/'+username+'/repos?per_page=100').json()

totalAdd = 0
totalSub = 0
for each in repos:
    repo_name = each ['name']
    time.sleep(5)
    repo_stats = requests.get('https://api.github.com/repos/'+username+'/'+repo_name+'/stats/contributors').json()
    for contrib in repo_stats:
        if contrib['author']['login'] == username:
            for week in contrib['weeks']:
                totalAdd += week['a']
                totalSub += week['d']

print "Total Additions", totalAdd
print "Total Deletions", totalSub