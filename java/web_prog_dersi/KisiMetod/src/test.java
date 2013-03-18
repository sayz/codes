
public class test {
	public static void main(String[] args){ 
		Ogrenci ogr = new Ogrenci();
//		Ogretmen ort = new Ogretmen();
//		Memur memur =new Memur();
//		OgretimGorevlisi og = new OgretimGorevlisi();
		 
		ogr.gezer();
		ogr.uyur();
		ogr.kantin();
		ogr.setTcno(123);
		ogr.setAd("İlknur");
		ogr.setSoyad("Karataş");
		ogr.setBolum("Tıp");
		ogr.setMemleket("Samsun");
		ogr.setSinif("5");
		ogr.infoPer();
		ogr.infoOgr();
	}

}
