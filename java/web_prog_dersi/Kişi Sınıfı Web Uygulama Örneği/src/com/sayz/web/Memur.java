package com.sayz.web;
public class Memur extends Kisi{
	/**
	 * 
	 */

	private String gorev;
	private int memno;
	
	public String evrakGetir(){
			return "şu anda evrakları getiriyor";
		}
		public String evrakGotur(){
			return "şu anda evrakları götürüyor";
		}
		public String getGorev() {
			return gorev;
		}
		public void setGorev(String gorev) {
			this.gorev = gorev;
		}
		public int getMemNo() {
			return memno;
		}
		public void setMemNo(int i) {
			this.memno = i;
		}
		
		public String infoMem(){
			return "Görev: " + gorev + "<br \\>" + "Memur No: " + memno;
		}

}