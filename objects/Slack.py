import slackweb
import time

class Slack:

    def __init__(self):
        self.slack = slackweb.Slack(url="https://hooks.slack.com/services/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")

    def notify(self,text):
        self.slack.notify(text=text)
