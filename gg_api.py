'''Version 0.35'''
from awards_and_winners import get_awards_winners
from nominations import get_nominee_award
from presenter import getPresenters
from utils import clean_tweet
from hosts import get_host_names
import json

OFFICIAL_AWARDS_1315 = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']
OFFICIAL_AWARDS_1819 = ['best motion picture - drama', 'best motion picture - musical or comedy', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best performance by an actress in a motion picture - musical or comedy', 'best performance by an actor in a motion picture - musical or comedy', 'best performance by an actress in a supporting role in any motion picture', 'best performance by an actor in a supporting role in any motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best motion picture - animated', 'best motion picture - foreign language', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best television series - musical or comedy', 'best television limited series or motion picture made for television', 'best performance by an actress in a limited series or a motion picture made for television', 'best performance by an actor in a limited series or a motion picture made for television', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best performance by an actress in a television series - musical or comedy', 'best performance by an actor in a television series - musical or comedy', 'best performance by an actress in a supporting role in a series, limited series or motion picture made for television', 'best performance by an actor in a supporting role in a series, limited series or motion picture made for television', 'cecil b. demille award']

global all_tweets
all_tweets = {}
global cleaned_tweets
cleaned_tweets = {}
global year

def set_tweets(year):
    tweet_data = ""
    flag = True
    while flag == True:
        year = input("Enter the year of awards you want to process: ")
        file_name = "gg" + year + ".json"
        if year in ["2015", "2013", "2018", "2019"]:
            flag = False
        else:
            print("Year not in 2013, 2015, 2018 or 2019, kindly retry! ")

    with open(file_name) as f:
        all_tweets[year] = json.load(f)

    cleaned_tweets[year] = [clean_tweet(tweet['text']) for tweet in all_tweets]

def get_tweets(year):
    if year in all_tweets:
        return cleaned_tweets[year]

    set_tweets(year)
    return cleaned_tweets[year]
    

def get_hosts(year):
    '''Hosts is a list of one or more strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    tweets = get_tweets(year)
    return get_host_names(tweets)

def get_awards(year):
    '''Awards is a list of strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    tweets = get_tweets(year)
    return get_awards_winners(tweets)

def get_nominees(year):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''
    # Your code here
    tweets = get_tweets(year)
    return get_nominee_award(tweets,year)

def get_winner(year):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    tweets = get_tweets(year)
    return get_awards_winners(tweets)

def get_presenters(year):
    '''Presenters is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change the
    name of this function or what it returns.'''
    # Your code here
    tweets = get_tweets(year)
    return getPresenters(tweets, year)

def pre_ceremony():
    '''This function loads/fetches/processes any data your program
    will use, and stores that data in your DB or in a json, csv, or
    plain text file. It is the first thing the TA will run when grading.
    Do NOT change the name of this function or what it returns.'''
    # Your code here 
    print("Pre-ceremony processing complete.")
    return

def write_json():
    write_dict = {}

    hosts = get_hosts(year)
    awards = get_awards(year)
    nominees = get_nominees(year)
    presenters = get_presenters(year)

    write_dict["hosts"] = hosts
    write_dict["award_data"] = {}
    for key in awards:
        if key not in write_dict["award_data"]:
            write_dict["award_data"][key] = {}
        write_dict["award_data"][key]["winner"] = list(awards[key])
    for key in presenters:
        if key not in write_dict["award_data"]:
            write_dict["award_data"][key] = {}
        write_dict["award_data"][key]["presenter"] = list(presenters[key])

    for key in nominees:
        if key not in write_dict["award_data"]:
            write_dict["award_data"][key] = {}
        write_dict["award_data"][key]["nominee"] = list(nominees[key])
    with open("gg"+year+"answers_gen.json", "w") as f:
        json.dump(write_dict,f,indent=4)
    return

def main():
    '''This function calls your program. Typing "python gg_api.py"
    will run this function. Or, in the interpreter, import gg_api
    and then run gg_api.main(). This is the second thing the TA will
    run when grading. Do NOT change the name of this function or
    what it returns.'''
    # Your code here  
    pre_ceremony()
    write_json()
    return

if __name__ == '__main__':
    main()
