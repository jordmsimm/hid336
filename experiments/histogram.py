import pandas as pd

def getHist(path):
    data = pd.read_csv(path, sep= " ")
    counts = pd.value_counts(data['Student_Data'])
    plot = counts.plot(kind='bar', title='Time Student Spent On Corections')
    plot.set_xlabel('Time spent for corrections')
    plot.set_ylabel('NUmber of students')
    return plot

getHist('histdata.txt')
