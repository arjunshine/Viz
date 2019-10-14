# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 07:32:20 2019

@author: Arjun
"""

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
# Loading the data
hrdata = pd.read_csv("C:/Users/Arjun/Downloads/ibm-hr-analytics-employee-attrition-performance/WA_Fn-UseC_-HR-Employee-Attrition.csv", header=0)
# describe the data
hrdata.describe()
#print the top 5 rows in the dataframe 
hrdata.head()
#print first 7 rows 
hrdata.head(7)
#print the last 5 rows in the dataframe 
hrdata.tail()
#print index
hrdata.index
#print datatype of all variables 
hrdata.dtypes
#return column names 
hrdata.columns 
hrdata.values 



#bin the data in yearsatcompany into 5 bins 
#3 new columns are created after binning the data 
hrdata['CmpYrInterval'] = pd.cut(hrdata['YearsAtCompany'], 
      5,
      labels=['<9', '<15', '<24', '<32', '<33+'])

hrdata['RateLvl'] = pd.cut(hrdata['DailyRate'],
      5,
      labels=['lvl1', 'lvl2', 'lvl3', 'lvl4', 'lvl5'])
hrdata['PromoYrLvl'] = pd.cut(hrdata['YearsSinceLastPromotion'], 
      5, 
      labels=['0to3', '3to6', '6to9', '9to12', '12+'])


#creating dummy variables 
hrdata['Gender_num'] = pd.get_dummies(hrdata.Gender, drop_first = True)

hrdata['Attrition_num'] = pd.get_dummies(hrdata.Attrition, drop_first = True)

#seperate the dataset into attrition yes and no 
attr_yes = hrdata[hrdata.Attrition=='Yes']
attr_no=hrdata[hrdata.Attrition=='No']


#extra feature histogram
hrdata.hist(figsize=(40,40))
plt.show()
#plotting
hrdata.plot(kind='density',subplots=True,layout=(9,5),sharex=False)
fig, ax1 = plt.subplots(1,2, figsize=(16,4))
attr_yes = hrdata[hrdata.Attrition=='Yes']
sb.distplot(hrdata.Age, ax = ax1[0])
sb.distplot(attr_yes.Age, ax = ax1[1])
plt.ylabel('Attrition = Yes')
plt.show()



total=hrdata.shape[0] #return the number of rows
hrfig = sb.countplot(x='Education', hue = 'Attrition', data = hrdata)
#used to display the values and format the text 
for p in hrfig.patches:
    height = p.get_height()
    hrfig.text(p.get_x()+p.get_width()/2.,
            height+3,
            '{:1.2f}'.format(height*100/total),
            ha="center") 
plt.show()





fig, ax6 = plt.subplots(1,2, figsize=(24,6)) #creates the grid od subplots 
#creats first plot with department and gender 
sb.countplot(x='Department', hue='Gender', data = attr_yes, ax = ax6[1])
sb.countplot(y='JobRole', hue='Gender', data = attr_yes, ax = ax6[0])
plt.show()


#creating subplot to understand trhe relation of marital status and attrition
sb.countplot(x='Attrition', hue='MaritalStatus', data=hrdata)
plt.show()




fig, ax2 = plt.subplots(2,2, figsize=(10,10))
sb.countplot(x='RateLvl', data=attr_yes, ax = ax2[0,0])
sb.countplot(x='CmpYrInterval', data=attr_yes, ax = ax2[0,1])
sb.countplot(x='PromoYrLvl', data=attr_yes, ax = ax2[1,0])
sb.countplot(x='StockOptionLevel', data=attr_yes, ax = ax2[1,1])
plt.show()





#boxplots for distance from home ,percentsalaryhike,numcompaniesworked,monthlyrate

fig, ax4 = plt.subplots(2,2, figsize=(10,10))
sb.boxplot(x='Attrition', y='DistanceFromHome', data=hrdata, ax = ax4[0,0])
sb.boxplot(x='Attrition', y='PercentSalaryHike', data=hrdata, ax = ax4[0,1])
sb.boxplot(x='Attrition', y='NumCompaniesWorked', data=hrdata, ax = ax4[1,0])
sb.boxplot(x='Attrition', y='MonthlyRate', data=hrdata, ax = ax4[1,1])

plt.show()



sb.barplot(y='JobRole', x = 'Gender_num', data = attr_yes)
#changes to the presented graph
fig, ax4 = plt.subplots(1,1, figsize=(20,20))
sb.barplot(y='Gender_num', x ='JobRole', data = attr_yes)






# each variable in data will by shared in the y-axis across a single row 
#and in the x-axis across a single column
#kind is used to specify the kind of graph for non identity relation
#diag_kind is used to specify the kind of graph for the diagonal relations
cont_col= ['Attrition', 'Age', 'DistanceFromHome','MonthlyRate','NumCompaniesWorked', 'StockOptionLevel']
sb.pairplot(hrdata[cont_col], kind="reg", diag_kind = "auto", hue = 'Attrition')
plt.show()




sb.jointplot(x='Attrition_num', y='YearsAtCompany', data=hrdata, kind="reg")
#extra feature 
#hexagon representing the density 
sb.jointplot(x='Attrition_num', y='YearsAtCompany', data=hrdata, kind="hex")
sb.jointplot(x='Age', y='MonthlyRate', data=hrdata, kind="kde")
plt.show()





sb.factorplot(x =   'Attrition',     # Categorical
               y =   'Age',          # Continuous
               hue = 'Department',   # Categorical
               col = 'CmpYrInterval',   # Categorical for graph columns
               col_wrap=1,           # 1 will be displayed in each row
               kind = 'box',
               data = hrdata)
plt.show()


#extra feature added size and legend  
sb.factorplot(x =   'Attrition',     # Categorical
               y =   'Age',          # Continuous
               hue = 'Department',   # Categorical
               col = 'CmpYrInterval',   # Categorical for graph columns
               col_wrap=1,           # 1 will be displayed in each row
               kind = 'bar',#can be set as bar,violin,box,
               data = hrdata,
               legend = True,
               size=6)



sb.factorplot(x =   'Attrition',     # Categorical
               y =   'Age',          # Continuous
               hue = 'Department',   # Categorical
               col = 'MaritalStatus',   # Categorical for graph columns
               col_wrap=2,           # Wrap facet after two axes
               kind = 'box',
               data = hrdata)




#extra feature 
hrdata.plot(kind='scatter', x='Age', y='DailyRate',alpha = 0.5,color = 'red')
plt.xlabel('Age', fontsize=16)              # label = name of label
plt.ylabel('DailyRate', fontsize=16)
plt.title('Age vs DailyRate Scatter Plot', fontsize=20)  

#devide the data into the bins 
hrdata.TotalWorkingYears.plot(kind = 'hist',bins = 5,figsize = (15,15))


sb.boxplot(hrdata['Gender'], hrdata['MonthlyIncome'])
plt.title('MonthlyIncome vs Gender Box Plot', fontsize=20)      
plt.xlabel('MonthlyIncome', fontsize=16)
plt.ylabel('Gender', fontsize=16)
plt.show()



sb.countplot(hrdata.JobLevel)
plt.title('JobLevel Count Plot', fontsize=20)      
plt.xlabel('JobLevel', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.show()


#pie chart 

labels = ['Male', 'Female']
hrdata['Gender'].value_counts()[0]
sizes = [hrdata['Gender'].value_counts()[0],
         hrdata['Gender'].value_counts()[1]
        ]
fig1, ax1 = plt.subplots()
#ratio between the center of each pie slice and the start of the text generated by autopct
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',pctdistance = 0.4, shadow=False) 
ax1.axis('equal')
plt.title('Gender Pie Chart', fontsize=20)
plt.show()


#used to plot the correlation between different factors 
f,ax = plt.subplots(figsize=(18, 18))
sb.heatmap(hrdata.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)



