import json, sys
import pandas as pd
from pandas import DataFrame

def main(self, file, user_id):
    self.file = sys.argv[1]
    self.user_id = sys.argv[2]

def analysis(file, user_id):
    times = 0
    minutes = 0
#    file = sys.argv[1]
#    file = '/home/shiyanlou/Code/user_study.json'
#    user_id = 199071
#    user_id = sys.argv[2]
    df = pd.read_json(file)
    minute = df[df['user_id'] == user_id].minutes
    times = minute.count()
    minutes = minute.sum()

    return times, minutes

