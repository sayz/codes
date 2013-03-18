public class Kisi {

	private int tcno;
	private String ad;
	private String soyad ;
	public void uyur(){
		System.out.println("şu anda uyuyor.");

	}
	
	public void gezer(){
		System.out.println("şu anda geziyor.");
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
	
	public void infoPer(){
//		JOptionPane.showMessageDialog(null, "ad soyad: " + ad + " " + soyad + " tc: " + tcno);
		System.out.println("Ad Soyad: " + ad + " " + soyad + "\nT.C No: " + tcno);
	}

}
