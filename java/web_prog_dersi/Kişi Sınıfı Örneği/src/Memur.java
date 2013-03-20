public class Memur extends Kisi{
	private String gorev;
	
	public void evrakGetir(){
			System.out.println("şu anda evrakları getiriyor");
		}
		public void evrakGotur(){
			System.out.println("şu anda evrakları götürüyor");
		}
		public String getGorev() {
			return gorev;
		}
		public void setGorev(String gorev) {
			this.gorev = gorev;
		}
		public void infoMem(){
			System.out.println("Görev: " + gorev);
		}

}