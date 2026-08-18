// Bu program ile dçüardan nÅmerik veri giriüi yapçlçr
// Hidayet TAKCI
// tarafçndan kodlanmçütçr.
/**************************/
import java.io.*;
public class DogumGunu
{
public static void main(String[] args) throws IOException
        {
        InputStreamReader reader=new InputStreamReader(System.in);
        BufferedReader input=new BufferedReader(reader);
        System.out.print("Enter Your Age :");
        String text=input.readLine();
        int age=new Integer(text).intValue();
        System.out.println("You are "+age+" years old");
        int year=2000-age;
        System.out.println("You were born in "+year);
        }
}
