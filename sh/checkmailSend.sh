#!/bin/bash

MAILER=$(which mail)
[ -n "$MAILER" ] || { echo >&2 "'mail' programı bulunamadı.  Lütfen mailutils paketini kurun."; exit 1; }

while :; do
   echo "$HOME dizini denetleniyor..."
   find $HOME -amin -10 | $MAILER -s "son 10 dk içinde işlem gören dosya ve dizinler //son denetleme: $(date +%c)" isim[et]alanadi[nokta]com
   echo 'Bir sonraki denetleme için bekleniyor...'
   sleep 10m;
done
