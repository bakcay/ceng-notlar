# Java Programlama Dili

import java.net.URL;
import java.sql.\*;
import java.io.\*;

class select
{

//\*\*\* main kısmı başlangıcı\*\*\*//

public static void main (String args\[\]) throws IOException
{
// veri alma kısmı
InputStreamReader reader=new InputStreamReader(System.in);
BufferedReader input=new BufferedReader(reader);
System.out.print("Enter Region Number :");
String name=input.readLine();
System.out.println("Merhaba "+name);
//veri alma bitiş
String url = "jdbc:odbc:deneme";
String query = "SELECT \* FROM BOLGE where BOLGE\_NO="+name;
try
{
Class.forName ("sun.jdbc.odbc.JdbcOdbcDriver");
Connection con = DriverManager.getConnection (url, "", "");
DatabaseMetaData dma = con.getMetaData ();

Statement stmt = con.createStatement ();
ResultSet rs = stmt.executeQuery (query);
dispResultSet (rs);

rs.close();
stmt.close();
con.close();
}
catch (SQLException ex)
{
System.out.println ("\\n\*\*\* SQLException caught \*\*\*\\n");
while (ex != null)
{
System.out.println ("SQLState: " +ex.getSQLState ());
System.out.println ("");
}
}
catch (java.lang.Exception ex)
{
ex.printStackTrace ();
}

}

//\*\*\* main kısmının sonu \*\*\*//

//\*\*\*dispResultSet başlangıcı \*\*\*//
private static void dispResultSet (ResultSet rs)
throws SQLException
{
int i;
ResultSetMetaData rsmd = rs.getMetaData ();
int numCols = rsmd.getColumnCount ();
System.out.println("");
boolean more = rs.next ();
while (more)
{
System.out.println(rs.getString(2));
more = rs.next ();
}
}
}
//\*\*\* dispResultSet sonu \*\*\*//
//\*\*\*program sonu \*\*\*//

---
*Kaynak: `JAVA PROGRAMLAMA DİLİ/ekitap-H_Takci-Java_Programlama_Dili/cselect.htm`*
*Örnekler: `Java-Programlama-Dili/ornekler/` (5 dosya)*
*Görseller: `Java-Programlama-Dili/gorseller/` (2 dosya)*
