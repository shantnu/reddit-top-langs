#!/usr/bin/python

import praw
import pdb
import pandas as pd
import matplotlib.pyplot as plt

language_list = ['c_language', 'cpp', 'csharp', 'objectivec', 'd_language', 'java', 'smalltalk', 'golang', 'scala', 'groovy', 'delphi', 'python', 'ruby', 'perl', 'Tcl', 'lua', 'php', 'javascript', 'fsharp', 'haskell', 'ocaml', 'lisp', 'scheme', 'erlang', 'matlab', 'brainfuck', 'cobol', 'fortran', 'visualbasic']
framework_list = ['laravel', 'django', 'rails', 'drupal', 'dotnet', 'angularjs', 'emberjs', 'node', 'flask', 'codeigniter']

user_agent = ("PyEng Bot 0.1")

r = praw.Reddit(user_agent = user_agent)

red_score = {}
for language in language_list:
    #print language, ":", int(r.get_subreddit(language).subscribers)
    #print language
    red_score[language] = int(r.get_subreddit(language).subscribers)

print red_score

#red_score={'fsharp': 1721, 'golang': 12375, 'pascal': 256, 'haskell': 18624, 'brainfuck': 118, 'csharp': 17433, 'smalltalk': 798, 'java': 37273, 'common_lisp': 971, 'scala': 7271, 'delphi': 592, 'perl': 8957, 'lua': 3397, 'matlab': 6895, 'objectivec': 4043, 'scheme': 3309, 'python': 88443, 'javascript': 57804, 'php': 33976, 'ruby': 26411, 'groovy': 1125, 'erlang': 4051, 'visualbasic': 1822, 'lisp': 9518, 'ocaml': 2094, 'd_language': 1581, 'Tcl': 519, 'fortran': 834, 'cpp': 25295, 'cobol': 342, 'c_language': 2975}

column_names =  ['Language', 'num_subscribers']


red_panda = pd.DataFrame(red_score.items(), columns=column_names)

red_panda.set_index("Language", inplace=True)

print red_panda.sort("num_subscribers")[:10]
print red_panda.sort("num_subscribers", ascending=False)[:10]

red_panda.sort("num_subscribers")[:10].plot(kind='bar', title = "The least popular languages on Reddit")

#pdb.set_trace()

plt.tight_layout()

plt.show()

red_panda.sort("num_subscribers", ascending=False)[:10].plot(kind='bar', title = "The most popular languages on Reddit")

plt.tight_layout()

plt.show()

top_five =  red_panda.sort("num_subscribers", ascending=False)[:5]

avg_n = float(top_five.sum())

top_five['percent'] = (top_five['num_subscribers'] * 100) / avg_n
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'lightcyan']
explode = (0.1, 0, 0, 0, 0) # only "explode" the 2nd slice (i.red_panda. 'Hogs')
top_five['percent'].plot(kind="pie",autopct='%1.1f%%', shadow=True, colors = colors, explode=explode, startangle=90, title = "The Top 5 languages on Reddit")

plt.show()


######### Part 2

plt.close()

red_score_framework = {}
for framework in framework_list:
    #print language, ":", int(r.get_subreddit(language).subscribers)
    red_score_framework[framework] = int(r.get_subreddit(framework).subscribers)
print red_score_framework

#red_score_framework = {'laravel': 3661, 'node': 11362, 'codeigniter': 825, 'emberjs': 1620, 'drupal': 5298, 'rails': 12383, 'django': 12164, 'flask': 3647, 'angularjs': 9010, 'dotnet': 10441}

column_names =  ['Framework', 'num_subscribers']


red_panda = pd.DataFrame(red_score_framework.items(), columns=column_names)

red_panda.set_index("Framework", inplace=True)

red_panda.sort("num_subscribers", ascending=False)[:10].plot(kind='bar', title = "The most popular Web frameworks on Reddit")

plt.tight_layout()

plt.show()