# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from builtins import open

from inscrawler import InsCrawler
import sys
import argparse
import json
from io import open


def usage():
    return '''
        python crawlerMain.py posts -u cal_foodie -n 100 -o ./output
        python crawlerMain.py posts_full -u cal_foodie -n 100 -o ./output
        python crawlerMain.py profile -u cal_foodie -o ./output
        python crawlerMain.py hashtag -t taiwan -o ./output

        The default number for fetching posts via hashtag is 100.
    '''


def get_posts_by_user(username, number, detail, debug):
    ins_crawler = InsCrawler(has_screen=debug)
    return ins_crawler.get_user_posts(username, number, detail)


def get_profile(username):
    ins_crawler = InsCrawler()
    return ins_crawler.get_user_profile(username)


def get_posts_by_hashtag(tag, number, debug):
    ins_crawler = InsCrawler(has_screen=debug)
    return ins_crawler.get_latest_posts_by_tag(tag, number)

def get_pull_posts_by_hashtag(tag, number):
    ins_crawler = InsCrawler()
    return ins_crawler.get_full_posts_by_tag(tag, number)



def output(data, filepath):
    out = json.dumps(data, ensure_ascii=False)
    if filepath:
        with open(filepath, 'w', encoding='utf8') as f:
            f.write(out)
    else:
        print(out)


if __name__ == '__main__':
    # result = get_posts_by_hashtag("love", None or 10, False)

    result2 = get_pull_posts_by_hashtag("댕스타그램", 10)
    print(result2)

    # output(result, "./output.json")


