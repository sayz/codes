import java.io.*;
class faktoriyel {
	public double fakt(int girilen) {
		double hesap = 1;
		if((girilen == 0) || (girilen == 1)) return 1;
		else {
			for(int i = girilen; i > 0; i--) {
				hesap = hesap * i;
			}
			return hesap;
		}
	}
	public static void main(String s[])
	throws IOException {
		BufferedReader ekran = new BufferedReader(
		new InputStreamReader(System.in));
		System.out.print("faktöriyeli alınacak sayiyi giriniz:");
		String sayi = ekran.readLine();
		System.out.print("girilen sayi:" + sayi + "\n");
		Integer d = new Integer(sayi);
		int intsayi = d.intValue();
		faktoriyel f = new faktoriyel();
		System.out.println ("girilen sayının faktöriyeli :" + Math.round(f.fakt(intsayi)));//Math.round() yuvarlamak için
		}
}
