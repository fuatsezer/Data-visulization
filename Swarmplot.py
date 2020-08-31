import seaborn as sns
sns.swarmplot(x="Fare",y="Age",hue="Survived",data=df)

