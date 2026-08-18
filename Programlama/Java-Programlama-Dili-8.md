# Java Programlama Dili

//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PROGRAM BAŞLANGICI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*//
import java.applet.\*;
import java.awt.\*;
import java.util.Vector;
import java.sql.\*;
import java.lang.\*;
//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
public class OutputApplet extends Applet implements Runnable {
private Thread worker;
private Vector queryResults;
private String message = "Initializing";
TextField textField;
Label label;
//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
public synchronized void start()
{
label=new Label("Bir Deger Girin ", Label.LEFT);
add(label);
textField = new TextField(20);
add(textField);

if (worker == null)
{
message = "Connecting to database";
worker = new Thread(this);
worker.start();
}
}
//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
public void run()
{
String str = textField.getText();

String url = "jdbc:odbc:deneme";
String query = "select \* from BOLGE WHERE BOLGE\_ADI LIKE '%"+str+"%'";
try {
Class.forName ("sun.jdbc.odbc.JdbcOdbcDriver");
} catch(Exception ex)
{
setError("Can't find Database driver class: " + ex);
return;
}

try {
Vector results = new Vector();
Connection con = DriverManager.getConnection(url,"", "");
Statement stmt = con.createStatement();
ResultSet rs = stmt.executeQuery(query);

while (rs.next()) {
String s = rs.getString("BOLGE\_ADI");
String text = s ;
results.addElement(text);
}
stmt.close();
con.close();
setResults(results);
} catch(SQLException ex)
{
setError("SQLException: " + ex);
}
}
//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
public synchronized void paint(Graphics g)
{
if (queryResults == null) {
g.drawString(message, 5, 50);
return;
}
g.drawString("Bolgelerimiz : ", 5, 50);
int y = 70;
java.util.Enumeration enum = queryResults.elements();
while (enum.hasMoreElements()) {
String text = (String)enum.nextElement();
g.drawString(text, 5, y);
y = y + 15;
}
}
//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
private synchronized void setError(String mess)
{
queryResults = null;
message = mess;
worker = null;
repaint();
}
//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
private synchronized void setResults(Vector results)
{
queryResults = results;
worker = null;
repaint();
}
//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
public boolean action(Event evt, Object arg)
{
run();
return true;
}
//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
}
//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PROGRAM SONU \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*//

---
*Kaynak: `JAVA PROGRAMLAMA DİLİ/ekitap-H_Takci-Java_Programlama_Dili/coutputapplet.htm`*
*Örnekler: `Java-Programlama-Dili/ornekler/` (5 dosya)*
*Görseller: `Java-Programlama-Dili/gorseller/` (2 dosya)*
