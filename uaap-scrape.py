from bs4 import BeautifulSoup
import requests
import smtplib
import logging

SUBJECT = 'FINALS TICKETS ARE OUT!'
URL = 'https://smtickets.com/events/search/uaap'

def get_credentials():
    credentials = {}
    with open('passwords.txt') as f:
        for x in f.readlines():
            entry = x.strip().split(':')
            credentials[entry[0]] = entry[1]
    return credentials

def get_mail_list():
    with open('mail_list.txt') as f:
        mail_list = [x.strip().split(', ') for x in f.readlines()][0]
    return mail_list
        
def setup_logging():
    logging.basicConfig(filename='scrape.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

def main(url ,subject):
    credentials = get_credentials()
    mail_list = get_mail_list()
    setup_logging()
    # launch url
    url = url
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        body = soup.find('tbody')
        event = body.find('strong')
    except Exception:
        logging.info('Failed to scrape')

    try:
        game = event.contents[0]
        link = body.find('a')['href']
        tickets = 'yes'
    except Exception:
        logging.info('No Tickets Yet')
        tickets = 'no'

    if tickets == 'yes':
        try:
            gmail_user = credentials['username']
            gmail_password = credentials['password']
            sent_from = gmail_user
            to = mail_list
            subject = subject
            msg_body = game, link
            message = """From: From Person %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, to, subject, msg_body)
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, message)
            server.close()
            logging.info('Email sent!')
        except Exception:
            logging.info('Something went wrong...')

def check_logger():
    try:
        infile = r"scrape.log"
        important = []
        keep_phrases = ["Email sent!"]
        with open(infile) as f:
            f = f.readlines()
        for line in f:
            for phrase in keep_phrases:
                if phrase in line:
                    important.append(line)
                    break
        if len(important) > 0:
            return "Stop"
        else:
            return "Go"
    except Exception:
        return "Go"

if __name__ == '__main__':
    status = check_logger()
    if status == "Go":
        main(URL, SUBJECT)
