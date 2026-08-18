# Java Programlama Dili

//----------------------------------------------------------------------------
// Module: SimpleSelect.java
// Description: Test program for ODBC API interface. This java application
// will connect to a JDBC driver, issue a select statement
// and display all result columns and rows
// Product: JDBC to ODBC Bridge
//----------------------------------------------------------------------------

import java.net.URL;
import java.sql.\*;

class SimpleSelect {
public static void main (String args\[\]) {
String url = "jdbc:odbc:deneme";
String query = "SELECT \* FROM BOLGE";
try {
// jdbc-odbc köprü sürücüsünü yükle
Class.forName ("sun.jdbc.odbc.JdbcOdbcDriver");

DriverManager.setLogStream(System.out);

Connection con = DriverManager.getConnection (url, "KUTPRJ", "is4356ht");
checkForWarning (con.getWarnings ());
DatabaseMetaData dma = con.getMetaData ();

//System.out.println("\\nConnected to " + dma.getURL());
//System.out.println("Driver " + dma.getDriverName());
//System.out.println("Version " +dma.getDriverVersion());
//System.out.println("");

Statement stmt = con.createStatement ();
ResultSet rs = stmt.executeQuery (query);
dispResultSet (rs);

rs.close();
stmt.close();
con.close();
}
catch (SQLException ex) {
System.out.println ("\\n\*\*\* SQLException caught \*\*\*\\n");
while (ex != null) {
System.out.println ("SQLState: " +ex.getSQLState ());
System.out.println ("Message: " + ex.getMessage ());
System.out.println ("Vendor: " +ex.getErrorCode ());
ex = ex.getNextException ();
System.out.println ("");
}
}
catch (java.lang.Exception ex) {
ex.printStackTrace ();
}
}
private static boolean checkForWarning (SQLWarning warn) throws SQLException
{
boolean rc = false;
if (warn != null) {
System.out.println ("\\n \*\*\* Warning \*\*\*\\n");
rc = true;
while (warn != null) {
System.out.println ("SQLState: " +warn.getSQLState ());
System.out.println ("Message: " +warn.getMessage ());
System.out.println ("Vendor: " +warn.getErrorCode ());
System.out.println ("");
warn = warn.getNextWarning ();
}
}
return rc;
}
private static void dispResultSet (ResultSet rs)
throws SQLException
{
int i;
ResultSetMetaData rsmd = rs.getMetaData ();
int numCols = rsmd.getColumnCount ();

//for (i=1; i<=numCols; i++) {
// if (i > 1) System.out.print(",");
// System.out.print(rsmd.getColumnLabel(i));
// }
System.out.println("");
boolean more = rs.next ();
while (more) {
for (i=1; i<=numCols; i++) {
if (i > 1) System.out.print(",");
System.out.print(rs.getString(i));
}
System.out.println("");
more = rs.next ();
}
}
}

---
*Kaynak: `JAVA PROGRAMLAMA DİLİ/ekitap-H_Takci-Java_Programlama_Dili/csimpleselect.htm`*
*Örnekler: `Java-Programlama-Dili/ornekler/` (5 dosya)*
*Görseller: `Java-Programlama-Dili/gorseller/` (2 dosya)*
