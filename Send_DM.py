from instagrapi import Client
from myInfo import my_password, my_username, receiver_username, message, time


# log in to your Instagram account
api = Client()
api.login(my_username, my_password) # if this line throws an error, then either your login info is wrong, OR instagram policies were triggered because you logged in too many times. If so, you need to manually login to your account and verify the account to proceed
print('Logged in successfully!')

# search for the receiver's user by username
user = api.search_users(receiver_username)


from datetime import datetime
from time import sleep
def send_message(message, user_id):
    while True:
        now = datetime.now()
        if [now.hour, now.minute] == time:
            api.direct_send(message, [user_id])
            print('Message sent successfully!')
        sleep(60)  # check the time every minute


if user:    # if receiver's user is found
    send_message(message, user[0].pk) # user[0].pk = user_id
else:
    print(f"No search results found for username '{receiver_username}'")

# log out of your Instagram account
api.logout()
