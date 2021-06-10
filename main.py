import plotly.figure_factory as ff
import pandas
import statistics
# read csv
df= pandas.read_csv("data.csv")

# finding mean,median,mode of the height
height=df["Height(Inches)"].tolist()
mean=statistics.mean(height)
mode=statistics.mode(height)
median=statistics.median(height)

# calculating std _deviation
std_deviation=statistics.stdev(height)

#printing mean.median.mode.std_deviation
print("Mean of height of students:",mean)
print("Median of height of students:",median)
print("Mode of height of students:",mode)
print("Standard Deviation of height of students:",std_deviation)
# plot the graph
#figure=ff.create_distplot([height],["height of students"])
#figure.show()
# finding the first std deviation
upper_limit=mean+std_deviation
lower_limit=mean-std_deviation
print (upper_limit,lower_limit)
#run a loop on height if the height lies betwween upper_limit and lower_limit
list1=[]
for i in height:
    if lower_limit<i<upper_limit:
        list1.append(i)

per1=(len(list1)/len(height))*100   
print("percentage of data lying in 1 st std deviation:", per1) 

# finding 2 nd std deviation
upper_limit=mean+2*std_deviation
lower_limit=mean-2*std_deviation
print (upper_limit,lower_limit)
#run a loop on height if the height lies betwween upper_limit and lower_limit
list2=[]
for i in height:
    if lower_limit<i<upper_limit:
        list2.append(i)

per2=(len(list2)/len(height))*100   
print("percentage of data lying in 2st std deviation:", per2) 

# finding 3 nd std deviation
upper_limit=mean+3*std_deviation
lower_limit=mean-3*std_deviation
print (upper_limit,lower_limit)
#run a loop on height if the height lies betwween upper_limit and lower_limit
list3=[]
for i in height:
    if lower_limit<i<upper_limit:
        list3.append(i)

per3=(len(list3)/len(height))*100   
print("percentage of data lying in 3 rd std deviation:", per3) 

