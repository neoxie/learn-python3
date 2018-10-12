#!/usr/bin/env python3
from urllib.request import urlopen


def fetch_words():
    print('fetch_words invoked...')
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf8').split()
            for word in line_words:
                story_words.append(word)
    return story_words
