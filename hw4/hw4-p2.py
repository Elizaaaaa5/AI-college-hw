
state = {
    "horses": ['h1', 'h2', 'h3'],
    "features": dict(h1=[1, 2], h2=[0.5, 2], h3=[1, 3]),
    "outcomes": dict(h1=-1, h2=0, h3=2),
    "bet": dict(h1=-1, h2=50, h3=100)
}
# In this problem, your bot will be betting on horse races alongside everybody else’s in the class.
# You will be writing a function “bet(state)”, which takes in a state dictionary (giving you both info
# about the current bet, and the previous round’s results) and returns an ordered pair – (horse-name,
# bet-amount).

import pickle
import logging
import numpy as np
from sklearn.svm import SVR

def bet(state):
    horses = state['horses']
    features = state['features']
    outcomes = state['outcomes']
    bets = state['bets']
    print(horses, features, outcomes, bets)
    clf = SVR(C=1.0, epsilon=0.1, cache_size=1000)

bet(state)

