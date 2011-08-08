#!/usr/bin/env ruby

require 'date'

#ing->tr gunler sozlugu olustur
in_tr = {
	"Mon" => "Pazartesi",
	"Tue" => "Sali",
	"Wed" => "Carsamba",
	"Thu" => "Persembe",
	"Fri" => "Cuma",
	"Sat" => "Cumartesi",
	"Sun" => "Pazar" }

puts "tarihi giriniz(gg, aa, yyyy):"

tarih = gets.chomp

#gg, aa, yyyy seklindeki tarihi 3 parcaya ayir.
split_tarih = tarih.split(/, */)

#ingilizce olarak o tarihteki gunu al.
in_day = Date.new(split_tarih[2].to_i, split_tarih[1].to_i, split_tarih[0].to_i).strftime("%a")

#gunu turkceye cevir.
tr_day = in_tr[in_day]

#gunu bas :-)
puts tr_day

