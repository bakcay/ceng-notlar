# Java Programlama Dili

import java.awt.\*;
import java.applet.\*;

public class MouseApplet extends Applet
{
int coordX, coordY;
public void init()
{
coordX = -1;
coordY = -1;
Font font =new Font("TimesRoman", Font.BOLD, 24);
setFont(font);
resize(400, 300);
}

public void paint(Graphics g)
{
if (coordX != -1)
g.drawString("Click!", coordX, coordY);
}

public boolean mouseDown(Event evt, int x, int y)
{
coordX = x;
coordY = y;
repaint();
return true;
}
}

---
*Kaynak: `JAVA PROGRAMLAMA DİLİ/ekitap-H_Takci-Java_Programlama_Dili/cmouseapplet.htm`*
*Örnekler: `Java-Programlama-Dili/ornekler/` (5 dosya)*
*Görseller: `Java-Programlama-Dili/gorseller/` (2 dosya)*
