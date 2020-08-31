import seaborn as sns
sns.lineplot(x="Fare",y="Age",hue="Survived",data=df)
