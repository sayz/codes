package com.sayz.web;
public class Ogretmen extends Kisi{
		private String sicilNo;
		
		private String bolum;
		
		public String getSicilNo() {
			return "Sicil No: " + sicilNo;
		}
		
		public void setSicilNo(String sicilNo) {
			this.sicilNo = sicilNo;
		}
		
		public String getBolum() {
			return "Bölüm: " + bolum;
		}
		
		public void setBolum(String bolum) {
			this.bolum = bolum;
		}
		
		public String ders(){
			return "şu anda derste...";
		}
		
		public String sınav(){
			return "şu anda sınavda...";
		}
}