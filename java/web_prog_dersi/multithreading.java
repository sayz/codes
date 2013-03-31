package multithreading;

public class ThreadOrnek {

  /**
	 * @param args
	 * @author sayz
	 */
	class CharYaz implements Runnable {
		private char karakter;
		private int yazimSayisi;

		
		public CharYaz() {
			
		}
		
		public CharYaz(char karakter, int yazimSayisi) {
			this.karakter = karakter;
			this.yazimSayisi = yazimSayisi;
		}
		
		public void run() {
			for (int i = 0; i < yazimSayisi; i++) {
				System.out.print(karakter);
			}
		}
	}
	
	class RakamYaz implements Runnable {
		private int rakamlar;
		private int yazimSayisi;

		
		public RakamYaz() {
			
		}
		
		public RakamYaz (int rakamlar, int yazimSyisi) {
			this.rakamlar = rakamlar;
			this.yazimSayisi = yazimSyisi;
		}
		
		public void run() {
			for (int i = 0; i < yazimSayisi; i++) {
				System.out.print(rakamlar);
				Thread.yield();
			}
		}
	}
	
	public static void main(String[] args) {
		ThreadOrnek.CharYaz karakterYaz = new ThreadOrnek().new CharYaz('A', 5);
		ThreadOrnek.RakamYaz rakamYaz = new ThreadOrnek().new RakamYaz(15, 5);
		ThreadOrnek.CharYaz karakterYaz2 = new ThreadOrnek().new CharYaz('B', 5);
		
		Thread isParcasi1 = new Thread(karakterYaz); isParcasi1.start();
		Thread isParcasi2 = new Thread(rakamYaz); isParcasi2.start();
		Thread isParcasi3 = new Thread(karakterYaz2); isParcasi3.start();
		
		

	}

}
