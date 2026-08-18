// Bu program ile dçüardan nÅmerik veri giriüi yapçlçr
// Hidayet TAKCI
// tarafçndan kodlanmçütçr.
/**************************/
import java.io.*;
public class DaireAlan
{
public static void main(String[] args) throws IOException
        {
        InputStreamReader reader=new InputStreamReader(System.in);
        BufferedReader input=new BufferedReader(reader);
        System.out.print("Enter the radius :");
        String text=input.readLine();
        Double x=new Double(text);
        double r=x.doubleValue();
        double area=Math.PI*r*r;
        System.out.println("The area of the circle is equal to "+area);
        }
}
