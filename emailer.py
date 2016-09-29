import weather
import mailer

def get_emails():
    # Get list of all emails
    emails = {}

    try:
        email_file = open('emails.txt', 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
            
    except FileNotFoundError as err:
        print(err)
    return emails

def get_schedule():
    # Get the schedule
    try:
        schedule_file = open('schedule.txt', 'r')    

        schedule = schedule_file.read()

    except FileNotFoundError as err:
        print(err)

    return schedule

def main():
    # Main function
    emails = get_emails()
    schedule = get_schedule()
    forecast = weather.get_weather_forecast()
    mailer.send_emails(emails, schedule, forecast)

main()
