# PANDAS
"""
Referanslar:
https://sparkbyexamples.com/pandas/pandas-combine-two-series-into-dataframe/
https://www.sadikturan.com/python-fonksiyonlar/python-lambda-fonksiyonu/1394
https://www.btkakademi.gov.tr
"""

import pandas as pd
import numpy as np
# Series([], dtype: float64) -varsayılan
# Pandas Serileri
# data                                         # pd.Series()
numbers = [20,30,40,50]                        # dtype: int64
letters = ['a','b','c','d']                    # dtype: object
obj = ['a','b','c',20]                         # dtype: object
dict = {'a':10,'b':20,'c':30,'d':40}           # dtype: int64
random_numbers = np.random.randint(10,100,6)   # dtype: int32
numpy_array = np.array([20,30,40,50])          # dtype: int32

pandas_series = pd.Series(numbers)
#print(pandas_series)
pandas_series = pd.Series(letters)
#print(pandas_series)
pandas_series = pd.Series(obj)
#print(pandas_series)
pandas_series = pd.Series(5, [0,1,2,3])
#print(pandas_series)
pandas_series = pd.Series(numbers, ['a','b','c','d'])
#print(pandas_series)
pandas_series = pd.Series(numbers, letters)
#print(pandas_series)
pandas_series = pd.Series(dict)
#print(pandas_series)
pandas_series = pd.Series(random_numbers)
#print(pandas_series)
pandas_series = pd.Series(numpy_array)
#print(pandas_series)

pandas_series = pd.Series([20,30,40,50], ['a','b','c','d'])
result = pandas_series[0]
#print(pandas_series)
#print(result) # 20
result = pandas_series.ndim
#print(result) # 1

result = pandas_series.shape
#print(result) # (4,)
result = pandas_series.sum()
#print(result) # 140
result = pandas_series.max()
#print(result) # 50
result = pandas_series + 50
#print(pandas_series)
#print(result)
result = np.sqrt(pandas_series)
#print(result)
result = pandas_series >= 50
#print(result)

dizi1 = pd.Series([1,2,3,4],['g','b','c','d'])
dizi2 = pd.Series([1,3,6,8],['a','b','c','e'])
result = dizi2 + dizi1
#print(result)
"""
a    NaN
b    5.0
c    9.0
d    NaN
e    NaN
g    NaN
dtype: float64 """

# Pandas DataFrames : series'lerin birleştirilmiş halidir.

s1 = pd.Series([3,2,0,1], name = "apple")
s2 = pd.Series([0,3,7,2], name = "orange")
data = pd.concat([s1,s2], axis = 1)
df = pd.DataFrame(data)
#print(df)
"""
   apple  orange
0      3       0
1      2       3
2      0       7
3      1       2
"""

df = pd.DataFrame()
#print(df)  #Empty DataFrame, Columns: [], Index: []
df = pd.DataFrame([1,2,3,4])
#print(df)
data = pd.DataFrame([["Ahmet",50],["Ali",60],["Yağmur",70]])
#print(data)
"""
        0   1
0   Ahmet  50
1     Ali  60
2  Yağmur  70
"""
data = [["Ahmet",50],["Ali",60],["Yağmur",70]]
df = pd.DataFrame(data, columns = ["name","grade"], index = [1,2,3])
#print(df)
"""
     name  grade
1   Ahmet     50
2     Ali     60
3  Yağmur     70
"""
dict = {"name": ["ahmet","ali","yağmur"], "grade": [50,60,70]}
df = pd.DataFrame(dict)
#print(df)
"""
     name  grade
1   Ahmet     50
2     Ali     60
3  Yağmur     70
"""

# Pandas ile farklı dosya tiplerinden veri okuma

# df = pd.read_json('*.json', encoding = "UTF-8") # encoding = "UTF-8" -> Türkçe karakter varsa
"""
connection = sqlite3.connect("sample.db")
df = pd.read_sql_query("SELECT * FROM students",connection) #pip install sqflite
"""
#df = pd.read_excel('sample.XLSX') # excel dosyalarını okumak için xlrd kütüphanesi indirmek gerekir. +openpyxl kütüphanesi
#df = pd.read_csv('sample.csv')
#print(df)


# Dataframe'ler ile çalışma

from numpy.random import randn
df = pd.DataFrame(randn(3,3), index = ["A","B","C"], columns = ["Column1","Column2","Column3"])

