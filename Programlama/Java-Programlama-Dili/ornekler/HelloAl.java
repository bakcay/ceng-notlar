import java.io.*;
public class HelloAl
{
public static void main(String[] args) throws IOException
        {
        InputStreamReader reader=new InputStreamReader(System.in);
        BufferedReader input=new BufferedReader(reader);
        System.out.print("Enter Your Name :");
        String name=input.readLine();
        System.out.println("Merhaba "+name);
        }
}
