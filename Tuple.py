#Python Tuple

#Pythonda tuple listeleri, list' e benzer ancak farkı tuple içindeki elemanlar değiştirilemez yani tuple listesine ekleme, silme ve güncelleme yapamayız.

#Örnek

tuple=("banana","grape","cherry")
print(tuple)

#Tuple liste elemanları, parantez ile oluşturulur. Ayrıca parantez kullanmadan da tuple listesi oluşturmuş oluruz ancak okunabilirlik açısından parantez kullanabiliriz.

tuple2="banana","grape","cherry"
print(tuple2)

#Tuple Liste Elemanlarını Güncelleme

#Tuple liste elemanları değiştirilemez ancak başka bir liste türüne çevrilerek güncelleme yapılabilir.

#Örnek

a = ("banana", "grape", "cherry")
b = list(a) 
b[0] = "apple" 
print(b)

#Örnek

message = ('Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan')
print(message[3])
#Tuple listesinden bir aralık seçmek istediğimizde ise slicing yöntemini kullanabiliriz.

#Örnek

message = ('Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan') 
print(message[0:2])
#0 ve 2. indeks aralığında elemanlar seçilir ve geriye bir tuple listesi döner.

#Sıfırdan başladığımızdan dolayı 0 değerini vermemiş olsak bile aynı sonucu alırız.

#Örnek

message = ('Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan') 
print(message[:2])


#Tuple Elemanlarına Döngü ile Erişim

#Tuple elamanlarına indeks numaraları ile nasıl erişebileceğimizi öğrendik ancak her bir elemana indeks numarası ile tek tek ulaşmak bazen zor olabilir dolayısıyla liste elemanlarına bazen döngü ile ulaşmak isteriz.

#Örnek

names = ('ahmet','mehmet','cenk') 
for name in names: 
    print(name)

#Tuple Metotları

#Python tuple ile kullanabileceğimiz 2 tane metot vardır. Bunlar count() ve index() metotlarıdır.

#Bir tuple içerisindeki tekrarlayan elemanların sayısını almak için count() metodunu kullanırız.

#Örnek

numbers = (1, 10, 5, 16, 4, 9, 10) 
letters = ('a','a', 'g', 's', 'b', 'y', 'a', 's') 
print(numbers.count(10))
print(letters.count('a'))

#Bir tuple içerisinde bir elemanın index numarasını almak için index() metodu kullanılır.

#Örnek

numbers = (1, 10, 5, 16, 4, 9, 10) 
print(numbers.index(10))
