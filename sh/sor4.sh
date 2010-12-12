#!/bin/bash

yol=/tmp/cop.txt
du -s $HOME/*|sort -rn>"$yol"
echo -n "ilk kaçı görmek istersiniz >"; read i
head -n $i "$yol"

