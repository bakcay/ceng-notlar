<%@ LANGUAGE=VBSCRIPT %>
<%
Server.ScriptTimeOut = 300    'Server'a daha  çok zaman tanımak için
strMenuSayfaURL = "/menu.htm"  'oluşturacağımız sayfanın yolu
strListKlasor = "/"           'içindekileri bulacağımız dizin
'Başka bir dizinin içindekiler listesi için dizinin adından sonra ters-bölü koymak gerekir örnek "/test/"
'Bu programı çalıştırabilmek için Web dizininde programların yazma izni olması gerekir
%>

<HTML>
<TITLE>ASP ILE MENU OLUSTURMA</TITLE>
<META http-equiv="content-type" content="text/html; charset=ISO-8859-9">
<META http-equiv="Content-Type" content="text/html; charset=windows-1254">
<BODY>

<%
Response.Write "<P>Menü sayfası oluşturuluyor: " & strMenuSayfaURL & " ...</P>"

'menü sayfası olacak düz yazı dosyasını oluşturalım
Set objFSO = CreateObject("Scripting.FileSystemObject")
strDosyaAdi = Server.MapPath(strMenuSayfaURL)
Set objMenuSayfa = objFSO.CreateTextFile(strDosyaAdi, True) 'overwrite

'menü sayfasının başlık bölümünü yazalım
objMenuSayfa.WriteLine "<HTML><BODY><P><B>Dosyaların listesi</B></P>"

'belirtilen dizindeki dosyaların listesini içeren kolleksiyonu oluşturalım
Set objKlasor = objFSO.GetFolder(Server.MapPath(strListKlasor))
Set kolDosyalar = objKlasor.Files

'Her bir dosyanın başlığını okuyarak listemizi yapalım
For Each objDosya in kolDosyalar

   'dosya adının uzantısı ASP ve HTM olanları ayıralım
   strDosyaTuru = objFSO.GetExtensionName(objDosya.Name)
   If (strDosyaTuru = "asp") Or (Left(strDosyaTuru, 3) = "htm") Then

      'dosyanın  tümünü okuyup bir String'de tutalım
      Set objOku = objDosya.OpenAsTextStream(1) 'okumak için
      strIcerik = objOku.ReadAll
      objOku.Close

      'içinden başlık bölümünü alalım
      strBaslik = ""
      intBaslangic = Instr(UCase(strIcerik), "<TITLE>") + 7
      intSon = Instr(UCase(strIcerik), "</TITLE>")
      If (intBaslangic > 0) And (intSon > intBaslangic) Then
        strBaslik = Trim(Mid(strIcerik, intBaslangic, intSon - intBaslangic))
      End If
      If Len(strBaslik) = 0 Then strBaslik = "Adsız sayfa '" & objDosya.Name & "'"

      'Menü sayfası için metni oluşturalım
      strBuDosyaURL = strListKlasor & objDosya.Name
      strKopru = "<A HREF=" & Chr(34) & strBuDosyaURL _
              & Chr(34) & ">" & strBaslik & "</A><BR>"
      objMenuSayfa.WriteLine(strKopru)

   End If

Next

'Menü sayfasının son bölümünü yazalım
objMenuSayfa.WriteLine "</BODY></HTML>"
objMenuSayfa.Close
Response.Write "<P>Menü sayfası oluşturuldu.</P>"
%>

<P><A HREF="<% = strMenuSayfaURL %>">Menü sayfasını aç</A></P>
</BODY>
</HTML>
