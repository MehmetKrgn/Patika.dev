# Patika.dev
Veri Yapilari ve Algoritmalar Insertion Sort Projesi

Proje 1
[22,27,16,2,18,6] -> Insertion Sort

1. Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
2. Big-O gösterimini yazınız.
3. Time Complexity: Average case: Aradığımız sayının ortada olması,Worst case: Aradığımız sayının sonda olması, Best case: Aradığımız sayının dizinin en başında olması.
4. Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.
5. [7,3,5,8,2,9,4,15,6] dizisinin Insertion Sort'a göre ilk 4 adımını yazınız.


## Çozum
1)
0. adim >> [22, 27, 16, 2, 18, 6]    en kucugu bul 0. index ile ddegis.
1. adim >> [2, 27, 16, 22, 18, 6] 0. indexten sonraki en kucugu bul 1. index ile degis.
2. adim >> [2, 6, 16, 22, 18, 27] 1. indexten sonraki en kucugu bul 2. index ile degis (kendisi ise değişiklik yapma).
3. adim >> [2, 6, 16, 22, 18, 27] 2. indexten sonraki en kucugu bul 3. index ile degis.
4. adim >> [2, 6, 16, 18, 22, 27] 3. indexten sonraki en kucugu bul 4. index ile degis (kendisi ise değişiklik yapma).
5. adim >> done

2)
n + (n-1) + (n-2) ... + 1 = n(n+1)/2 then The Time Comlexity is O(n^2)

3)
Best case: O(n), Worst Case: O(n^2)

4)
Dizi siralandiktan sonra 18 sayısı ortada olduğundan average pozisyonda olur.

5)
0. adim >> [7, 3, 5, 8, 2, 9, 4, 15, 6]   en kucugu bul 0. index ile degis.
1. adim >> [2, 3, 5, 8, 7, 9, 4, 15, 6] 0. indexten sonraki en kucugu bul 1. index ile degis (kendisi ise değişiklik yapma).
2. adim >> [2, 3, 4, 8, 7, 9, 5, 15, 6] 1. indexten sonraki en kucugu bul 2. index ile degis.
3. adim >> [2, 3, 4, 5, 7, 9, 8, 15, 6] 2. indexten sonraki en kucugu bul 3. index ile degis.
4. adim >> [2, 3, 4, 5, 6, 9, 8, 15, 7] 3. indexten sonraki en kucugu bul 4. index ile degis.
