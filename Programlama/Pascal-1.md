# Pascal

Beginner

[Getting Started](http://www.orkun.org/pdoc3.htm#Getting Started)

[write and writeln](http://www.orkun.org/pdoc3.htm#write and writeln)

[semicolons, libraries, readln](http://www.orkun.org/pdoc3.htm#semicolons)

[Hello, World](http://www.orkun.org/pdoc3.htm#hello)

[variables](http://www.orkun.org/pdoc3.htm#variables)

[Excercise 1.2](http://www.orkun.org/pdoc3.htm#1.2)

[constants](http://www.orkun.org/pdoc3.htm#Constants)

[readln](http://www.orkun.org/pdoc3.htm#readln2)

[Excercise 1.3](http://www.orkun.org/pdoc3.htm#1.3)

[math](http://www.orkun.org/pdoc3.htm#math)

[div, mod](http://www.orkun.org/pdoc3.htm#div and mod)

[boolean expressions](http://www.orkun.org/pdoc3.htm#boolean)

[and, or](http://www.orkun.org/pdoc3.htm#andor)

[if...then...else](http://www.orkun.org/pdoc3.htm#ifthen)

[for](http://www.orkun.org/pdoc3.htm#for)

[while](http://www.orkun.org/pdoc3.htm#while)

[repeat](http://www.orkun.org/pdoc3.htm#repeat)

[solutions](http://www.orkun.org/pdoc3.htm#solutions)

Getting Started

All Turbo Pascal programs must begin with a program name. This is simple. You just type the word 'program' one space and then what you want the title of the program to be. The title of the program can be anything you want as long as it is not what is referred to as a '*Reserved word*'. A reserved word is any word that is used by Turbo Pascal to receive commands. For example 'program' is a reserved word that tells Turbo Pascal that there is a program that can be run; therefore you may not use the word 'program' for any other purpose than that. You then type the reserved word 'begin' on a line all by itself. This tells Turbo Pascal where to start executing statements(where to begin), and you tupe 'end.' at the place to you want the program to end.</n>

```pascal
program Example;

begin
...;
...;
...;
end.
```

[[TOP]](http://www.orkun.org/pdoc3.htm#top)

write and writeln

The 'write' and 'writeln' commands are perhaps the two most basic commands in Turbo Pascal. There purpose is to display output on the screen. The format of the 'writeln' commands are simple. Simply type the command and then in parenthesis put what you want typed in single quotes('):

```pascal
writeln('Hello, World');
```

The easiest way of explaining the difference between the two is that 'writeln' sends the cursor to the next line for the next output while 'write' leaves the cursor in the same place, For example the commands:

```pascal
writeln('Hello, ');
writeln('World.');
```

will display the output:

Hello,

World.

on the screen whereas the lines

```pascal
write('Hello, ');
write('World.');
```

will display the output:

Hello World.

on the screen.

It is also possible to include more than just one group of text in a 'writeln' statement. You may also include variables and text together by just separating them with a comma(,).This is unimportant now but it is good to remember for later where more will be explained.

[[TOP]](http://www.orkun.org/pdoc3.htm#top)

Semicolons

You may have noticed in the code examples there is a semicolon at the end of every line. The reason for this is because in Turbo Pascal, Semicolon signify the end of a STATEMENT. The reason I say statement and not line is because in some cases you will want to spread out your statement over many lines and you will not want a semicolon on those lines. An example of this is a 'IF' statement which we will get to later, but for right now just put a semicolon after everything and you should be alright. The only exception is the 'begin' statement. Do not put a semicolon after any 'begin'.

Libraries

Libraries are extensions of Turbo Pascal commands. The specifics will be gon over in later chapters but For right now Lets just say that you call up different Libraries just after the 'program' statement using the 'uses' statement. For right now this is totally unimportant and you don't need to know it at all RIGHT NOW, however if in is kind of nice to be able to clear the screen before you run your program and to do that you need the 'crt' library so that you may use the 'clrscr'(clear screen) command. If you wish to clear the screen just do this: type the statement 'uses crt;' right after the 'program' statement and immediately after the 'begin' statement type 'clrscr'.

readln

It is to early to talk about the readln statement but for right now type 'readln;' just before your 'end.' this will pause the program until the ENTER key is pressed, otherwise when you run it your program will run and go back into Turbo Pascal so fast you won't think it has run at all and you will think that there is an error when there really isn't.

[[TOP]](http://www.orkun.org/pdoc3.htm#top)

Excercise 1.1: Hello, World

You are now ready to write your first Turbo Pascal Program. Go into your Turbo Pascal Compiler and type in a program that displays the output 'Hello World'. The program solution is at the bottom of this page but try not to look at it. If you are unable to get the program to work don't worry look at the code example and type it in. As long as you understand what is happening we're in good shape.
[[TOP]](http://www.orkun.org/pdoc3.htm#top)

Variables

In Algebra a variable is a character with a non-constant numeric value(a letter with a changing

number value). In Turbo Pascal it is essentially the same thing. You assign a variable a value

using the sign I sometimes like to call the *Becomes Equal To* sign. It is made of simply a colon

and an equal sign(:=). Say I created a variable called 'Number', and then I assigned it a value of

two. I can then treat that variable exactly like the number 2.

For Example the lines:

```pascal
Number := 2;
writeln('Number: ', Number);
```

will produce the output

Number: 2

or

```pascal
Number := 2 + 1;
writeln('Number: ', Number);
```

will produce the output

Number: 3

(Note that in these examples the parentheses after the 'writeln' statements contain both text and variable which are separated by a comma(,). This is perfectly legal)

You can name a Variable anything you like as long as it is not a reserved word. You may not call a variable 'begin' or 'end' or anything else like that. You can write any variable, but when you do do not put it in quotations like if you were writing normal text. If you do the variable name will come on the screen instead of the variable value.

the code

```pascal
Number := 3;
writeln(Number);
writeln('Number');
```

will display the output

3

Number

There are several different variable types: Integer, Real, string, char, and Boolean.

**Integer** variable types are a part of the whole number system. That means that any number without any decimal positions is an integer. Integer values cannot be greater than 32,767 and cannot be less than -32,767. Example:

-32767...-3,-2,-1,0,2,3...32767

**Real** variable types can be any number including numbers with decimal positions. this includes numbers like 10.0. Even though it has the same value as 10 it is a Real number and not an integer because of the decimal place. Real numbers are displayed on the screen in scientific notation which can be confusing so you will learn to deal with these later. Example:

1.23498 , 3.543 , -9.0 , 987.765

**String** variable types are variables that have word values. They can be any array of characters and can have any value including numbers. But it is important to remember that if a string variable has a number value it is only a group of character numbers and cannot be treated as Real or Integer variables. It is important to remember that when assigning string variables a value you must put single quotes(') around it. Example:

```pascal
Word := 'Hello';
```

**Char** variable types are actually character variable types, but Turbo Pascal shortens it to char. These variable types are exactly treated like string variable types except for the fact that they can only be 1 character long. They can be any character 'a' through 'z' or '0' - '9'. also they can be any other character on the ASCII chart of characters. Like strings however, they can have number values but cannot be treated as actual numbers. Example:

'a' , 'A' , '3' , '!' , '&' , '{' , '+' , etc.

**Boolean** variables can only have two values: TRUE and FALSE. These are useful as flags and can be treated like comparisons, but you will probably not use these very frequently and you not need to now them right now so they will be left for later.

The variable types you will be using most right now are Integer type, Real type, and string type. Now that you know what kind of variables are possible you can learn how to declare them. Bear in mind that once they are declared they can only contain data of there declared type. For example you may not assign the value of 'a' to a variable declared as an Integer or a Real.

Before variables can be used the must be declared before the program begins. This is done with a 'var' statement a list of the variables you wish to declare and their types. We call this a *variable *declaration for right now the 'var' statement must come right after the 'uses' statement and just before the 'begin' statement in your program.

```pascal
var
Number1, Number 2:Integer;
Word1,Word2:string;
Letter:char;
Error:boolean;
```

This variable declaration will assign the variables 'Number1' and 'Number2' as integer variables, the variables 'Word1' and 'Word2' as string variables, the variable 'Letter' as a character variable, and the variable 'Error' as a Boolean. These variables can now be used in the program.

[[TOP]](http://www.orkun.org/pdoc3.htm#top)

Ex: 1.2

To practice using variables write a program with a variable declaration that declares 3 integer variables and one string variable. In the main body of the program(between the 'begin' and end.' statements) assign two of the integer variables numbers then assign the third integer variable the sum of the two other integer variables. Give the string variable the value of 'Sum' and then display the Value of the String variable and the value of the third integer variable on the screen.

[[TOP]](http://www.orkun.org/pdoc3.htm#top)

Constants

Constants are like variables because you declare them at the top of the program. The are not like

variables because they can have no value other than the one they are declared with. This sounds

useless but when your program gets extremely large constants can help clarify things and make

debugging(finding and fixing mistakes in the code) easier.

Constants are declared using the 'Const' statement and this must appear right before the 'var' statement in a program. When assigning a value the equal sign(=) is used by itself. Example:

```pascal
Const
Pi = 3.14;
CircleDegrees = 360;
```

After the values are declared they remain that value throughout the program and cannot be changed. [[TOP]](http://www.orkun.org/pdoc3.htm#top)

readln

Now that you now about variables you can learn about the 'readln' statement. The readln

statement is very useful because it allows you to get input from the keyboard. The reason this

section did not come earlier in the tutorial is because you must know about variables to use it.

When the user(the person using the program) enters a value into the program and a 'readln'

statement is used to receive the data, Turbo Pascal uses a variable to store the Data. That

variable name and type is decided by the programer(you).

The structure of the 'readln' statement is simple. Just put the variable you with to contain the entered value in parentheses immediately after the word 'readln'. The variable will be reassigned that data and no other and will contain that data until reassigned again.

For example if you wanted the user to enter his age you would want to store the information in an integer variable so you would put an Integer variable in the parentheses after the readln and it would look something like this:

```pascal
readln(age);
```

O course 'age' would have to be declared at the beginning of the program. If you wanted the user to enter their name it would be the same except the variable would have to be declared as a string variable. It is important to remember that the readln statement does not put anything on the screen except a flashing curser. So the code:

```pascal
readln(age);
```

would look like this on the screen

_

Therefore you will want a 'writeln' statement telling the user what they are entering.

```pascal
write('Enter age: ');
readln(age;)
```

This produces:

Enter age: _

[[TOP]](http://www.orkun.org/pdoc3.htm#top)

ex: 1.3

Now that you have a knowledge of the 'readln' statement you should take this opportunity to practice using it. Write a program that requests the name and age of the user and then writes it on the screen.

[[TOP]](http://www.orkun.org/pdoc3.htm#top)

+,-,*,/

For future reference it is good to know that you are allowed to add(+), subtract(-), multiply(*), and divide(/) numbers and variables in Turbo Pascal. It is also important to remember that standard order of operations apply when doing complex calculations. If you don't know order of operations it really isn't hard. They are the order in which complex calculations should be executed. The easiest way to remember is BEDMAS: Brackets, Exponents, Division and Multiplication, and last is Addition and Subtraction. For example:

2 + 3 * 4 - (4 + 6 / 2)

Solving this using order of operations is simple. First comes Brackets or parentheses. So first, solve the '4 + 6 / 2' part. Because in the order of operations Division comes before Addition; divide the 6 by 2 first then add the 4 to get 7. So the equation now is '2 + 3 * 4 - 7'. The next step in order of operations is Exponents, but since there aren't any go on to Multiplication and Division. So the next step is to multiply 3 * 4 which gives the answer 12. Now the equation is '2 + 12 - 7'. The only operations left are addition and subtraction; so just do them in order to get the answer 7. If you still don't understand order of operations consult your local math teacher and ask them. If there is no local math teacher and you can't find anybody who knows, or you can't find the information in a book or Internet, you can E-Mail me and I will see what I can do for you. [[TOP]](http://www.orkun.org/pdoc3.htm#top)

div, mod

It is important to observe that when dividing numbers often times the answer isn't a whole

number. For example 3 / 2 = 1.5. The problem here is that when you divide two integers such as

3 and 2 you get a 'real' number. So there are two reserved words in Turbo Pascal that were made

specifically for dividing integers. 'div' is used to find out how many times one number goes into

another number. So the code:

```pascal
writeln('Three goes into eleven ', 11 div 3, 'times.');
```

will produce the output:

Three goes into eleven 3 times.

11 divided by 3 does not equal 3, but since three can Å5SÍo/k6
MÚÆUz;Õ/?)ì´kGÿ{>º¬­÷qøÙY

º'@(m<RQjs)CÉÎ¡aZs¾Ç±4Ì9¦_@?ã &Vî Õ}9L¢Ì ëYø%.,¼é¶ðp
?­& u¡pvOª^½ó8¼¯k³6Pfôß ÿDôMÛæþÔ»î
ÛhÁ{O×ÂÐ;D¤

Öð°;Ù!¿Ga

÷ÕªjÛûShÇÈÎ<mîO-x‑\`x¾Ó\g[<õÇ,ð

Ç³Cà9­x¿
OÁáx*°\µ]Tqáâz&ÿPþ5a8{

æ8_g8Ãpï®Be­Å
¶ 3 ­ß¢²ëÍå R>ª4wN Úó%PMÌÏ,ItÂ-lÞóN7CÁócäsaä@Üè M´ù!/ö/¶Idèå¤òeô?7Ë®X\`sxû,Ó»ÙwI3èéÃ\`8/hª

U
®áÌusë]A~ÙvÛâvzÄÂ¬ªø ÒB

H´¸ªúnÁdM¾Å·±
\%d½W0çù!¡±¦¸ßGÛxBv] ÓÁ½2 ­°F; ÜÒ
¶Mme'
$öi9@@íôÊ.úÁã 'ít­¾6867 mod 25);

This prints:

25 goes into 867 a total of 34 times with a remainder of 17

There are three methods of programming that can be used to write any problem and solve any problem. **Sequence**, **Selection**, and **Iteration**. What you have learned so far has been the most basic method of Sequence(statements executing in order). Now that you know many of the basics you can begin learning The other programming methods. [[TOP]](http://www.orkun.org/pdoc3.htm#top)

Boolean Expressions

Before you learn about infamous 'if' statement you must know about boolean expressions. First,

What is a boolean expression. A boolean expression is simply a comparison it can be either of

two things: TRUE or FALSE. Why do they call it boolean. Well it says in all the science books

that it was named after some scientist guy, but the truth is that the programers of old were just

trying to make your life miserable. Anyway, anything that can be labeled TRUE or FALSE. All

boolean expressions must contain a boolean operator, <,>,=,<>.

This is a table to explain all the boolean operator:

| > | greater than |
| --- | --- |
| < | less than |
| >= | greater than or equal to |
| <= | less than or equal to |
| <> | not equal to |
| = | equal to |

Here is an example of a boolean expression:

3 > 4

This is a boolean expression, and it has the value of FALSE. Just because it has a value of FALSE does not mean it is an illegitimate statement. It is perfectly legal, and will not give an error message when used. You may also compare variables to one another. Real, integer, string, and char variables can be compared. When comparing string and char variables it is compared alphabetically. The variable that precedes another alphabetically has a value of less than:

aardvark <apple >

This boolean expression is TRUE. It works the same with character variables. When comparing strings and character values there is one very important thing to remember. The way a computer compares letters is it takes that letters ASCII value and compares it to the other. This works just fine until you have words that contain capital letters and lowercase. On the ASCII Chart all Capital letters come before all lower case letters. If you don't know what ASCII is don't worry about it. Right now it is unimportant; just remember that all capital letters are less than all character values so the statement:

Z

is TRUE. A lower case 'a' has a greater value than all upper case letters 'A' through 'Z'.

You may be wondering where you are going to use all this. Having a thorough knowledge of boolean expressions is very important. If you don't fully understand what has been said it would be wise to re-read this section. [[TOP]](http://www.orkun.org/pdoc3.htm#top)

and, or

A boolean expression can also contain more than one comparison using the reserved words 'and'

and 'or'. These two words you will find useful in the future in some cases you will want some

desired input to meet two requirements before executing a statement so you will want to use

'and'. Or maybe you want the input to meet one of two requirements to execute a statement then

you would use 'or'. For right now just look at this code example:

```pascal
(Grade >= 80) and (Grade <90)
```

(note parentheses around boolean expressions; when using 'and' or 'or' this must be the case)

when using 'and' both comparisons have to be true for the whole expression to be true. So in the above example if 'Grade' is an integer variable that is greater than or equal to 80 and Grade is less than 90 then the above statement is TRUE. But if either or both of the two comparisons is FALSE the whole thing is FALSE. Here is an example of the possible combinations using 'and':

TRUE and TRUE = TRUE

TRUE and FALSE = FALSE

FALSE and TRUE = FALSE

FALSE and FALSE = FALSE

'or' is a different story:

```pascal
(Grade >= 80) or (Grade <90)
```

Here if either of the two comparisons is true the whole thing is true:

TRUE or TRUE = TRUE

TRUE or FALSE = TRUE

FALSE or TRUE = TRUE

FALSE or FALSE = FALSE

If you are uncertain of using 'and' and 'or' don't worry about it right now but remember this place because you will need to use it later. [[TOP]](http://www.orkun.org/pdoc3.htm#top)

if..then

In many cases in programming you will want the computer to react differently according to the

input. For example: you are asking the user to enter a grade value between 0 and 100. If they

enter a value higher than 90 you want the text 'Good work!' to appear on the screen(here is where

you get to use those boolean expressions). This is called selection and is often done using an 'If'

statement and it takes this form:

```pascal
if (Boolean expression)
then (statement);
```

The 'If' statement isn't hard to learn and makes perfect sense just think about it this way: IF THIS THEN DO THIS; IF GRADE IS GREATER THAN 90 THEN WRITELN('Good Work!'); This is not hard at all; the important thing to remember is that the if statement needs a Boolean expression to run decide what to do. In the example above the Boolean expression is 'GRADE IS GREATER THAN 90'. This is either TRUE or FALSE. GRADE is either greater than 90(TRUE) or it isn't(FALSE). The boolean expression after the 'if' must be TRUE for the statement after the 'then' to execute.

assuming 'grade' is an Integer variable between 90 and 100; the code:

```pascal
if grade > 90
then writeln('Good Work!');
```

will display the output:

Good Work!

Take note that there is NO SEMICOLON after the first line. This is important. Semicolon mark the end of a statement. That is why it is called an 'if' statement, because any part by itself is not a complete statement but the whole thing together is. A full statement does not have to be on one line. And in many cases you do not want(and sometimes can't) keep a full statement on one line. It is clearer and therefore better to break up an if statement into parts to make the code clear. If you put a semicolon after the 90 then you will get an error.

else

Now that you know the basic structure of an if statement you may learn how to incorporate 'else'.

It is very easy. Just think IF THIS THEN DO THIS ELSE DO THIS; IF GRADE IS GREATER

THAN 90 THEN WRITELN('Good Work!') ELSE WRITELN('Try 'Harder!'). The 'else' part

tells the computer what to do if the boolean expression in the 'if' statement is FALSE. Take a

look at this code:

```pascal
if Grade > 90
then writeln('Good Work!')
else writeln('Keep Trying!');
```

If Grade is an Integer value greater than 90 then the output:

Good Work!

will appear on the screen. If Grade is not greater than 90 then the output:

Keep Trying!

will appear.

else if

There can be more than one boolean expression in an 'if' statement. Lets say you have a grade

value between 0 and 100 and it is stored in an integer variable 'Grade'. You want to write an 'if'

statement that will print the text 'High Honors!' on the screen if the value of Grade is 90 or

above, or if the value of Grade is less than 90 but is equal to 80 or above then you want the

computer to print the text 'Honors!' otherwise you want the computer to print the text 'Keep

Trying!'. Stop for a minute and think about how you would do this with what you have learned

so far.

You probably thought about having three 'if' statements and the code would look something like this:

```pascal
if Grade >= 90
then writeln('High Honors!');
if (Grade < 90) and (Grade >= 80)
then writeln('Honors');
if Grade < 80
then writeln('Keep Trying');
```

There is an easier and better way. 'else if' is sort of like a secondary 'if' in an 'if' statement. Like an 'if', 'else if' has a boolean expression right after it. If the boolean expression just after 'if' is FALSE then the computer looks at the boolean expression just after the 'else if' statement Take a look at an example:

```pascal
if Grade => 90
then writeln('High Honors!')
else if Grade => 80
then writeln('Honors!')
else
writeln('Keep Trying!');
```

To best understand it assume that Grade is an integer with a value of 85. If Grade has a value of 85 then the first boolean expression is FALSE so the computer skips the second boolean expression. 85 is greater than 80 so the boolean expression after 'else if' is TRUE, therefore:

Honors!

would appear on the screen.

begin..end

Many times in an if statement you will want more than one line to execute if the boolean

expression is true. This can be done with 'begin' and 'end':

```pascal
if Grade > 90
then
begin
writeln('High Honors!');
writeln('Keep up the good work!');
end
else writeln('Keep Trying!');
```

So if 'Grade' is greater than 90 then

High Honors!

Keep up the good work!

will appear on the screen.

[[TOP]](http://www.orkun.org/pdoc3.htm#top)

Excercise 1.4

You should now know enough about 'if' statements to start using them in your code. Write a program that asks for three integer grades between 0 and 100 from the user and then it deciphers which one is highest and which one is the lowest and prints them on the screen and labels them. Sample screen:

Enter first grade(1-100):_89_

Enter second grade(1-100):_32_

Enter third grade(1-100):_54_

89 is highest

32 is lowest

**This is not that easy**. You may want to go back and review the section on the 'and' and 'or' commands. It should help a great deal.

Now that you can program in sequence and selection it is time you learned how to program using itteration. Iteration is a simple idea: You keep repeating a specified amount of code until the computer is told to stop. These are called loops.

[[TOP]](http://www.orkun.org/pdoc3.htm#top)

for

The 'for' loop structure is not hard to understand. The 'for' loop is used when there is a set number of times you want to repeat a certain amount of code. Each 'for' loop requires an integer variable that serves as a counter. Look at the first example:

```pascal
for n := 1 to 4 do
writeln(n);
```

This is your basic 'for' loop. 'n' has to be a declared integer variable. After the for it is assigned the values one through four using the reserved word 'to'. This makes it so that on the first loop n will have a value of 1 on the second 2 and so on until it has a value of 4. Once it has a value of 4 it will stop looping. So the above code would give the output:

1

2

3

4

It is important to remember that only the statement immediately after the 'do' will execute in the loop so if you wish to execute more than one statement you will have to use 'begin' and 'end'. The code:

```pascal
for n := 1 to 4 do
writeln('hello');
writeln('goodbye');
```

Even though it is indented so that it looks like the second statement after the 'for' would execute the output of this code would look like this:

hello

hello

hello

hello

goodbye

Lets add a begin and end to the statement:

```pascal
for n := 1 to 4 do
begin
writeln('hello');
writeln('goodbye');
end;
```

This code will look like this on the output display:

hello

goodbye

hello

goodbye

hello

goodbye

hello

goodbye

Lets take a look at a more practical use for the 'for' loop. Say you wanted to get seven integers entered from the user and added together to get a total. There is an easier way than typing in seven 'write' statements each followed by a 'readln' statement. With a loop it only takes one of each.

```pascal
Total := 0;
for n := 1 to 7 do
begin
write('Enter number ', n);
readln(Number);
Total := Total + Number;
end;
```

This code will ask for a number seven times and will add the entered number to total each time. When the loop finishes you will have the total of all seven numbers added together. Take note that 'Total' was initialized at zero before the loop started. This is important because notice that in the loop 'Total' is being reassigned with its own value plus that of the value of 'Number'. If it is not initialized to 0, Total will start with a garbage value. This will result in an incorrect answer.

In a 'for' loop the counter can begin anywhere and end any where as long as it is an integer. so you could say:

```pascal
for n := -5 to 5 do
```

and the loop would loop 11 times(don't forget to include 0). Also you can begin on a higher number and go down to a lower number. Just remember to use the reserved word 'downto' instead of 'to':

```pascal
for n := 10 downto 5 do
```

One last thing you must also remember is that you must never ever put a semicolon after the 'do' in a 'for' loop. If you do this the computer will think it is the end of a statement and it will just executed the loop before even coming to the statement/s that you wanted executed in the loop.

[[TOP]](http://www.orkun.org/pdoc3.htm#top)

while

A 'while' loop is different than a for loop in that it loops a variable amount of times depending on a boolean expression that comes right after the 'while'. Here is an example:

```pascal
while count <20 do count :="count" + 1;
```

Wether this 'while' loop executes or not totally depends on the boolean expression 'count <20'. If this expression is TRUE then the loop will execute; If count is equal to or greater than 20 then this expression is FALSE and the loop will not execute. It is this way with all 'while' loops; if the boolean expression is TRUE it executes if not it doesn't.

A 'while' loop is like a for loop in that it will only execute the statement immediately following it in the loop. So to execute more than one statement you must use 'begin' and 'end', just like a 'for' loop. What is a while loop good for? It is good in case you want a loop that will only execute if a certain condition is met. For example, 'while' loops are good for **error traps**. An error trap is a loop that executes when the user enters undesired input. For example say the computer requested a number between 1 and 10 and the user entered an 11; then you would want the computer to tell the person that they had entered bad input and would like them to re-enter the value. The code might look something like this:

```pascal
write('Enter number between 1 and 10: ');
readln(Number);
while (Number <1) or (Number 10) do
begin
write('Bad input. Please Enter a value between 1 and 10:');
readln(Number);
end;
```

If Number is an integer variable and the user enters a value less than one or greater than ten then the boolean expression in the 'while' loop is true and the loop will execute. This will print:

Bad input. Please Enter a value between 1 and 10: _

and now the user is prompted to enter a new value for 'Number'. After they do the computer sees the 'end;' and so it jumps back up to the 'while' to check and see if the boolean expression is TRUE or FALSE. If the user entered a value between 1 and 10 then the boolean expression is FALSE and the loop will not execute again but if the user entered another wrong value than the boolean expression is TRUE and the error loop will execute a second time. It will keep doing this until the correct input is entered.

[[TOP]](http://www.orkun.org/pdoc3.htm#top)

repeat...until

There are only two main differences between the 'while' loop and the 'repeat...until' loop. The first is the fact that instead of the boolean expression before the loop starts it comes just after the loop ends. This means that no matter what, a 'repeat...until' loop will always execute at least once; whereas in a 'while' loop it might not execute at all. The second difference is that the 'repeat...until' loop does not require a 'begin' and 'end' when you want to have more than one statement in the loop. for example:

```pascal
count := 0;
Total := 0;
repeat
count := count + 1;
write('Enter Grade: ');
readln(Grade);
Total := Total + Grade;
until count = 7;
```

This is a good example of a 'repeat...until' loop. Notice that there is no 'begin' or 'end' despite the fact that there are 4 statements in the loop. There is a counter in the loop so that the loop will only loop 7 times and will know when to stop.

When using 'while' loops and 'repeat...until' loops it is important to be careful not to get into **infinite loops**. Infinite loops are loops where the computer keeps looping and looping and the boolean expression is always true so that the loop can never be exited. Here is an example:

```pascal
count := 0;
Total := 0;
repeat
write('Enter Grade: ');
readln(Grade);
Total := Total + Grade;
until count = 7;
```

Infinite Loops

This is the same code as the previous code except without the counter('count := count + 1;').

Without this line count will not change in the loop so while you are in the loop count will equal 0

and will never equal 7. So the condition 'until count = 7' is never met and the loop will go on

forever.

Excercise 1.5

Write a program called 'Grade'. The program should allow the user to enter as many grades as they want and it should have a terminator so that when the user enters the number 999 the computer knows that the user is finished entering grades. Make it so that the computer keeps track of the highest and lowest grades. At the end print the average of the grades, the number of grades entered and the highest and lowest grades entered. Make it so that if the user wants they can keep entering sets of grades for as long as they want. Example run:

Enter Grade(1-100, 999 to quit): 90

Enter Grade(1-100, 999 to quit): 157

Grade must be between 1 and 100.

Enter Grade(1-100, 999 to quit): 92

Enter Grade(1-100, 999 to quit): 88

Enter Grade(1-100, 999 to quit): 999

The average of the 3 grades is 90

The highest grade was 92

The lowest grade was 88

Do you wish to enter another set(Y/N): p

Do you wish to enter another set(Y/N): n

**WARNING**: This is very difficult, so don't kill yourself over it.

Solutions

Solution for excercise 1.1:

```pascal
program Hello_World
uses crt;
begin
clrscr;
writlen('Hello, World');
readln;
end.
```

Solution for excercise 1.2

```pascal
program variablePractice;
uses crt;
var
Number1,Number2,Number3:Integer;
Word:String;
begin
clrscr;
Number1 := 76;
Number2 := 53;
Number3 := Number1 + Number2;
Word := 'Sum';
writeln(Word, ': ', Number3);
readln;
end.
```

Solution for excercise 1.3

```pascal
program nameage;
uses crt;
var
name:string;
age:integer;
begin
clrscr;
write('Enter name: ');
readln(name);
write('Enter age: ');
readln(age);
writeln;
writeln(name, ', you are ', age, ' years old');
readln;
end.
```

Solution to excercise 1.4:

```pascal
program grades;
uses crt;
var
grade1, grade2, grade3:integer;
begin
clrscr;
write('Enter first grade(1-100): ');
readln(Grade1);
write('Enter second grade(1-100): ');
readln(Grade2);
write('Enter third grade(1-100): ');
readln(Grade3);
if (Grade1 > Grade2) and (Grade1 > Grade3)
then writeln(Grade1, ' is highest.')
else if (Grade 2 > Grade1) and (Grade2 > Grade3)
then writeln(Grade2, ' is highest.')
else writeln(Grade3, ' is highest');
if (Grade1 < Grade2) and (Grade1 < Grade3)
then writeln(Grade2, ' is lowest.')
else if (Grade 2 < Grade1) and (Grade2 < Grade3)
then writeln(Grade2, ' is lowest.')
else writeln(Grade3, ' is lowest.');
readln;
end.
```

Solution to excercise 1.5

```pascal
program Grades;
uses crt;
var
Total, Grade, HighGrade, LowGrade, NumGrades:integer;
Average:Real;
Chioce:String;
begin
clrscr;
repeat
Total := 0;
NumGrades := 0;
HighGrade := 0;
LowGrade := 100;
repeat
write('Enter Grade(1-100, 999 to quit): ');
readln(Grade);
while (Grade <> 999) and ((Grade > 100) or (Grade <1)) do begin writeln('Grade must be between 1 and 100.'); write('Enter Grade(1-100, 999 to quit): '); readln(Grade); end; if Grade <> 999
then
begin
Total := Total + Grade;
NumGrades := NumGrades + 1;
If Grade > HighGrade
then HighGrade := Grade;
if Grade <LowGrade then LowGrade :="Grade;" end; until Grade="999;" Average :="Total" / NumGrades; writeln('The average of the ', NumGrades, ' grades is ', average:1:1); writeln('The highest grade was ', HighGrade); writeln('The lowest grade was ', LowGrade); writeln; repeat write('Do you wish to enter another set of grades(Y/N)? '); readln(Choice); until (upcase(Choice)="Y" ) or (upcase(Choice)="N" ); until upcase(Choice)="N" ; end. >
```

[[TOP]](http://www.orkun.org/pdoc3.htm#top)

Borland Firmasının Web Sitesinden alınmıştır.

---
*Kaynak: `PASCAL/Pascal Hakkynda Döküman 2 - bornova_ege_edu_tr.htm`*
