alist = [3, 5, 18, 9, 21,20, 20, 4, 17, 8, 1]
def secondMax(dizi)
max1 = dizi[0]
max2 = dizi[1]

for i in dizi
    if(i > max1)
        max2 = max1
        max1 = i

    elsif i > max2
        max2 = i
    end
end
max2
end
puts "Dizinin en büyük ikinci elemanı = " + secondMax(alist).to_s
        
