import javax.swing.*;


public class SearchName {

	
	public static void main(String[] args) {
		
		String[] personList = {"sefa", "ali", "veli", "selami", "ilknur", "sonnur","ayşe", "fatma", "jale", "hale"};
		
		String isim = JOptionPane.showInputDialog(null, "Aradığınız isim nedir?");

		Boolean foundFlag = false; 
		for (int i = 0; i < personList.length; i++) {
			if (personList[i].equals(isim)) {
				foundFlag = true;
				JOptionPane.showMessageDialog(null, "Aradığınız isim \"" + isim + "\", dizinin " + i + " nolu" + " indisinde bulunuyor.");
				System.exit(0);
			}
		}
		if (!foundFlag) {
			JOptionPane.showMessageDialog(null, "Aradığınız isim bu dizide yok!");
		}


	}

}