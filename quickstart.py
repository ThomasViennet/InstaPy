import os
import time
import schedule
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = ''
insta_password = ''


# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

def job():
    try:
        session.login()

        # settings
        session.set_relationship_bounds(enabled=True,
    				 potency_ratio=-1.21,
    				  delimit_by_numbers=True,
    				   max_followers=4590,
    				    max_following=5555,
    				     min_followers=45,
    				      min_following=77)
        session.set_user_interact(amount=4, randomize=True, percentage=100)
        session.set_do_follow(enabled=True, percentage=100, times=2)
        session.set_do_like(enabled=True, percentage=100)
        session.set_do_comment(True, percentage=25)
        session.set_comments(['Je suis fan @{} !', 'Magnifique', 'Superbe', 'Top !', 'Ton compte instagram est vraiment top @{} !'])

        # actions
        session.interact_user_followers(['miaoubox'], amount=10, randomize=True)
        session.unfollow_users(amount=10, onlyInstapyFollowed = True, onlyInstapyMethod = 'FIFO', sleep_delay=600, unfollow_after=4*24*60*60)

    except Exception as exc:
        # if changes to IG layout, upload the file to help us locate the change
        if isinstance(exc, NoSuchElementException):
            file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
            with open(file_path, 'wb') as fp:
                fp.write(session.browser.page_source.encode('utf8'))
            print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
                '*' * 70, file_path))
        # full stacktrace when raising Github issue
        raise

    finally:
        # end the bot session
        session.end()

schedule.every().day.at("8:33").do(job)
schedule.every().day.at("9:41").do(job)
schedule.every().day.at("11:02").do(job)
schedule.every().day.at("12:17").do(job)
schedule.every().day.at("13:38").do(job)
schedule.every().day.at("16:30").do(job)
schedule.every().day.at("18:24").do(job)
schedule.every().day.at("19:46").do(job)
schedule.every().day.at("21:24").do(job)
schedule.every().day.at("22:55").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