result = df
result = df["Column1"]
#print(result)
result = type(df["Column1"])
#print(result) # Name: Column1, dtype: float64 <class 'pandas.core.series.Series'>

# loc["row","column"] => loc["row"] => loc[":","column"]
#print(df)
result = df.loc["A"]
#print(result)
result = df.loc[:,"Column1":"Column2"]
#print(result)
result = df.loc["A":"B","Column1":"Column2"]
#print(result)

# iloc : indeks değerini değiştirdik (A,B,C) fakat yinede indeks değerleri ile çalışmak istediğimiz zaman kullanılır.
result = df.iloc[2]
#print(df)
#print(result)

result = df.drop("Column3", axis=1) # axis = 1 =>columns
#print(result)


# DataFrame ile filtreleme

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns = ["Column1","Column2","Column3","Column4","Column5"])
result = df
#print(result)
#print(df.head(5))
#print(df["Column1"].head(5)) = print(df.Column1.head(5))

result = df > 50
#print(result)
result = df[df > 50]
#print(result)
result = df[df["Column1"] > 70]
#print(result)
"""
   Column1  Column2  Column3  Column4  Column5
5       81       49       54       89       89
6       78       25       73       87       29
7       82       59       54       17       93
"""
result = df[df["Column1"] > 70][["Column1","Column2"]]
#print(result)
result = df[(df["Column1"] > 50) & (df["Column1"] <= 70)] # "|" => or
#print(result)


# DataFrame Groupby

personeller = {
    'Çalışan': ["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
    'Departman': ["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları"],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt':["Kadıköy","Tuzla","Maltepe","Tuzla","Maltepe","Tuzla","Kadıköy"],
    'Maaş':[5000,3000,4000,3500,2750,6500,4500]
}
df = pd.DataFrame(personeller)
result = df["Maaş"].sum()
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups # departman ve semt isimlerine göre grupla
#print(df)
#print(result)
"""
semtler = df.groupby("Semt")
for name, group in semtler:
    print(name)
    print(group)
"""
"""
Kadıköy
        Çalışan         Departman  Yaş     Semt  Maaş
0  Ahmet Yılmaz  İnsan Kaynakları   30  Kadıköy  5000
6   Mustafa Can  İnsan Kaynakları   42  Kadıköy  4500
Maltepe
         Çalışan    Departman  Yaş     Semt  Maaş
2  Hasan Korkmaz     Muhasebe   45  Maltepe  4000
4      Ali Turan  Bilgi İşlem   23  Maltepe  2750
Tuzla
       Çalışan         Departman  Yaş   Semt  Maaş
1   Can Ertürk       Bilgi İşlem   25  Tuzla  3000
3  Cenk Saymaz  İnsan Kaynakları   50  Tuzla  3500
5  Rıza Ertürk          Muhasebe   34  Tuzla  6500
"""

#result = df.groupby("Departman").sum()
#result = df.groupby("Departman").mean()
#result = df.groupby("Departman")["Maaş"].mean()
#print(result)
"""
Departman
Bilgi İşlem         2875.000000
Muhasebe            5250.000000
İnsan Kaynakları    4333.333333
Name: Maaş, dtype: float64
"""
#result = df.groupby("Departman")["Maaş"].max()["Muhasebe"]
#print(result)
#result = df.groupby("Departman").agg(np.mean) # agg() yöntemi, dizin (satır) ekseni olan DataFrame'in varsayılan 0 ekseni boyunca yürütülecek bir işlev veya işlev adları listesi uygulamanıza izin verir.
#print(result)

# Pandas ile kayıp ve bozuk veri analizi
data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data, index = ['a','c','e','f','h'], columns = ['column1','column2','column3'])
df = df.reindex(['a','b','c','d','e','f','g','h'])
result = df
#print(result)
"""
   column1  column2  column3
a     16.0     91.0     56.0
b      NaN      NaN      NaN
c     43.0     12.0     62.0
d      NaN      NaN      NaN
e     57.0     78.0     21.0
f     58.0     47.0     17.0
g      NaN      NaN      NaN
h     85.0     65.0     49.0
"""
result = df.drop(["column1","column2"], axis=1)
#print(result)
result = df.drop(["a","d"], axis=0)
#print(result)

result = df.isnull() # not a number(NaN) değerler için false değer döndürür.
result = df.isnull().sum()
#print(result)

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn
#print(df)
result = df[df["column1"].notnull()]["column1"]
#print(result)

