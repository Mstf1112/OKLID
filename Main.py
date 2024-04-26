# 2D uzaydaki noktaları temsil eden bir liste oluşturma
points = [(2, 3), (0, -1), (4, 5), (-2, 6)]

print("Points Listesi:")
print(points)
import math


def euclideanDistance(point1, point2):
    """
    İki nokta arasındaki Öklid mesafesini hesaplar.

    Argümanlar:
    point1 (tuple): İlk nokta, (x1, y1) şeklinde.
    point2 (tuple): İkinci nokta, (x2, y2) şeklinde.

    Dönüş:
    float: İki nokta arasındaki Öklid mesafesi.
    """
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


# Örnek kullanım
point1 = (2, 3)
point2 = (4, 6)
print("İki nokta arasındaki Öklid mesafesi:", euclideanDistance(point1, point2))

import math


def euclideanDistance(point1, point2):
    """
    İki nokta arasındaki Öklid mesafesini hesaplar.

    Argümanlar:
    point1 (tuple): İlk nokta, (x1, y1) şeklinde.
    point2 (tuple): İkinci nokta, (x2, y2) şeklinde.

    Dönüş:
    float: İki nokta arasındaki Öklid mesafesi.
    """
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


# Örnek 'points' listesi
points = [(2, 3), (0, -1), (4, 5), (-2, 6)]

# 'distances' adında boş bir liste oluşturalım
distances = []

# Her nokta çifti arasındaki Öklid mesafesini hesaplayalım ve 'distances' listesine ekleyelim
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı noktaları tekrar tekrar kontrol etmemek için j'yi i+1'den başlatıyoruz
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Sonucu gösterelim
print("Points Listesi:")
print(points)
print("Distances Listesi:")
print(distances)
# distances listesinden minimum mesafeyi bulma
min_distance = min(distances)

# Sonucu yazdırma
print("Minimum Mesafe:", min_distance)
