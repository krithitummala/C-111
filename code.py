import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["Math_score"].tolist()
fig = ff.create_distplot([data],["Math score"], show_hist= False)
#fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("The population mean is", mean)
print("The population standard deviation is", std_deviation)

def randomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(1,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

meanList = []
for i in range(0,1000):
    setOfMeans = randomSetOfMean(100)
    meanList.append(setOfMeans)

sampleMean = statistics.mean(meanList)
sampleStd_deviation = statistics.stdev(meanList)
print("The sample mean is", sampleMean)
print("The sample standard deviation is", sampleStd_deviation)

fig = ff.create_distplot([meanList], ["Math Marks"], show_hist= False)
fig.add_trace(go.Scatter(x = [sampleMean,sampleMean], y = [0,0.20], mode = "lines", name = "mean"))

stdStart, stdEnd = sampleMean - sampleStd_deviation, sampleMean + sampleStd_deviation
std2Start, std2End = sampleMean - (2*sampleStd_deviation), sampleMean + (2*sampleStd_deviation)
std3Start, std3End = sampleMean - (3*sampleStd_deviation), sampleMean + (3*sampleStd_deviation)

fig.add_trace(go.Scatter(x = [stdStart,stdStart], y = [0,0.20], mode = "lines", name = "std start"))
fig.add_trace(go.Scatter(x = [stdEnd,stdEnd], y = [0,0.20], mode = "lines", name = "std end"))
fig.add_trace(go.Scatter(x = [std2Start, std2Start], y = [0,0.20], mode = "lines", name = "std 2 start"))
fig.add_trace(go.Scatter(x = [std2End, std2End], y = [0,0.20], mode = "lines", name = "std 2 end"))
fig.add_trace(go.Scatter(x = [std3Start,std3Start], y = [0,0.20], mode = "lines", name = "std 3 start"))
fig.add_trace(go.Scatter(x = [std3End,std3End], y = [0,0.20], mode = "lines", name = "std 3 end"))
#fig.show()

df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()

meanOfSample1 = statistics.mean(data)
print("The mean of sample 1 is", meanOfSample1)
fig = ff.create_distplot([meanList],["student marks"], show_hist= False)
fig.add_trace(go.Scatter(x = [sampleMean,sampleMean], y = [0,0.20], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [meanOfSample1,meanOfSample1], y = [0,0.20], mode = "lines", name = "mean of sample 1"))
fig.add_trace(go.Scatter(x = [stdEnd,stdEnd], y = [0,0.20], mode = "lines", name = "std end"))
fig.show()

df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()

meanOfSample1 = statistics.mean(data)
print("The mean of sample 1 is", meanOfSample1)
fig = ff.create_distplot([meanList],["student marks"], show_hist= False)
fig.add_trace(go.Scatter(x = [sampleMean,sampleMean], y = [0,0.20], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [meanOfSample1,meanOfSample1], y = [0,0.20], mode = "lines", name = "mean of sample 1"))
fig.add_trace(go.Scatter(x = [stdEnd,stdEnd], y = [0,0.20], mode = "lines", name = "std end"))


df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()

meanOfSample2 = statistics.mean(data)
print("The mean of sample 1 is", meanOfSample1)
fig = ff.create_distplot([meanList],["student marks"], show_hist= False)
fig.add_trace(go.Scatter(x = [sampleMean,sampleMean], y = [0,0.20], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [meanOfSample2,meanOfSample2], y = [0,0.20], mode = "lines", name = "mean of sample 1"))
fig.add_trace(go.Scatter(x = [stdEnd,stdEnd], y = [0,0.20], mode = "lines", name = "std end"))
fig.add_trace(go.Scatter(x = [std2End, std2End], y = [0,0.20], mode = "lines", name = "std 2 end"))
fig.show()

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()

meanOfSample3 = statistics.mean(data)
print("The mean of sample 1 is", meanOfSample1)
fig = ff.create_distplot([meanList],["student marks"], show_hist= False)
fig.add_trace(go.Scatter(x = [sampleMean,sampleMean], y = [0,0.20], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [meanOfSample3,meanOfSample3], y = [0,0.20], mode = "lines", name = "mean of sample 1"))
fig.add_trace(go.Scatter(x = [stdEnd,stdEnd], y = [0,0.20], mode = "lines", name = "std end"))
fig.add_trace(go.Scatter(x = [std2End, std2End], y = [0,0.20], mode = "lines", name = "std 2 end"))
fig.add_trace(go.Scatter(x = [std3End,std3End], y = [0,0.20], mode = "lines", name = "std 3 end"))
fig.show()