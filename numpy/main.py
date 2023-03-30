# Numpy
"""NumPy, dizilerle çalışmak için kullanılan bir Python kütüphanesidir. Ayrıca doğrusal cebir, fourier dönüşümü ve matrisler alanında çalışmak için de gerekli işlevlere sahiptir.

Python’da dizilerin amacına hizmet eden listeler vardır, ancak işlenmesi yavaştır. NumPy, geleneksel Python listelerinden 50 kata kadar daha hızlı bir dizi nesnesi sağlar.

NumPy’deki dizi nesnesi (array) ndarray olarak adlandırılır ve ndarray, çalışmayı çok kolaylaştıran birçok destekleyici işlev sağlar.

NumPy Neden Listelerden Daha Hızlı?
NumPy bir Python kütüphanesidir ve kısmen Python’da yazılmıştır, ancak hızlı hesaplama gerektiren parçaların çoğu C veya C ++ ile yazılmıştır.

NumPy’nin Kurulumu : pip install numpy

Referanslar:
https://numpy.org/doc/
https://kerteriz.net/python-numpy-kullanimi-nedir-ve-nasil-kullanilir/
https://www.btkakademi.gov.tr/portal/course/player/deliver/sifirdan-ileri-seviye-python-programlama
"""
import numpy as np

py_list = [1,2,3,4,5,6,7,8,9] # python list kavramı numpydaki array kavramına karşılık gelmektedir.
np_array = np.array([1,2,3,4,5,6,7,8,9]) # numpy array

print(type(py_list))  # <class 'list'>
print(type(np_array)) # <class 'numpy.ndarray'>

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3) # reshape metodu, bir dizinin şeklini (shape) değiştirmek için kullanılır.

print(py_multi)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np_multi)
"""[[1 2 3]
    [4 5 6]
    [7 8 9]]"""
print(np_array.ndim) # 1
print(np_multi.ndim) # 2

print(np_array.shape) # (9,) tek boyutlu
print(np_multi.shape) # (3, 3) 3x3'lük matris

# NUMPY DİZİLERİ İLE ÇALIŞMA

result = np.arange(1,10) # 1 ile 10 arasında sayılardan oluşan bir dizi oluştur.
print(result)
# [1 2 3 4 5 6 7 8 9]
result = np.arange(10,50,3) # 10 ile 50 arasında 3 artış ile dizi oluştur.
print(result)
# [10 13 16 19 22 25 28 31 34 37 40 43 46 49]
result = np.zeros(10)
print(result)
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
result = np.ones(10)
print(result)
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
result = np.linspace(0,100,5) # verilen başlangıç ve bitiş değerlerini 5 eşit parçaya böler.
print(result)
# [  0.  25.  50.  75. 100.]
result = np.random.randint(0,10,3) #
print(result)
result = np.random.rand(5) # 0 ile 1 arasında 5 sayı üretir.
print(result)
result = np.random.randn(3) # -1 ile 1 arasında 3 sayı üretir.
print(result)
np_array_1 = np.arange(50) # 0 ile 49 arasında sayılardan oluşan 50 elemanlı dizi
result = np_array_1.reshape(5,10) # 5x10'luk matris
print(result)
print(result.sum(axis=1)) # satırların toplamı
print(result.sum(axis=0)) # sütunların toplamı

result = np.random.randint(1,100,10)
print(result)
print(result.max()) # üretilen sayılar arasındaki en büyük sayıyı yazdır.
print(result.min()) # üretilen sayılar arasındaki en küçük sayıyı yazdır.
print(result.mean()) # üretilen sayıların ortalamsını yazdırır.
print(result.argmax()) # üretilen en büyük sayının indeks numarası
print(result.argmin()) # üretilen en küçük sayının indeks numarası

# NUMPY DİZİLERİNİN İNDEKSLENMESİ

numbers_1 = np.array([0,5,10,15,20,25,50,75])
print(numbers_1[5])
print(numbers_1[0:3])
print(numbers_1[::]) # baştan sona kadar tüm liste
print(numbers_1[::-1]) # adım sayısını sağdan sola doğru 1'er 1'er artırarak elemanları yazdırır.
# [75 50 25 20 15 10  5  0] ! Listeyi ters çevirmiş olur.

numbers_2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
print(numbers_2)
print(numbers_2[0])
print(numbers_2[0][2]) # ya da print(numbers_2[0,2])
print(numbers_2[:][2]) # matrisin 2. indeksindeki tüm elemanları yazdır.
print(numbers_2[:,2]) # bütün satırlardan 2.indeksteki elemanları yazdır.
print(numbers_2[0,:]) # 0.indeksteki tüm elemanları yazdırır
print(numbers_2[:2,:2]) # 0 ve 1. indeksteki satırları alır bunların içinden de 0 ve 1. indeksteki sütünları alır.

arr1 = np.arange(0,10)
arr2 = arr1 # referans
print(arr1)
# [0 1 2 3 4 5 6 7 8 9]
print(arr2)
# [0 1 2 3 4 5 6 7 8 9]
arr2[0] = 20
print(arr1)
# [20  1  2  3  4  5  6  7  8  9]
print(arr2)
# [20  1  2  3  4  5  6  7  8  9]

arr3 = np.arange(0,5)
arr4 = arr3.copy() # arr4 farklı adreste tanımlanan yeni bir listedir.
arr3[0] = 20
print(arr3)
# [20  1  2  3  4]
print(arr4)
# [0 1 2 3 4]

numbers = np.random.randint(0,10,9)
print(numbers)
result = numbers.reshape(3,3)
result = result[[1,0]] # 1. indeksteki elemanı ve 0. indeksteki elemanı alır
print(result)

# NUMPY DİZİ OPERASYONLARI

numbers_3 = np.random.randint(10,100,6)
numbers_4 = np.random.randint(10,100,6)
print(numbers_3)
print(numbers_4)
result = numbers_3 + numbers_4
print(result)
result = numbers_3 + 10 # numbers_3 dizisindeki her elemana 10 ekler.
print(result)
result = np.sin(numbers_3) # dizideki tüm elemanların sinüs değerini alır
print(result)
result = np.sqrt(numbers_3) # dizideki tüm elemanların sinüs değerini alır
print(result)
result = np.log(numbers_3) # dizideki tüm elemanların sinüs değerini alır
print(result)

mnubers1 = numbers_3.reshape(2,3)
mnubers2 = numbers_4.reshape(2,3)
print(mnubers1)
print(mnubers2)
result = np.vstack((mnubers1,mnubers2)) # parametre olarak verilen matrisleri dikey olarak birleştirme --vertical
print(result)
result = np.hstack((mnubers1,mnubers2)) # parametre olarak verilen matrisleri yatay olarak birleştirme --horizontal
print(result)

result = numbers_3 >= 50
print(result) # [False  True False False False  True]
result = numbers_3 % 2 == 0
print(result) # [False False False  True  True  True]


















