#!/bin/bash

sudo apt-get install mailutils

while :; do
   echo "$HOME dizini denetleniyor..."
   find $HOME -amin -10 | mail -s "son 10 dk içinde işlem gören dosya ve dizinler //son denetleme: $(date +%c)" isim[et]alanadi[nokta]com
   echo 'Bir sonraki denetleme için bekleniyor...'
   sleep 10m;
done
