# Java Programlama Dili

import java.awt.\*;
public class ButtonActionsTest extends java.applet.Applet {
public void init() {
setBackground(Color.white);
add(new Button("Red"));
add(new Button("Blue"));
add(new Button("Green"));
add(new Button("White"));
add(new Button("Black"));
}
public boolean action(Event evt, Object arg) {
if (evt.target instanceof Button) {
changeColor((String)arg);
return true;
} else return false;
}
void changeColor(String bname) {
if (bname.equals("Red")) setBackground(Color.red);
else if (bname.equals("Blue")) setBackground(Color.blue);
else if (bname.equals("Green")) setBackground(Color.green);
else if (bname.equals("White")) setBackground(Color.white);
else setBackground(Color.black);
repaint();
}
}

---
*Kaynak: `JAVA PROGRAMLAMA DİLİ/ekitap-H_Takci-Java_Programlama_Dili/cbuttonactions.htm`*
*Örnekler: `Java-Programlama-Dili/ornekler/` (5 dosya)*
*Görseller: `Java-Programlama-Dili/gorseller/` (2 dosya)*
