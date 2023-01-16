import re
import difflib
from collections import Counter
from setup import stop_words
from constants import OFFICIAL_AWARDS_1315, OFFICIAL_AWARDS_1819

sub_links = re.compile(r'http(s)?\:\/\/[\w\.\d]*\b')
sub_hashtag = re.compile(r'#')
sub_tags = re.compile(r'@[^ ]*\b')
sub_numbers = re.compile(r'\b\d+\b')
sub_punctuation = re.compile(r'[^\w\d\s]+')
sub_splitter = re.compile("([a-z])([A-Z])")
sub_spaces = re.compile(r'\s+')
#sub_gg = re.compile(r'[Gg]olden\s[Gg]lobe[s]?')

def get_awardname_tokens(year):
    award_list = get_awards_list(year)
    award_token_dict = {}
    for award in award_list:
        award_ = clean_tweet(award)
        award_token = [word for word in award_.split() if word.lower() not in stop_words]
        award_token_dict[award] = " ".join(award_token)
    
    return award_token_dict


def segregate_tweets_by_awardname(keyword, tweets, year):
    award_list = get_awards_list(year)
    award_token_dict = get_awardname_tokens(year)

    tweet_dict_by_award = {}

    for tweet in tweets:
        if not  set(tweet.lower().split()).intersection(keyword):
            continue

        category = award_classifier(tweet, award_list, award_token_dict)

        if category:
            if category not in tweet_dict_by_award:
                tweet_dict_by_award[category] = []
            tweet_dict_by_award[category].append(tweet)

    return tweet_dict_by_award

def get_awards_list(year):
    award_list = OFFICIAL_AWARDS_1315.copy()
    if year in ["2018", "2019"]:
        award_list = OFFICIAL_AWARDS_1819.copy()
    return award_list

def award_classifier(tweet, award_categories, token_dict):
    best_score = 0
    best_category = ""
    for award in award_categories:
        score = string_similarity(tweet, token_dict[award])
        if score > best_score:
            best_score = score
            best_category = award
    return best_category

def string_similarity(str1, str2):
    result =  difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
    return result.ratio()

def clean_tweet(tweet):
        # Remove all links hashtags and other things that are not words
        #tweet = re.sub("[rR][tT]",'', tweet)
        tweet = str(tweet)
        # tweet = tweet.replace('#', '')
        # tweet = tweet.replace('@', '')
        tweet = tweet.replace(' rt ', '')
        tweet = tweet.replace(' RT ', '')
        tweet = sub_links.sub(' ', tweet)
        tweet = sub_hashtag.sub('', tweet)
        tweet = sub_tags.sub('', tweet)
        tweet = sub_numbers.sub('', tweet)
        tweet = sub_punctuation.sub(' ', tweet)
        tweet = sub_splitter.sub(r'\1 \2', tweet)
        tweet = sub_spaces.sub(' ', tweet)
        tweet = tweet.lstrip(' ')
        #tweet = re.sub(r"(\srt\s|\sRT\s)",'', tweet)
        tweet = tweet.replace('television', 'tv')
        tweet = tweet.replace(' mp ', 'motion picture')
        #tweet = sub_gg.sub('', tweet)
        #tweet = tweet.replace('movie', 'picture')
        tweet = tweet.replace('mini-series', 'mini series')
        tweet = tweet.replace('miniseries', 'mini series')
        return tweet

