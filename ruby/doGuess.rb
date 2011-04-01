#coding:utf-8
  puts "#########################"
  puts "#                       #"
  puts "#   SAYI TAHMİN OYUNU   #"
  puts "#                       #"
  puts "#########################\n\n"
  sabit = 15
  i = 0
  while 2>1
      print "tahmininizi giriniz:"
      num = gets.chomp
      if num.to_i == sabit
          puts "****Tebrikler sayıyı bildiniz****"
          break
        end
      if num.to_i != sabit
        i += 1
        if i == 5
            puts "Mallesef 5 kere olan deneme hakkınız doldu"
            break
            end
        print "sayıyı büyütün ve tekrar "  if num.to_i < sabit
        print "sayıyı küçültün ve tekrar "  if num.to_i > sabit
        end
    end
