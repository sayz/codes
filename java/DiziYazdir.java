public class DiziYazdir {
    public static void main(String args[]){
        int i,j,k;
        int [] a = {1,2,3,4,5,6,7,8};
        double[] d = { 2.1 , 3.4 , 4.6 ,1.1 ,0.11 } ;
        String[] s = {"defter", "kalem", "sarman" , "tekir", "boncuk"};
        // double tipindeki dizimizi ekrana bastiriyoruz
        for (i = 0 ; i < d.length ; i ++) { 
            System.out.println("d["+i+"] = " + d[i] );
        }
        System.out.println("---------------");
        for (k = 0 ; k < a.length ; k ++) { 
            System.out.println("a["+k+"] = " + a[k] );
        }
        System.out.println("---------------");
        // String tipindeki dizimizi ekrana bastiriyoruz
        for (j = 0 ; j < s.length ; j ++) {
            System.out.println("s["+j+"] = " + s[j] );
        }
    }
}
