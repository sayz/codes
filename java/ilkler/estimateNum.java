import java.io.*;
class estimateNum {
	public static void main(String s[])
	throws IOException {
		System.out.println("\t\t\t\tSAYI TAHMIN OYUNU");
		BufferedReader ekran = new BufferedReader(
		new InputStreamReader(System.in));
			int sabit = 1903;
			int i = 0;
			
			while(true) {
				System.out.print("Lütfen sayıyı giriniz(1000-2000):");
				String sayi = ekran.readLine();
				Integer d = new Integer(sayi);
				int a = d.intValue();	
				
				if (a == sabit) {
					System.out.println("!!!!!!Tebrikler Sayıyı Bildiniz!!!!!!");
					break;
				}
				
				if (a != sabit) {
					i++;
					if (i == 7) {
						System.out.println("Maalesef 5 kez olan deneme hakkınız bitti");
						break;
					}
					
					if (a < sabit)
						System.out.println("Sayıyı büyütün ve tekrar girin");
					if (a > sabit)
						System.out.println("Sayıyı küçültün ve tekrar girin");
				}
				
				}
				
		}
		
}
