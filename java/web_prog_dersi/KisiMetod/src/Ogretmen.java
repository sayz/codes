public class Ogretmen extends Kisi{
		private String sicilNo;
		
		private String bolum;
		
		public String getSicilNo() {
			return sicilNo;
		}
		
		public void setSicilNo(String sicilNo) {
			this.sicilNo = sicilNo;
		}
		
		public String getBolum() {
			return bolum;
		}
		
		public void setBolum(String bolum) {
			this.bolum = bolum;
		}
		
		public void ders(){
			System.out.println("şu anda derste...");
		}
		
		public void sınav(){
			System.out.println("şu anda sınavda...");
		}
}