import pandas as pd
f=pd.read_csv("telecom_churn.csv")
print(f['Total day calls'].mean())   #3 среднее число звонков

print(f[f["State"] == "LA"]['Total day calls'].mean())  # 4 среднее для штата

b=f.groupby("State")["Total day calls"].mean()
print(b)   # 5 среднее число звонков для каждого штата

sr = f.loc[:, ["Total day calls"]].mean()[0]
print(f[f["Total day calls"] > sr]) # 6 кол-во звонков больше среднего

a=f.groupby(["State"]).agg({"Total day calls": "mean","Total eve calls":"mean"})
print(a) # 7

a['T/F']=a["Total day calls"]>a["Total eve calls"]
print(a) #8

a = f[(f["International plan"] == "Yes") & (f["Voice mail plan"] == "Yes")]
print(a.shape[0]/f.shape[0]) #9

print(f["Area code"].nunique()) #10

e = f.groupby(["Customer service calls"]).agg({"Total day minutes": "count"})
print(e) #11

print(f.loc[:, ["Total intl minutes"]].mean()) #13

print(f.loc[[100, 102, 104], ["State", "Churn"]]) #18

s = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})
s["C"] = s["A"].apply(lambda x: x ** 2) + s["B"].apply(lambda x: x ** 2)
print(s) #19

s["D"] = s[["A", "B", "C"]].apply(lambda x: x.mean(), axis=1)
print(s) #20





