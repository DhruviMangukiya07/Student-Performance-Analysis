#  Student Performance Analysis
import pandas as pd
import seaborn  as sns
import matplotlib.pyplot as plt
data = {
    'Name':['Dhruvi','Rahul','Priya','Aman','Neha','Karan','Riya','Vishal','Sneha','Jay'],
    'Subject':['Python','SQL','Python','Excel','SQL','Power BI','Python','Excel','SQL','Power BI'],
    'Marks':[90,75,95,60,85,70,29,65,39,78],
    'Hours_Studied':[5,3,6,2,4,3,5,2,6,4]
}

df = pd.DataFrame(data)

print("80+ marks students:",df[df['Marks']>80])

print("Average Marks:",df['Marks'].mean())

print("Highest Marks student:",df.loc[df['Marks'].idxmax()])

print("Lowest Marks student:",df.loc[df['Marks'].idxmin()])

Subject_avg = df.groupby('Subject')['Marks'].mean()
print(Subject_avg)

df['Result'] = df['Marks'].apply(
 lambda x:'pass' 
 if x >= 40
 else 'fail'
)
print(df)

sns.barplot(x = 'Subject',y = 'Marks',data = df,color='yellow')
plt.title('Average marks by subject')
plt.show()

sns.countplot(x = 'Result',data = df)
plt.title('Pass vs Fail')
plt.show()

sns.scatterplot(x = 'Hours_Studied',y = 'Marks',data = df)
plt.title('Hours studied vs marks')
plt.show()

sns.histplot(df['Marks'],bins = 5,kde = True,color = 'pink')
plt.title('Distribution of marks')
plt.show()

corr = df[['Marks','Hours_Studied']].corr()
sns.heatmap(corr,annot = True,cmap = 'coolwarm')
plt.show()