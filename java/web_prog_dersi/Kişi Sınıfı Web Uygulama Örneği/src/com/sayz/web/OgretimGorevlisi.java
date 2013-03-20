package com.sayz.web;
public class OgretimGorevlisi extends Ogretmen{
	private String dal;
	int yas;
	
	public String getDal() {
		return "Dal: " + dal;
	}
	public void setDal(String dal) {
		this.dal = dal;
	}
	public int getYas() {
		return yas;
	}
	public void setYas(int yas) {
		this.yas = yas;
	}
}