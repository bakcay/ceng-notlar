# CGI - Perl Kullanimi

WebMailer 1.1 ReadMe.TXT File

Thank's for trying out WebMailer We hope you find many uses for

this software.....

-----------------------------------------------------------

1 WebMailer 1.1 Information / Documentataion

-----------------------------------------------------------

WebMailer 1.1 is currently a Freeware Application. It does require WindMail

which you can find at:

http://www.geocel.com/windmail/

-----------------------------------------------------------

2 LIMITED WARRANTY AND DISCLAIMER OF WARRANTY

-----------------------------------------------------------

THIS SOFTWARE (WINDMAIL!) AND ALL ACCOMPANYING WRITTEN MATERIALS ARE PROVIDED

"AS IS" WITHOUT WARRANTY OF ANY KIND. FURTHER, GEOCEL INTERNATIONAL,

INC.(GEOCEL) DOES NOT WARRANT, GUARANTEE, OR MAKE ANY REPRESENTATIONS REGARDING

THE USE, OR THE RESULTS OF USE, OF THE SOFTWARE OR WRITTEN MATERIALS IN TERMS

OF CORRECTNESS, ACCURACY, RELIABILITY, CURRENTNESS, OR OTHERWISE. THE ENTIRE

RISK AS TO THE RESULTS AND PERFORMANCE OF THE SOFTWARE IS ASSUMED BY YOU. IF

THE SOFTWARE OR WRITTEN MATERIALS ARE DEFECTIVE, YOU, AND NOT GEOCEL OR ITS

DEALERS, DISTRIBUTORS, AGENTS, OR EMPLOYEES, ASSUME THE ENTIRE COST OF ALL

NECESSARY SERVICING, REPAIR, OR CORRECTION.

THE ABOVE IS THE ONLY WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED,

INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND

FITNESS FOR A PARTICULAR PURPOSE, THAT IS MADE BY GEOCEL, ON THIS GEOCEL PRODUCT.

NO ORAL OR WRITTEN INFORMATION OR ADVICE GIVEN BY GEOCEL, ITS DEALERS,

DISTRIBUTORS, AGENTS OR EMPLOYEES SHALL CREATE A WARRANTY OR IN ANY WAY

INCREASE THE SCOPE OF THIS WARRANTY AND YOU MAY NOT RELY ON ANY SUCH

INFORMATION OR ADVICE. YOU MAY HAVE OTHER RIGHTS WHICH VARY FROM STATE TO

STATE.

NEITHER GEOECL NOR ANYONE ELSE WHO HAS BEEN INVOLVED IN THE CREATION,

PRODUCTION OR DELIVERY OF THIS PRODUCT SHALL BE LIABLE FOR ANY DIRECT,

INDIRECT, CONSEQUENTIAL OR INCIDENTAL DAMAGES (INCLUDING DAMAGES FOR LOSS OF

BUSINESS PROFITS, BUSINESS INTERRUPTION, LOSS OF BUSINESS INFORMATION, AND

THE LIKE) ARISING OUT OF THE USE OR INABILITY TO USE SUCH PRODUCT EVEN IF

GEOCEL HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

This Limited Warranty shall be governed and construed in accordance

with the laws of the State of Texas.

ACKNOWLEDGMENT

BY USING AND/OR INSTALLING WINDMAIL!, YOU ACKNOWLEDGE THAT YOU HAVE READ THIS

LIMITED WARRANTY, UNDERSTAND IT, AND AGREE TO BE BOUND BY ITS' TERMS AND CONDITIONS.

YOU ALSO AGREE THAT THE LIMITED WARRANTY IS THE COMPLETE AND EXCLUSIVE STATEMENT OF

AGREEMENT BETWEEN THE PARTIES AND SUPERSEDE ALL PROPOSALS OR PRIOR AGREEMENTS,

ORAL OR WRITTEN, AND ANY OTHER COMMUNICATIONS BETWEEN THE PARTIES RELATING TO

THE SUBJECT MATTER OF THE LIMITED WARRANTY.

-----------------------------------------------------------

6 Installation

-----------------------------------------------------------

Files:

webmailer.exe - Actual CGI Program

webmailer.htm - Sample HTML Form for Submission to WebMailer

You need to copy the WEBMAILER.EXE file to the CGI-BIN Directory, or a Directory

that has CGI Execute permission enabled.

The WEBMAILER.HTM is just a sample HTML FORM that can be used with webmailer.

The FORM ACTION must be pointed to your WebMailer CGI!

-----------------------------------------------------------

7 Documentation

-----------------------------------------------------------

The Only Controls for this program are HTML Form Variables. For example,

to set the Background Image of the return page to a specific picture you could set

the form variable BGIMAGE to a URL or Relative Link. This would be done like:

<INPUT TYPE=HIDDEN NAME=BGIMAGE VALUE="/images/background.gif">

The only required variables are "email" and "recipient".

Variable Required

Description

-----------------------------------------------------------

EMAIL Required benc@geocel.com

Sets the email address who the Mail appears to be coming from. This could be a constant,

HIDDEN type variable, or could be a TEXT input field. Letting a user enter their

Email address would make it look as though the message was sent from the user.

RECIPIENT Required benc@geocel.com

Sets the email address that the message is delivered to. This is almost always a HIDDEN

variable, but could be a TEXT field if you are using WebMailer as a Web To Email gateway.

REQUIRED Optional "First\_Name, Last\_Name, Address, Phone, City"

This is where you enter a list of Required Fields. If a user submits a form without the

REQUIRED fields, they are told that their Form is incomplete and which blanks are

required.

SORTORDER Optional "First\_Name, Middle, Last\_Name, Age"

This variable sets the order of the variables in the form as they are reported back to you

and displayed to the User in the Optional output page. This is also how you choose

only the variables you want to show up.

REDIRECT Optional http://www.geocel.com/windmail/

Sets the URL (must be absolute URL) of the Thank You page of your choice. If this is not

entered, then WebMailer will output a customizable output page.

BGIMAGE Optional /images/background.gif

Sets the background image of the output page (if REDIRECT is not present), or of any

error pages.

BGCOLOR Optional FFFFFF

Sets the background color of the output page (if REDIRECT is not present), or of any

error pages.

TEXTCOLOR Optional 000000

Sets the text color of the output page (if REDIRECT is not present), or of any

error pages.

LINKBACK Optional http://www.geocel.com/windmail/

Creates a Link at the bottom of the output Page. This is the URL that it links back to.

LINKBACKTEXT Optional Back to the WebMailer 1.0 Website!

If there is a Link Back to the WebSite, this is the text that is displayed along with that

link.

-----------------------------------------------------------

8 Technical Support

-----------------------------------------------------------

This is a Freeware Application, therefore it has no Commercial Support. WindMail,

however is a commercial application and does have support. This program will only

be supported through WindMail.

---
*Kaynak: `CGI-PERL KULLANIMI/webmail.txt`*
*Örnekler: `CGI-Perl-Kullanimi/ornekler/` (30 dosya)*
*Görseller: `CGI-Perl-Kullanimi/gorseller/` (1 dosya)*
