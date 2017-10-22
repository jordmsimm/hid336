import pandas as pd

def getHist(path):
    data = pd.read_csv(path, sep= " ")
    plot = data.hist()
    return plot

getHist('histdata.txt')
