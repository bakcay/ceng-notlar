# Java Programlama Dili

import java.awt.\*;
import java.applet.\*;

public class ButtonApplet extends Applet
{
Button button1;
Button button2;
Button button3;

public void init()
{
button1 = new Button("Button1");
button2 = new Button("Button2");
button3 = new Button("Button3");

add(button1);
add(button2);
add(button3);
}

public boolean action(Event evt, Object arg)
{
if (evt.target instanceof Button)
HandleButtons(arg);
return true;
}

protected void HandleButtons(Object label)
{
if (label == "Button1")
button1.setLabel("1nottuB");
else if (label == "Button2")
button2.setLabel("2nottuB");
else if (label == "Button3")
button3.setLabel("3nottuB");
else
{
button1.setLabel("Button1");
button2.setLabel("Button2");
button3.setLabel("Button3");
}
}
}

---
*Kaynak: `JAVA PROGRAMLAMA DİLİ/ekitap-H_Takci-Java_Programlama_Dili/cbuttonapplet.htm`*
*Örnekler: `Java-Programlama-Dili/ornekler/` (5 dosya)*
*Görseller: `Java-Programlama-Dili/gorseller/` (2 dosya)*
