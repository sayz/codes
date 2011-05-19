import javax.swing.*;
import java.awt.*;
public class Logo extends JFrame
{
     //Logo sınıfımızın constructoru
     public Logo()
     {
          //Yeni bir JLabel objesi oluşturuluyor
          JLabel logoLabel = new JLabel("sefa yıldız",
          new ImageIcon("mec.jpg"),
          JLabel.CENTER);
 
          //burada yazımızın logonun neresine gelecegini belirtiyoruz
          //yazının dikey olarak logonun altında yatayda ise ortada olmasını istiyoruz
          logoLabel.setVerticalTextPosition(JLabel.BOTTOM);
          logoLabel.setHorizontalTextPosition(JLabel.CENTER);
 
          //JLabel objesini pencereye ekliyoruz
          this.getContentPane().add(logoLabel);
 
          //penceremeizin ekranın ortasında çıkmasını istiyoruz
          Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();
          this.setBounds((int)dim.getWidth()/2, (int)dim.getHeight()/2,100,100);
 
     }
 
     public static void main(String[] args)
     {
          //onu görünür hale getiriyoruz
          Logo l = new Logo();
          l.setVisible(true);
 
     }
}
