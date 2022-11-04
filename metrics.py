import copy

import tweepy


class Metrics:
    """
    Class for getting all the metrics for the first version
    """

    def __init__(self, dms):
        self.dms = dms

    def outbound_messages_reply_rate(self):
        sent = set()
        responded = set()

        dms = self.dms
        temp_responded = copy.copy(dms.responded)
        for id in dms.responded:
            if id not in dms.sent:
                temp_responded.remove(id)

        omrr = 0 if len(dms.sent) == 0 else len(responded) / len(dms.sent)
        metric = {
            "sent": len(dms.sent),
            "sent_user_ids": list(dms.sent),
            "responses": len(responded),
            "responded_user_ids": list(responded),
            "metric": round(omrr, 4),
        }

        return metric


class DM:
    """
    Class for getting all a user's dms in one sweep
    """

    def __init__(self, auth):
        self.count = 200
        self.sent = set()
        self.responded = set()
        self.tweets_with_button = dict()
        self.v1_user = tweepy.API(auth, wait_on_rate_limit=True)
        self.get_dms()

    def get_dms(self):
        user_id = self.v1_user.verify_credentials().id

        dms = tweepy.Cursor(self.v1_user.get_direct_messages, count=self.count).items()
        for dm in dms:
            recipient_id = dm.message_create["target"]["recipient_id"]

            if recipient_id != str(user_id):
                self.sent.add(recipient_id)

                try:
                    # In case there is no initiated_via object
                    # welcome_message_id = dm.initiated_via.get("welcome_message_id", None)
                    tweet_id = dm.initiated_via.get("tweet_id", None)
                    if tweet_id:
                        self.tweet_ids_with_button[str(tweet_id)] += 1
                except:
                    pass

            if recipient_id == str(user_id):
                sender = dm.message_create["sender_id"]
                self.responded.add(sender)
