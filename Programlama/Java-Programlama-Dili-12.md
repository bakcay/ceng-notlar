# Java Programlama Dili

**Yeni Başlayanlar İçin Java**

Programming With Java Kitabından Derlemedir.

Java, özellikle web ortamında kullanılmak üzere geliştirilmiş bir programlama dilidir. Platformdan bağımsız olarak çalışır. Java programları çalıştırılacağı zaman önce Applet download edilir, ardından da makinelere daha önceden yüklenmiş olan JVM (Java Virtual Machine) Appleti yorumlayarak çalıştırır.

Burada bazı temel bilgiler ve adım adım java anlatılacaktır.

Javayı nerden bulabilirsiniz?

[http://www.javasoft.com/](http://www.javasoft.com/) adresine giderek, Products & API linkini tıklarsınız ve takip eden adımlar sonucunda JDK 1.2 veya başka bir Java Development Kitini makinenize yüklersiniz. Yükleme esnasında karışıklık çıkmaması için yükleme dizini olarak c:\\java seçilebilir.

Yükleme işlemi bittikten sonra;

**Autoexec.bat** dosyasının ** PATH** satırı şu şekilde değiştirilmelidir.

```bash
SET PATH=c:\java\bin;%path%
```

classpath satırıda uygun bir şekilde değiştirilebilir. Eğer classlar c:\\java\\deneme gibi bir adreste yer alıyorsa classpath satırı şu şekilde olacaktır.

`SET CLASSPATH=c:\java\deneme;` olur.

Daha sonra .java uzantılı program parçalarını yazabilir ve çalıştırabilirsiniz. Yazılacak java programları ikiye ayrılmaktadır. Bunlar konsol programları ve applet programlarıdır.

Konsol Programları

Örnek bir java konsol programı aşağıdaki gibidir.

```java
public class Hello {
public static void main(String[] args) {
System.out.println("Merhaba Dunya ");
}
}
```

Hello.java programı

Program yazıldıktan sonra javac.exe (Java Compiler) tarafından derlenir.

```bash
javac Hello.java
```

eğer hata yoksa aktif dizinde Hello.class dosyası oluşacaktır.Bu dosyayı çalıştırabilmek için ise

`java Hello` komutu verilir. Komut çıktısı olarak ise ekrana 'Merhaba Dunya' metni çıkacaktır.

Applet Programları

Örnek bir applet programı ise şu şekilde olacaktır.

```java
import java.awt.*;
import java.applet.*;
public class Applet1 extends Applet {
public void paint(Graphics g) {
g.drawString("Hello from Java!", 60, 75);
}
}
```

Applet1.java programı

Bu program yazıldıktan sonra da yine derleme işlemi için javac kullanılır.

```bash
javac Applet1.java
```

yazılarak program derlenir. Derlenen programın sonucunu görmek için class, html uzantılı bir dosya içine gömülür.

Classın gömüldüğü örnek html dosyası şu şekildedir.

```html
<title>Applet Test Page</title>
<h1>Applet Test Page</h1>
<applet code="Applet1.class" width=200 height=150 name="Applet1">
</applet>
```

çalıştırmak için Appletviewer.exe kullanılır.

```bash
Appletviewer Applet1.html
```

yazıldıktan sonra ekrana aşağıdaki pencere gelecektir.

Dikkat edilmesi gereken hususlardan biri class adı ile program adının aynı olmasıdır.

Program, herhangi bir editörde (NotePad, WordPad, Word, Edit,...) yazılabilir. Kaydederken .java uzantısı ile kaydedilmek şartıyla.

[Java Sayfası](Java-Programlama-Dili-11.md)

---
*Kaynak: `JAVA PROGRAMLAMA DİLİ/ekitap-H_Takci-Java_Programlama_Dili/java.htm`*
*Örnekler: `Java-Programlama-Dili/ornekler/` (5 dosya)*
*Görseller: `Java-Programlama-Dili/gorseller/` (2 dosya)*
