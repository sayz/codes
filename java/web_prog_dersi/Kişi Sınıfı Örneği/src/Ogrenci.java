
public class Ogrenci extends Kisi{
		private String memleket;
		private String bolum;
		private String sinif;
		
		public void ders(){
			System.out.println("şu anda derste.");
		}
		
		public void kantin(){
			System.out.println("şu anda kantinde.");
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
		public void infoOgr(){
			System.out.println("Doğum Yeri: " + memleket + "\nBölüm:"+ bolum + 
					"\nSınıf: " + sinif);
		}
}