result = df.dropna() # axis = 0 (varsayılan) satır bazında işlem yapar eğer satırda NaN değer varsa o satırı almaz.
#print(result)
"""
   column1  column2  column3  column4
f     82.0     68.0     86.0     30.0
h     53.0     65.0     93.0     10.0
"""
result = df.dropna(how = "any")
#print(result)
"""
   column1  column2  column3  column4
f     11.0     89.0     14.0     30.0
h     30.0     71.0     38.0     10.0
"""
result = df.dropna(how = "all")
#print(result)
"""
   column1  column2  column3  column4
a     50.0     40.0     82.0      NaN
b      NaN      NaN      NaN     30.0
c     69.0     30.0     30.0      NaN
d      NaN      NaN      NaN     51.0
e     22.0     74.0     27.0      NaN
f     11.0     89.0     14.0     30.0
h     30.0     71.0     38.0     10.0
"""
result = df.dropna(subset = ["column1","column2"])
#print(result)
result = df.dropna(thresh = 2) # en az iki kaydı olanları silme
#print(result)

result = df.fillna(value = "no input") # NaN olan değerleri doldurma
#print(result)
"""
    column1   column2   column3   column4
a      34.0      37.0      73.0  no input
b  no input  no input  no input      30.0
c      30.0      71.0      16.0  no input
d  no input  no input  no input      51.0
e      24.0      76.0      48.0  no input
f      39.0      70.0      79.0      30.0
g  no input  no input  no input  no input
h      33.0      50.0      66.0      10.0
"""

result = df.sum()
#print(result)
result = df.sum().sum()
#print(result)
result = df.isnull().sum().sum()
#print(result)
result = df.size
#print(result)
"""
column1    215.0   -> df.sum()
column2    178.0
column3    285.0
column4    121.0
dtype: float64
799.0              -> df.sum().sum()
13                 -> df.isnull().sum().sum()
32                 -> df.size
"""
def ortalama(df):                            # bütün null olan yerlere ortalama değeri (42.052632) yazdıran fonksiyon
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet
result = df.fillna(value = ortalama(df))
#print(result)
"""
     column1    column2    column3    column4
a  58.000000  52.000000  81.000000  42.052632
b  42.052632  42.052632  42.052632  30.000000
c  32.000000  62.000000  59.000000  42.052632
d  42.052632  42.052632  42.052632  51.000000
e  24.000000  37.000000  62.000000  42.052632
f  23.000000  17.000000  25.000000  30.000000
g  42.052632  42.052632  42.052632  42.052632
h  78.000000  10.000000  58.000000  10.000000
"""

# Pandas ile string fonksiyonları

data = pd.read_csv("sample.csv")
data.dropna(inplace = True)
newColumn = ["seyda b ","elif b","merve","ali","veli b","seyda","elif","merve","ali","veli","seyda","elif b","merve","ali","veli","seyda","elif","merve","ali","veli","seyda","elif","merve b","ali","veli","seyda","elif","merve","ali","veli"]
data["name"] = newColumn
#data["name"] = data["name"].str.upper() # lower
#data["index"] = data["name"].str.find('f')
#print(data)
"""
    Unnamed: 0  YearsExperience    Salary   name  index
0            0              1.2   39344.0  seyda     -1  f harfi bulunmamakta
1            1              1.4   46206.0   elif      3  name kolonunda 3.indekste f harfi bulunmakta
2            2              1.6   37732.0  merve     -1
3            3              2.1   43526.0    ali     -1
4            4              2.3   39892.0   veli     -1
...
"""
data = data[data.name.str.contains("el")]
#print(data)
"""
    Unnamed: 0  YearsExperience    Salary  name
1            1              1.4   46206.0  elif
4            4              2.3   39892.0  veli
6            6              3.1   60151.0  elif
9            9              3.8   57190.0  veli
11          11              4.1   55795.0  elif
...
"""
#data = data.name.str.replace(' ','-')
#print(data)
"""
1     elif-b
4     veli-b
6       elif
9       veli
11    elif-b
...
"""
data[['firstName','lastName']] = data['name'].loc[data['name'].str.split().str.len()==2].str.split(expand = True)
#print(data.head(10))
"""
    Unnamed: 0  YearsExperience    Salary    name firstName lastName
1            1              1.4   46206.0  elif b      elif        b
4            4              2.3   39892.0  veli b      veli        b
6            6              3.1   60151.0    elif       NaN      NaN
9            9              3.8   57190.0    veli       NaN      NaN
11          11              4.1   55795.0  elif b      elif        b
...
"""

