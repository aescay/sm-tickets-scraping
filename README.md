# sm-tickets-scraping
A quick-hacked way to send email alerts if tickets for an event you are eyeing have been released.

# Introduction and Some Disclaimers
I hacked this project within a couple of hours after my university, the University of the Philippines, made it to the finals of the University Athletic Association of the Philippines (UAAP) Men's Basketball Finals. The project's goal was to help my friends and I secure tickets for the finals games.

I tried to make it as clean as possible for other hobbyists to modify and use for their own ticketing or other alterting needs, but not developed enough for anyone to use as a tool - because as much as I want to contribute to the open source community, I don't want to significantly ruin my chances of securing tickets!

This is also my very first public contribution to open source programming, so I would love any feedback on how to improve my code, documentaion, or anything else regarding this repo.

# Packages
- beautifulsoup4
- lxml
- request
- smtplib
- logging

# How To Use
This repository has a python script, [uaap-scrape.py](https://github.com/aescay/sm-tickets-scraping/blob/master/uaap-scrape.py) which can scrape [SM Tickets](https://smtickets.com) and alert a mailing list via email once the tickets are made available! A log will also be made for you to monitor the status of the last run.

## Steps
1. Install the required packages listed above via pip or conda (I recommend conda to keep your python environments clean)
2. Edit the [passwords_sample.txt](https://github.com/aescay/sm-tickets-scraping/blob/master/passwords_sample.txt) file to reflect your user name and password for your email account. Rename the file to passwords.txt so that it can automatically be read by the script. I have also included this in the .gitignore file so there's no need to worry about accidentally pushing your login details on github if you properly save the file.
3. Edit the [mail_list_sample.txt](https://github.com/aescay/sm-tickets-scraping/blob/master/mail_list_sample.txt) file to include the emails you would like to send the alert to. Rename the file to mail_list.txt so that it can automatically be read by the script. Just like passwords.txt, I have also included this in the .gitignore file so there's no need to worry about accidentally pushing your login details on github if you properly save the file.
4. Run `python uaap-scrape.py`

## Automation Implementation
You may opt to run this script using *cron* in order to monitor it on a regular basis. I would leave that up to you to configure but it is relatively simple and there are many resources available to guide you with this process.  
  
I chose to implement this with *cron* and a *Raspberry pi 3* which searches every 5 seconds for any updates.

## Modifying the Script for Other Use Cases
I chose to leave this relatively challenging so that I don't hurt my chances of securing a ticket, but there are a few parameters that can be easily altered:  
1. *Email Subject* This will change the subject of the Email that is sent
2. *URL* This will change the page to be searched

Once you configure these it should be good to go. As long as you use any search site of SM Tickets, this should work without the need for any modification (ex. Site looks like: https://smtickets.com/events/search/[enter_event_here])
  
If you choose to do something different from just checking if tickets for an event have been posted, you would need to modify more of the main script. Would be happy to help if you hit me up with a message!
