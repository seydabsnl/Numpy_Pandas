import pandas as pd
import numpy as np

# 1- first 10 records
df = pd.read_csv("insurance.csv")
print(df.head(10))

# 2- Column names in Dataset
result = df.columns.value_counts()
print(result)

# 3- fetch the region and expenditure count of the first 50 records
result = df.head(50).loc[:,"region":"charges"]
print(result)

# 4- find the total average age
result = 0
for column in df["age"]:
    result = result + column
person = df.value_counts().sum()
age_mean = result / person
print(age_mean)

# 5- Find average of expenses by southwest region
sum_charges = 0
filter = df.loc[df['region'] == 'southwest']
sum_filter = filter.value_counts().sum()
for column in filter["charges"]:
    sum_charges = sum_charges + column
result = sum_charges / sum_filter
print(result)

# 6- Bring records of men who smoke and are over 45 years old
result = df[(df["age"] > 45) & (df["smoker"] == "yes") & (df["sex"] == "male")]
#print(result)

# 7- Find the average age of women who have insurance
result = df[(df["sex"] == "female")]
sum_result = result.value_counts().sum()
age_sum = 0
for age in result["age"]:
    age_sum = age_sum + age
result = age_sum / sum_result
print(result)

# 8- Bring your bmi over 30 and and smoker records.
result = df[(df["bmi"] > 30) & (df["smoker"] == "yes")]
#print(result)

# 9- Take the regions of records with bmi greater than 30 as the total number.
result = df[df["bmi"] > 30]
print(df["region"].unique()) # ['southwest' 'southeast' 'northwest' 'northeast']
result = result.value_counts("region").unique() # [243 171 148 143]
print(result)

# 10- delete some columns and list the remaining columns.
result = df.drop("age", axis="columns")
print(result)


















