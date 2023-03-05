from app import db
from app.classes.message import Notification_Notifications
from datetime import datetime


# 1 New comment on message
# 2 tipped  a post with bitcoin
# 3 tipped a post with xmr
# 4 tipped a comment with btc
# 5 tipped a comment with xmr
# 6 user was made a mod of a sub
# 7 user was removed as mod of a sub
# 8 user was unbanned from a sub
# 9 user was invited to a sub
# 10 user was removed to a sub
# 11 user was muted from a sub
# 12 user was banned from a sub
# 13 user post was locked


def add_new_notification(thetypeofnote, user_id):

    now = datetime.utcnow()
    newnotification = Notification_Notifications(
                        timestamp=now,
                        read=0,
                        user_id=user_id,
                        subcommon_id=0,
                        subcommon_name='',
                        post_id=0,
                        comment_id=0,
                        msg_type=thetypeofnote,
                            )
    db.session.add(newnotification)

