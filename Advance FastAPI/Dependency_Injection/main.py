import pandas as pd

data =[{
    'id':[1,2],
    'name':['Priyanshu Tiwari','Hanuman'],
    'Course':['B.Tech','MTech'],
    'branch':['CSE','ECE'],
    'sem':['7th','3rd']

},{
    'id':[1,2],
    'name':['Priyanshu Tiwari','Hanuman'],
    'Course':['B.Tech','MTech'],
    'branch':['CSE','ECE'],
    'sem':['7th','3rd']

}
]

df=pd.DataFrame(data)
print(df)