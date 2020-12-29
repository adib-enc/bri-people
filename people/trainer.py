import sys
# print(sys.executable)
import pandas as pd
import numpy as np
from patsy import dmatrices
import statsmodels.api as sm
import matplotlib.pyplot as plt
import time
"""
https://www.kaggle.com/c/bri-data-hackathon-people-analytic/rules

bri-data-hackathon-people-analytic
"""
class Trainer:
    test = 1
    def __init__(self):
        pass

    def overview1(self):
        df = pd.read_csv('data/train.csv', header=0)
        print(df.head(10))

def run():
    t = Trainer()
    t.overview1()