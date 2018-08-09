#coding: utf-8

import pings #pip install pings
import post_slack

def ping_test():
    post_slack.send_alert("popopo")

if __name__ == "__main__":
    # hosts = ["google.com","yahoo.co.jp","square-enix.com"]
    ping_test()


