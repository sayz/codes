import java.io.*;
class asal {
      public static void main(String[] args)
       throws IOException {
			BufferedReader konsol = new BufferedReader(new InputStreamReader(System.in)); 
			int i;
			int asal_mi = 1;
			System.out.print("Bir sayı giriniz > ");
			String strsayi = konsol.readLine();
			Integer sayi = new Integer(strsayi);		
			for( i = 2; i <= sayi/2; i++ ) {
				if( sayi%i == 0 ) {
					asal_mi = 0;
					break;
				}
			}
			if(asal_mi == 1){
				System.out.println(sayi + "\tasal sayıdır");
			}
			else{
				System.out.println(sayi + "\tasal sayı değildir");
			}

	}
}
