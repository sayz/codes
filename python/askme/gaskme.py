#!/usr/bin/env python
#-*-coding:utf-8-*-
###########################
#                         #
#                         #
#                         #
#    coder: @sayz         #
#    team : 19 Tayfası    #
#                         #
#                         #
#                         #
###########################
import pygtk
import askme
pygtk.require20()
import gtk
class Gaskme(object):
    def __init__(self):
        #pencere ayarları yaılıyor:
        self.pencere = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.pencere.set_border_width(20)
        self.pencere.set_position(gtk.WIN_POS_CENTER)
        self.pencere.connect("delete_event", gtk.main_quit)

        #sözlük'ten kelime çekiliyor:
        self.sozluk = askme.putinto()
        self.randWord = askme.randomKelime(self.sozluk.keys())

        #pencere elemanları tanımlanıyor:
        self.giris = gtk.Entry()
        self.denetle = gtk.Button("kontrol")
        self.denetle.connect("clicked", self.is_true)
        self.i_etiket = gtk.Label("bakalım bilcek misin :-)")
        self.ii_etiket = gtk.Label(self.randWord)
        self.tablo= gtk.Table(2, 3, homogeneous=False)
        self.tablo.set_row_spacings(10)
        self.tablo.set_col_spacings(10)
        self.pencere.add(self.tablo)

        #pencere elemanlarını pencere üzerine yerleştiriyoruz:
        self.tablo.attach(self.ii_etiket, 0, 1, 0, 1)
        self.tablo.attach(self.giris, 0, 1, 1, 2)
        self.tablo.attach(self.denetle, 1, 2, 1, 2)
        self.tablo.attach(self.i_etiket, 0, 2, 2, 3)
        #--------------------------------------------------------
        self.pencere.show_all()
        
    def renkliEtiket(self, renk, metin):
        return """<span foreground='%s'>'%s'</span>"""%(renk, metin)

    def is_true(self, penar):
        try:
             self.entry = str(self.giris.get_text())
        except ValueError:
             pass
        
        self.farkL = askme.farkListesi(self.entry, self.sozluk[self.randWord])
        self.yuzde = askme.yuzdeBul(self.farkL, self.sozluk[self.randWord])

        if 100 >= self.yuzde >= 10:
            self.i_etiket.set_label(self.renkliEtiket("red", "hata\
var") + " cevap:%s" %self.sozluk[self.randWord])
            self.denetle.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("red"))
            self.giris.modify_text(gtk.STATE_NORMAL, gtk.gdk.Color("red"))

        elif askme.uzAbs(self.giris.get_text(), self.sozluk[self.randWord]) > 1:
            self.i_etiket.set_markup(self.renkliEtiket("red", "uzunluklar çok \
farklı") + "->cevap:%s"%self.sozluk[self.randWord])
            self.denetle.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("red"))
            self.giris.modify_text(gtk.STATE_NORMAL, gtk.gdk.Color("red"))

        else:
            self.i_etiket.set_label(self.renkliEtiket("blue","tebrikler doğru") + "->cevap:\
%s"%self.sozluk[self.randWord])
            self.denetle.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("blue"))
            self.giris.modify_text(gtk.STATE_NORMAL, gtk.gdk.Color("blue"))

    def main(self):
        gtk.main()

gui = Gaskme()
gui.main()