# Pandas ile join ve merge

customers = {
    "CustomerId": [1,2,3,4],
    "FirstName": ["Ahmet","Ali","Hasan","Canan"],
    "LastName": ["Yılmaz","Korkmaz","Çelik","Toprak"],
}
orders = {
     "OrderId": [10,11,12,13],
     "CustomerId": [1,2,5,7],
     "OrderDate": ["2021-10.06","2021-10.07","2021-10.08","2021-10.09"]
}
df_customers = pd.DataFrame(customers, columns = ["CustomerId","FirstName","LastName"])
df_orders = pd.DataFrame(orders, columns = ["OrderId","CustomerId","OrderDate"])

#print(df_customers)
#print(df_orders)
"""
   CustomerId FirstName LastName
0           1     Ahmet   Yılmaz
1           2       Ali  Korkmaz
2           3     Hasan    Çelik
3           4     Canan   Toprak
   OrderId  CustomerId   OrderDate
0       10           1  2021-10.06
1       11           2  2021-10.07
2       12           5  2021-10.08
3       13           7  2021-10.09
"""
result = pd.merge(df_customers,df_orders,how='inner')
#print(result)
"""
   CustomerId FirstName LastName  OrderId   OrderDate
0           1     Ahmet   Yılmaz       10  2021-10.06
1           2       Ali  Korkmaz       11  2021-10.07
"""
result = pd.merge(df_customers,df_orders,how='left')
#print(result)
"""
   CustomerId FirstName LastName  OrderId   OrderDate
0           1     Ahmet   Yılmaz     10.0  2021-10.06
1           2       Ali  Korkmaz     11.0  2021-10.07
2           3     Hasan    Çelik      NaN         NaN
3           4     Canan   Toprak      NaN         NaN
"""
result = pd.merge(df_customers,df_orders,how='right') # outer (tüm kayıtlar)
#print(result)
"""
   CustomerId FirstName LastName  OrderId   OrderDate
0           1     Ahmet   Yılmaz       10  2021-10.06
1           2       Ali  Korkmaz       11  2021-10.07
2           5       NaN      NaN       12  2021-10.08
3           7       NaN      NaN       13  2021-10.09

"""
customersA = {
    "CustomerId": [1,2,3,4],
    "FirstName": ["Ahmet","Ali","Hasan","Canan"],
    "LastName": ["Yılmaz","Korkmaz","Çelik","Toprak"],
}
customersB = {
    "CustomerId": [4,5,6,7],
    "FirstName": ["Yağmur","Çınar","Cengiz","Can"],
    "LastName": ["Bilge","Turan","Yılmaz","Turan"],
}
df_customersA = pd.DataFrame(customersA,columns = ["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns=["CustomerId","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB],axis =1)
#print(result)

# Pandas ile DataFrame metodları

data = {
    "column1": [1,2,3,4,5],
    "column2": [10,20,13,45,25],
    "column3": ['abc','bca','ade','cba','dea']
}
df = pd.DataFrame(data)
result = df
result = df['column2'].unique()
#print(result)
result = df['column2'].nunique() # sayısı
#print(result)
result = df['column2'].value_counts() # her bir elemanın kaç kez tekrarladığını gösterir.
#print(result)

def kareal(x):
    return x * x
result = df['column1'].apply(kareal)   # ya da result = df['column1'] * 2
#print(result)

kareal2 = lambda  x: x * x
result = df['column1'].apply(kareal2)
#print(result)
"""
Lambda Fonksiyonu Neden Kullanılır?
Lambda fonksiyonu bir başka fonksiyon içinde kullanıldığında anlam kazanır. 
Örneğin bir sayının karesini mi kübünü mü almak istediğinizden emin değilsiniz bu durumda bir fonksiyon içerisinde lambda tanımlaması yaparak istediğimiz bir aşamada geriye çalıştırılabilir bir fonksiyon döndürebilirsiniz.
Örnek:
def math(n):
  return lambda a : a ** n

square = math(2)
cube = math(3)

print(square(3)) # 9
print(cube(3))    # 27
"""
result = df.sort_values("column2", ascending = False) # varsayılan olarak true, ascending = False değeri büyük olandan küçük olana doğru sıralama yapar.
#print(result)




