package com.sayz.web;

public class Ogrenci extends Kisi{
		private String memleket;
		private String bolum;
		private String sinif;
		
		public String ders(){
			return "şu anda derste.";
		}
		
		public String kantin(){
			return "şu anda kantinde.";
		}

		public String getMemleket() {
			return memleket;
		}
		public void setMemleket(String memleket) {
			this.memleket = memleket;
		}
		public String getBolum() {
			return bolum;
		}
		public void setBolum(String bolum) {
			this.bolum = bolum;
		}
		public String getSinif() {
			return sinif;
		}
		public void setSinif(String sinif) {
			this.sinif = sinif;
		}
		public String infoOgr(){
			return "Doğum Yeri: " + memleket + "<br \\>Bölüm:"+ bolum + 
					"<br \\>Sınıf: " + sinif;
		}
}