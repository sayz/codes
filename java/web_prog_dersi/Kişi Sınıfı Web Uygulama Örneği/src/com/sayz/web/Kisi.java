package com.sayz.web;
public class Kisi {

	private int tcno;
	private String ad;
	private String soyad ;
	public String uyur(){
		
		return "şu anda uyuyor";

	}
	
	public String gezer(){
		return "şu anda geziyor.";
	}
	
	public String getAd() {
		return ad;
	}
	
	public void setAd(String ad) {
		this.ad = ad;
	}
	
	public int getTcno() {
		return tcno;
	}
	
	public void setTcno(int tcno) {
		this.tcno = tcno;
	}
	
	public String getSoyad() {
		return soyad;
	}
	
	public void setSoyad(String soyad) {
		this.soyad = soyad;
	}
	
	public String infoPer(){
//		JOptionPane.showMessageDialog(null, "ad soyad: " + ad + " " + soyad + " tc: " + tcno);
		return "Ad Soyad: " + ad + " " + soyad + "<br \\>T.C No: " + tcno;
	}

}
