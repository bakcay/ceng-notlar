# Programming İn Pascal

## **PROGRAMMING IN PASCAL**

## **Contents**

**SECTION 1** page

Getting Started start here 1

Example 1 your first Pascal program 1

Example 2 cost of buying stamps 4

Designing Programs the four design stages 5

Example 3 cost of a bus journey 5

Example 4 garden fencing 10

Example 5 darts scores 12

Example 6 student test results 12

Example 7 soccer team points 13

Text Variables string data type 14

Example 8 input name and age 14

Semicolons semicolon as a separator 16

Example 9 percentage test result 16

Example 10 sales of chips 17

Example 11 average race times 19

Decisions, decisions IF...THEN...ELSE statements 20

Example 12 old enough to vote? 20

Example 13 exam - pass or fail 21

Example 14 guess the capital city 22

Example 15 electronic scoreboard 25

Example 16 calculating income tax 26

Over and over different types of loops 26

The Unconditional Loop average exam marks 27

The Conditional Loop the guessing game 30

Example 17 the guessing game again... 30

Example 18 the guessing game again with clues 32

**SECTION 2** page

Procedures, procedures the need to use procedures 35

Example 19 different flavours of chips 35

Example 20 capital cities again 40

Example 21 invoices and sales tax 42

**SECTION 3**

Arrays the need to use arrays 45

Example 22 read in students' test marks 45

Validation the need to validate data 48

Rounding rounding and truncating 50

Example 23 painting a room 51

**SECTION 4**

Functions and Parameters what are they? 57

Example 24 using functions 60

Validation again using Boolean results 61

Procedures and Parameters source data and results data 63

Example 25 actual and formal parameters 63

More on Parameters local and global parameters 70

**SECTION 5**

Files and File Processing storing data on disk 75

Text Files writing to and reading from text files 75

Typed Files writing to and reading from typed files 77

Example 26 creating a file of student records 77

**SECTION 6**

Sorting the need to sort data 95

Example 27 the bubble sort 95

Recursion powerful....but what is it? 99

**APPENDIX 1**

The Final Challenge updating one file from another 107**PROGRAMMING IN PASCAL**

## **SECTION 1**

## **Introduction**

Pascal is an example of a *high level* computer programming language. There are many other programming languages and they each have their own advantages and disadvantages.

This course aims to teach you the basics of the language. We'll start with some easy examples and work our way up. Don't be afraid to experiment and don't take things at face value; ask questions - it's the best way to learn.

## **Getting Started**

We'll type in a short Pascal program and demonstrate how it works. Pascal recognizes certain instructions and *keywords* - we'll type these in capital letters, while anything else will be in small letters. Make sure you use spaces and punctuation exactly as shown here in the examples.

**Example 1**

load up your version of Pascal

type in this program - use your own name instead of A Programmer!

PROGRAM my\_first; {short demonstration program}

VAR {by A Programmer}

index : INTEGER;

BEGIN

FOR index := 1 TO 10 DO

BEGIN

WRITELN(index)

END

END.

save your program giving it the name **my\_prog.pas******

When you've written a program and typed it in, then the next stage is to *compile* it. A compiler checks through your program looking for *syntax errors* - any obvious mistakes that you might have made, or instructions that Pascal can't understand.

If there are syntax errors, you'll need to correct them before going any further. This is sometimes the most difficult part of getting a program to work properly - check spellings and punctuation carefully!

When your program compiles successfully you are ready to run the program and see if it does what it is supposed to...

run the program and note what happens

Now for some comments - read them carefully and don't be tempted to skip over this part because it will help you understand what's coming next. We'll look at each line in turn:

PROGRAM my\_first; {short demonstration program}

All Pascal programs start with the keyword PROGRAM followed by a name and then a semicolon. The rest of this line is enclosed by curly brackets. Anything in curly brackets is ignored by the computer - the reason it is there, though, is to act as a *comment* and to help the reader see what each part of the program does. When you write your own programs you should always include such comments.

VAR {by A Programmer}

VAR is short for *variable*. If your program uses any numbers - or variables - then this is where we say what they are called and what sort of variables they are. As before, the comment in curly brackets is ignored by the computer.

index : INTEGER;

...our program uses just one variable. It is called **index** and it is a whole number, or *integer*.

Now we come to the start of the main program. It begins, surprisingly enough, with...

BEGIN

Notice that the lines are now set in a little way from the left margin. This is called *indenting* and helps to make the program easier to read.

FOR index := 1 TO 10 DO

This is the start of what is called a *loop*. A loop is an instruction (or set of instructions) which is carried out repeatedly - this is exactly what computers are good at!

BEGIN

...marks the start of the instruction(s) in the loop

WRITELN(index)

...is the only instruction in the loop. It prints out the value of the variable **index**. Notice, again, that it has been indented.

END

...marks the end of the loop and

END.

...marks the end of the program. Note that there is only ever one full stop in a Pascal program, right at the end.

Let's make one or two changes to the program:

load **my\_prog.pas** if it isn't already

change line 6 to read FOR index := 1 TO 20 DO

compile the program

run the program and note what happens

change line 8 to read WRITELN('hello world')

compile and run this program

change line 8 to read WRITELN(index, ' times 3 is ', index \* 3)

compile and run this program

So far, we've seen that a Pascal program is made up of a number of instructions. The file containing these instructions is compiled before the program can be run.

Right now, you shouldn't worry too much if some of this seems a little strange. We'll start with some simple examples and take it from there...

**Example 2**

choose **New** from the **File** menu and type in our next example:

PROGRAM stamps; {calculates the cost of stamps}

VAR {by A Programmer}

cost : REAL;

number : INTEGER;

total : REAL;

BEGIN

cost := 0.65;

WRITELN('enter the number of stamps');

READLN(number);

total := number \* cost;

WRITELN('you ordered ', number, ' stamps');

WRITELN('the total cost is ', total)

END.

save the program as **stamps.pas******

compile and run the program

It should be obvious that the result is not what you might have expected. To explain why that is, let's look more closely at what's happening. Firstly, the program uses three numbers, or variables, called **cost, number** and **total**. The one called **number** is an integer (a whole number) because it doesn't make much sense to have, say, 0.7 of a stamp! The other numbers, however - called **cost** and **total** - are not, of course, always going to be whole numbers and so they are described as type REAL which means they can have a decimal part. That's exactly what has happened and it's just that the answer is not written in a way that is clear to us. We can solve it though...

change the second last line to this:

WRITELN('the total cost is ', total :5:2);

This is just a bit of *formatting* so that, when the number **total** is printed, 5 spaces will be allowed for it and there will be 2 numbers after the decimal point. Easy, see...

The program you've just done is different from the first one in that the user had to enter information when the program is run. In other words, it is *interactive* as, indeed is most of the software that you use. An improvement that we might consider making is to allow the user to say what the price of each stamp is, rather than assume that it's 65c. How could you make the necessary changes? Here's a clue: you'll need to replace the line cost := 0.65; with two lines that let the user type in the cost of a stamp.

Here's another clue: the two lines will be similar to the part of the program that asks the user to type in the number of stamps...

**See your teacher if you're not sure how to do this.**

make the changes to the program

compile and run the program

check that it works

## **Designing Programs**

In order to write a program, you first need to decide exactly what it is supposed to do. That might sound obvious but if you make mistakes at this stage it's unlikely that your program will work properly. There are four important processes to consider:

analyze the problem, decide what the program is meant to do and *design a solution***

*code* the program - type in the Pascal code

*test* the program - check that it produces correct results

*evaluate* the solution - does it do what it's supposed to? Could it be improved?

We'll run through the following example to show you how the process works.

**Example 3**

A bus company requires a program which will calculate the cost of a journey given the rate per mile and the length of the journey. For example, if the company charges $0.75 per mile and the journey is 15 miles then the cost of the journey is 0.75 x 15 = $11.25

*1. Design a Solution*

Many programs follow a basic design that looks something like this:

1. input information

2. process the information

3. output the results

We'll use that approach to solve our example and start with the following:

1. get information from user

2. calculate cost of journey

3. print out results

We now take each of these three steps in turn and write down, in more detail, what each one does. The first step is to ask the user to enter the information required. What information do we need? Remember that the user needs to be *prompted*, or told, what to type in, otherwise they won't know what to do...

1.1 ask user to enter rate per mile

1.2 read in rate per mile

1.3 ask user to enter mileage

1.4 read in mileage

Notice the numbering system - step 1 has been broken down into four separate steps 1.1 to 1.4

The second step is fairly simple and can be described in one line...

2.1 calculate cost = rate x mileage

Step 3 is also straightforward...

3.1 print the mileage

3.2 print the rate per mile

3.3 print the cost

So we started with a simple design and refined it, putting in the necessary detail. The complete design is shown below:

1.1 ask user to enter rate per mile

1.2 read in rate per mile

1.3 ask user to enter mileage

1.4 read in mileage

2.1 calculate cost = rate x mileage

3.1 print the mileage

3.2 print the rate per mile

3.3 print the cost

It is important to note that the reason for doing this is not to make extra work for ourselves - it's so that we can use the design to code the program.

*2. Code the Program*

The program needs to use three numbers - the number of miles, the rate per mile and the cost of the journey. We now need to decide i) what to call these numbers, an identifier and, ii) what type of numbers they are. Here's our suggestion, listed in a table

| identifier | type |
| --- | --- |
| **rate****** | REAL |
| **miles** | INTEGER |
| **cost** | REAL |

Remember that whole numbers are INTEGERs. Numbers which might have a decimal part are called REAL numbers. So, now for the code...

PROGRAM bus\_journey; {to calculate journey cost}

VAR {by A Programmer}

rate : REAL;

miles : INTEGER;

cost : REAL;

BEGIN

WRITELN('enter the rate per mile ');

READLN(rate);

WRITELN('enter the number of miles ');

READLN(miles);

cost := rate \* miles;

WRITELN('number of miles = ', miles);

WRITELN('rate per mile = $', rate);

WRITELN('cost of journey = $', cost)

END.

Notice how closely the code corresponds to our design.

type in the program and save it as **bus.pas******

compile and run the program

Again, you'll see that the results are not what you perhaps expected.

edit the last but one and last but two lines to read:

WRITELN('rate per mile = $', rate :5:2);

WRITELN('cost of journey = $', cost :5:2);

compile and run the program

explain why it was not necessary to edit the line

WRITELN('number of miles = ', miles);

We're going to make one or two more changes now...

edit line 7 to read

WRITE('enter the rate per mile ');

(notice we're using WRITE instead of WRITELN)

and edit line 9 to read

WRITE('enter the number of miles ');

compile and run the program

describe what difference the changes make when you run the program:

which do you prefer?

save this version of the program

*3. Testing the Program*

Once you have the program working, you should test it to make sure it works properly. For example, we might draw up a table like the one below and check out various possibilities. What happens if you enter 6.5 for the number of miles? It is, after all, supposed to be a whole number.

copy and fill in the rest of this table

| **rate****** | **miles****** | expected answer | result or comment |
| --- | --- | --- | --- |
| 2 | 50 |  |  |
| 0.25 | 100 |  |  |
| 0 | 100 |  |  |
| 3 | 6.5 |  |  |
| 3 | mmm |  |  |

A summary of the results might go something like:

"The program gives correct results for whole numbers. If the user enters a decimal number for the number of miles then a 'run-time error' occurs and the program stops. This also happens if the user enters a letter instead of a number"

*4. Evaluation*

An evaluation should say whether the program does the job that is was designed for and whether it could be improved. For example:

"The program correctly calculates the cost of a journey based on the information provided by the user. Run-time errors occur if the user doesn't enter the correct type of data and it would be better if the program would allow the user to re-enter incorrect data instead of just stopping."

**Example 4**

A gardener requires a program which will calculate the length of fencing needed for a rectangular garden, given that she knows the length and width.

*1. Design a Solution*

Using a similar approach to the last example, we'll start with the following:

1. get information from user

2. calculate length of fence

3. print out results

As before, we take each of these steps in turn and write down in more detail what each one does. What information do we need? How do we calculate the length of fencing?

Step 1 becomes:

1.1 ask user to enter length of garden

1.2 read in the length

1.3 ask user to enter width of garden

1.4 read in the width

Step 2 becomes:

2.1 total length of fencing is 2 x length + 2 x width

Step 3 becomes:

3.1 print the length

3.2 print the width

3.3 print the total

The complete design is shown below.

1.1 ask user to enter length of garden

1.2 read in the length

1.3 ask user to enter width of garden

1.4 read in the width

2.1 total length of fencing is 2 x length + 2 x width

3.1 print the length

3.2 print the width

3.3 print the total

*2. Code the Program*

The program needs to use three numbers - the length and width of the garden and the total length of fencing. What type of numbers should they be - whole numbers or decimal numbers?

decide what type of numbers you should use - INTEGER or REAL - then copy the table into your work book and complete it.

| identifier | type |
| --- | --- |
| **length****** |  |
| **width****** |  |
| **total****** |  |

open your Pascal editor and type in the code for the program - you can use the last example as a guide.

save your program as **fencing.pas******

compile and run the program

*3. Testing the Program*

When you've got the program running, you need to test it.

draw up a table similar to the one in the previous example and choose some suitable numbers to test your program

write down a short summary of the results

*4. Evaluation*

Have a look at the evaluation for the last example and use it as a guide for this one.

write an evaluation of your program

**Example 5**

A bar manager would like a program which calculates the darts score when a player throws three darts. The program should print out the three scores and their total.

*1. Design a Solution*

write down a design for your solution as we have in the last two examples

show the completed design to your teacher

*2. Code the Program*

type in the code for your program

save the program as **darts.pas******

compile and run the program

*3. Test the Program*

as before, draw up a table and choose some suitable numbers to test the program

write a short summary of the results

*4. Evaluation*

write a note giving an evaluation of the program

show this to your teacher

**Example 6**

A teacher would like a program that calculates the average mark for students who sit three tests. Each mark is out of 60 and the program should print out the total mark and the average mark.

*1. Design a Solution*

write down a design for your solution as we have in the last three examples

show the completed design to your teacher

*2. Code the Program*

type in the code for your program

save the program as **average1.pas******

compile and run the program

*3. Test the Program*

as before, draw up a table and choose some suitable numbers to test the program

write a short summary of the results

*4. Evaluation*

write a note giving an evaluation of the program

show this to your teacher

**Example 7**

A newspaper sports editor would like a program which calculates the numbers of points that a soccer team has. Teams get 2 points for a win, 1 for a draw and 0 if they lose.

*1. Design a Solution*

write down a design for your solution as we have in the last few examples

show the completed design to your teacher

*2. Code the Program*

type in the code for your program

save it as **soccer.pas******

compile and run the program

*3. Test the Program*

as before, draw up a table and choose some suitable numbers to test the program

write a short summary of the results

*4. Evaluation*

write a note giving an evaluation of the program

show this to your teacher

## **Text Variables**

All the programs you've done so far have used *numeric* variables - ie numbers. Each variable is of a particular type - real or integer - and each has its own name. Variables can be used in calculations as, for example:

average := total / 3;

In this case, **average** is calculated as having the value of **total** divided by 3. There are, however, other types of variables...

Variables used to represent text are often called *string* variables. An example would be a variable containing your name.

**Example 8**

type in the following program then compile and run it

PROGRAM text; {using text variables}

VAR {by A Programmer}

name : STRING\[10\];

age : INTEGER;

BEGIN

name := 'A Programmer'; {use your name here}

age := 15;

WRITELN('my name is ', name);

WRITELN('my age is ', age)

END.

The variable called **name** is defined as a string variable in line 3:

name : STRING\[10\];

The number 10 in the square brackets means that the string can have up to 10 letters, or *characters*, in it. This program, of course, doesn't do a great deal. Apart from anything else, it prints the same thing every time you run it.

edit the program to look like this:

PROGRAM text; {using text variables}

VAR

name : STRING\[10\];

age : INTEGER;

days : INTEGER;

BEGIN

WRITE('enter your name : ');

READLN(name);

WRITE('enter your age : ');

READLN(age);

days := 365 \* age;

WRITELN('hello ', name);

WRITELN('you are ', age);

WRITELN('you must be at least ', days, ' days old!')

END.

save the program as **age.pas******

At least this program produces different output depending on what you type in. You'll notice that a couple of the instructions used WRITE instead of WRITELN. Can you remember what difference it makes?

edit your program to use WRITELN instead of WRITE

write a short description of the difference in your work book

explain which of the two you think worked better

explain what happens if you type in a name with more than 10 letters

## **Semicolons...**

You have probably noticed that some lines in your Pascal programs have a semicolon at the end, and some don't. Sometimes, if you forget to put a semicolon at the end of a line, the compiler will report that as an error and refuse to compile your program - it's an easy mistake to make and everyone does it from time to time.

But what are the rules? When is a semicolon required and when does it not matter?

You need to be aware that semicolons are there because they *separate* one Pascal statement from the next so that the compiler knows where one statement ends and another begins. Here's an example from the program you've just done:

WRITELN('you are ', age);

WRITELN('you must be at least ', days, ' days old!')

END.

The semicolon separates the two WRITELN statements but notice that we do **not** need a semicolon at the end of the second last line - END is a *keyword*, not a statement, so it doesn't need a semicolon to separate it from the statement on the previous line.

**Example 9**

This next program is going to ask the user to enter their name, the number of marks they got in a test and the number of marks that the test is out of. We then calculate the percentage and print out the result. For example, Steve Shark might have scored 15 out of 20 and this is 75%

*1. Design a Solution*

write down a complete design for your program

show the design to your teacher

*2. Code the Program*

type in the code for your program

save it as **percent.pas******

compile and run the program

*Test the Program*

as before, draw up a table and choose some suitable data to test the program

write a short summary of the results

*Evaluation*

write a note giving an evaluation of the program

show this to your teacher

**Example 10**

A youth club runs a disco every Friday, Saturday and Sunday. They sell different flavors of chips at 65c per bag. The youth club requires a program which adds up the total number of bags of chips of a particular flavor sold on the three nights and calculates the total money raised.

*1 Design a Solution*

Our first attempt is:

1. get information from user

2. calculate money raised

3. print out results

Step 1 becomes:

1.1 ask user to enter flavor of chips

1.2 read in flavor

1.3 ask user for number sold on Friday

1.4 read in number sold on Friday

1.5 ask user for number sold on Saturday

1.6 read in number sold on Saturday

1.7 ask user for number sold on Sunday

1.8 read in number sold on Sunday

Step 2 becomes:

2.1 calculate total bags sold

2.2 calculate total money raised

Step 3 becomes:

3.1 print out flavor

3.2 print number of bags sold

3.3 print total money raised

The complete design is shown below:

1.1 ask user to enter flavor of chips

1.2 read in flavor

1.3 ask user for number sold on Friday

1.4 read in number sold on Friday

1.5 ask user for number sold on Saturday

1.6 read in number sold on Saturday

1.7 ask user for number sold on Sunday

1.8 read in number sold on Sunday

2.1 calculate total bags sold

2.2 calculate total money raised

3.1 print out flavor

3.2 print number of bags sold

3.3 print total money raised

*2. Code the Program*

look again at what the program needs to do and decide how many variables you need

what type of variables are they?

what will you call them?

if you're not too sure, then see your teacher before you go any further

use the design above and type in the code for the program

save the program as **chips1.pas******

compile and run the program

*Test the Program*

draw up a table and choose some suitable test data

write a short summary of the results

*4. Evaluate the Solution*

write a report on your solution and suggest any improvements that you could make

*\[From now on we're not always going to ask you to do steps 3 and 4 ie to test the program and evaluate it. That's not because it isn't important, but because we think you should really do it as a matter of course and without needing to be asked every time. If it's necessary to look at this aspect for any particular examples then we will say so.**** See your teacher if there's any doubt****.\]***

**Example 11**

The school PE department requires a program which will calculate average times run by students in the 100yds event. The program should ask for the student's name, their home room class and the best three times that the student has run. The results printed out should show the student's name, their home room class and their average time.

*1. Design a Solution*

use the previous examples to help you design a solution to the problem.

show the design to your teacher

*2. Code the Program*

decide what variables you need to use in the program

as before, if you're not too sure, then see your teacher before you go any further

use your design and type in the code for the program

save the program as **sports.pas******

compile and run the program

## **Decisions, decisions...**

Our programs so far have broken down into a list of steps, one after the other. Sometimes, however, we need to make decisions and choose between two or more options.

Pascal uses the keywords IF, THEN and ELSE when making choices.

**Example 12**

This is a simple program that reads in a person's age and prints out a message.

type in the program below

save it as **voting.pas******

PROGRAM voting; {to decide if you can vote or not}

VAR

age : INTEGER;

name : STRING\[20\];

BEGIN

WRITE('enter your name ');

READLN(name);

WRITE('enter your age ');

READLN(age);

WRITELN('hello ', name);

IF age < 18

THEN

WRITELN('you are too young to vote')

ELSE

WRITELN('vote for the purple party!')

END.

run this program and check it using different input data

Note that only one of the two messages is displayed, depending on the person's age.

**Example 13**

Here's another example. It reads in a person's test mark and prints a 'pass' or 'fail' message.

type in the program

save it as **passfail.pas******

PROGRAM exam; {pass or fail an exam}

VAR

name : STRING\[20\];

mark : INTEGER;

BEGIN

WRITE('enter your name ');

READLN(name);

WRITE('enter your mark ');

READLN(mark);

IF mark > 50

THEN

BEGIN

WRITELN('hi ', name);

WRITELN('you scored ', mark);

WRITELN('well done, you passed')

END

ELSE

BEGIN

WRITELN('sorry ', name);

WRITELN('you scored ', mark);

WRITELN('you failed, better luck next time')

END

END.

compile and run the program

check it using different data

**Example 14**

This is a game for two players. The program should ask one of the players to enter the name of a country and then the name of its capital. The screen is cleared and the program should then ask the other player to enter the capital of the country and print an appropriate message, depending on whether the answer is right or wrong.

*1. Design a Solution*

Our first attempt looks like this:

1. get information from player 1

2. get answer from player 2

3. print appropriate message

Step 1 becomes:

1.1 prompt player 1 for country

1.2 read in country

1.3 prompt player 1 for capital

1.4 read in capital

1.5 clear the screen

Step 2 becomes:

2.1 prompt player 2 for answer

2.2 read in answer

Step 3 is the crucial one and becomes:

3.1 if answer is correct

3.2 then

3.3 print 'correct' message

3.4 else

3.5 print 'incorrect' message

So the complete design is:

1.1 prompt player 1 for country

1.2 read in country

1.3 prompt player 1 for capital

1.4 read in capital

1.5 clear the screen

2.1 prompt player 2 for answer

2.2 read in answer

3.1 if answer is correct

3.2 then

3.3 print 'correct' message

3.4 else

3.5 print 'incorrect' message

*2. Code the Program*

type in the following program

you should note that CLRSCR - the instruction to clear the screen - may be different on some machines; see your teacher if you're not sure

PROGRAM quiz; {a quiz game}

VAR

country : STRING\[8\];

capital : STRING\[8\];

answer : STRING\[8\];

BEGIN

WRITE('enter name of country ');

READLN(country);

WRITE('enter name of capital ');

READLN(capital);

CLRSCR;

WRITE('what is the capital of ', country, '?');

READLN(answer);

IF answer = capital

THEN

BEGIN

WRITELN('the capital of ', country, ' is ', capital);

WRITELN('well done, you got it right')

END

ELSE

BEGIN

WRITELN('sorry, you got it wrong');

WRITELN('the correct answer is ', capital)

END

END.

save the program as **cities1.pas******

compile and run the program

*3. Test the Program*

copy and complete this table for the different test data shown

| country | capital | answer | result |
| --- | --- | --- | --- |
| France | Paris | Paris | correct |
| France | Paris | paris |  |
| France | Paris | 77 |  |
| Venezuela | Caracas | Caracas |  |
| USA | Washington | Washington |  |

A summary of the results might be:

"The program gave correct results when the answer matched the capital exactly - it is *case-sensitive* in as much as upper and lower case letters have to be the same. For example, "Paris" is not the same as "paris". If the user enters a number instead of some text then the answer will be wrong but it will not cause a 'run-time error'.

If the text is longer than the string - eight characters, in this case - then the word is simply shortened to fill the space allowed."

*4. Evaluate the Solution*

An evaluation of the program might be:

"The program meets the design specification and produces correct results when tested. Many improvements are, however, possible. An obvious one would be so that the user could use either upper or lower case letters - provided, of course, that the spelling was correct. The program could be developed such that a number of questions were asked and the user could then be given a score."

**Example 15**

A large electronic scoreboard in a sports stadium displays the scores of the two teams during a game. At the end of the game we want it to display a 'congratulations' message to the winning team. A program is required which asks the user to enter the names of the two teams and the number of points scored by each. The program will then print out an appropriate message.

*1. Design a Solution*

as before, design a suitable solution

show the completed design to your teacher

*2. Code the Program*

type in the code for your program

save it as **scores.pas******

compile and run the program

*3. Test the Program*

use suitable data to test your program and note the results

There is an obvious flaw in the specification. Does your test data reveal the problem? See your teacher if you're not sure.

*4. Evaluate the Solution*

Can you describe the problem with the design and suggest how it might be solved?

write an evaluation note and indicate improvements that could be made

**Example 16**

Those earning over a certain amount have to pay income tax. To keep the figures simple we'll say that if you earn less than $5000 you pay no income tax, otherwise you pay 25% of anything over $5000. A person earning $4500 would therefore pay no tax but someone earning $5500 would pay 25% of $500, ie $125 in tax.

**See your teacher now if you're not sure how this works.**

We would like a program which asks the user to enter the amount earned and which then calculates the tax paid, if any, and prints out the results.

*1. Design a Solution*

as before, design a suitable solution

show the completed design to your teacher

*2. Code the Program*

type in the code for your program

save it as **taxes.pas******

compile and run the program

## **Over and over ...**

A loop is part of a program that gets repeated a number of times. The very first Pascal program you did had a loop in it. Loops can be *conditional* in which case they repeat until something happens - a *condition* is met - or they can be *unconditional*, in which case they are repeated for a fixed number of times. You've already seen an example of an unconditional loop - look back at the first program in this tutorial. The loop starts with...

FOR index := 1 TO 10 DO

... and the instruction(s) to be repeated go between a BEGIN and an END statement:

BEGIN

WRITELN(index)

END

In this case the variable called **index** is a *counter* which controls the loop - it starts at 1 and goes up to 10

******i) Unconditional Loops **

Recall Example 6 where a teacher wanted to read in three marks and calculate the average. Now consider what would happen if there were 10 or 20 or 200 marks...

...well this is what loops are designed for and if we know in advance how many times the loop is to be repeated, then so much the better!

Here's a different design for the program. As each mark is read in, we're going to keep a running total:

1. get information from user

2. calculate average

3. print results

Step 1 becomes:

1.1 set total to zero

1.2 loop for each student

1.3 prompt user to enter mark

1.4 read in the mark

1.5 update the total

1.6 end loop

Step 2 is:

2.1 average = total / number of marks

Step 3 is:

3.1 print out the total marks

3.2 print out the average mark

So the complete design looks like this:

1.1 set total to zero

1.2 loop for each student

1.3 prompt user to enter mark

1.4 read in the mark

1.5 update the total

1.6 end loop

2.1 average = total / number of marks

3.1 print out the total marks

3.2 print out the average mark

type in this program and save it as **average2.pas**

PROGRAM unconditional;

VAR

mark : INTEGER;

total : INTEGER;

average : REAL;

BEGIN

total := 0;

FOR counter = 1 TO 10 DO

BEGIN

WRITE ('type in the exam mark: ');

READLN (mark);

total := total + mark

END;

average := total / 10;

WRITELN('the total is: ');

WRITELN('the average is: ', average)

END.

there are two mistakes in the program which means that it won't compile until you find them - can you see what they are?

there are two more mistakes that you should be able to find when you run the program - can you fix them?

Here's a better design that lets the user decide how many students there are:

1.1 set total to zero

1.2 prompt user to enter number of students

1.3 read in number of students

1.4 loop for each student

1.5 prompt user to enter mark

1.6 read in the mark

1.7 update the total

1.8 end loop

2.1 average = total / number of students

3.1 print out the total marks

3.2 print out the average mark

can you make the necessary changes to your program?

**See your teacher if you're not sure how to do this.**

Notice in this example what is meant by a 'running total' and notice also the line in the program that updates this total.

**ii) Conditional Loops**

Now for a conditional loop. This is where you don't know in advance how many times you're going to have to go round the loop - you need to loop *until* something happens to stop the loop, or until a *condition* is met.

type in this program

PROGRAM conditional; {a conditional loop}

VAR

number : INTEGER;

guess : INTEGER;

BEGIN

number := 5;

REPEAT

WRITE('enter a number between 0 and 10: ');

READLN(guess);

UNTIL guess = number;

WRITELN('what took you so long?')

END.

compile and run the program

As you can see, the loop is repeated until the number typed in is 5.

**Example 17**

We'll extend the idea now so that one user types in a number and the other person tries to guess it...

*1. Design a Solution*

Here's our design for the guessing game.

1. get number from player 1

2. get guess(es) from player 2 until guess is correct

3. print message

Step 1 becomes:

1.1 prompt player 1 for number

1.2 read in number

1.3 clear the screen

Step 2 becomes:

2.1 repeat

2.2 prompt player 2 for guess

2.3 read in guess

2.4 until guess is correct

So the complete design is:

1.1 prompt player 1 for number

1.2 read in number

1.3 clear the screen

2.1 repeat

2.2 prompt player 2 for guess

2.3 read in guess

2.4 until guess is correct

3 print message

*2. Code the Program*

type in the code for the program

save it as **guess1.pas******

compile and run the program

**Example 18**

We'd like now to extend the design of the previous program and add one or two new features. It would be helpful if the program could give some clues and say whether the guess is too big or too small. It would also be helpful if the program could count the number of guesses and print the total at the end. We'll start our new design just like the original one:

*1. Design a Solution*

1. get number from player 1

2. get guess(es) from player 2 until guess is correct

3. print message

Step 1 becomes:

1.1 prompt player 1 for number

1.2 read in number

1.3 clear the screen

Step 3 becomes:

2.1 repeat

2.2 prompt player 2 for guess

2.3 read in guess

2.4 print clue

2.5 update number of guesses

2.6 until guess is correct

Step 2.4 needs some clarification - note how the numbering system works...

2.4.1 if guess > number

2.4.2 then

2.4.3 print "guess is too big"

2.4.4 if guess < number

2.4.5 then

2.4.6 print "guess is too small"

Step 3 becomes:

3.1 print message

3.2 print number of guesses

So the complete solution is:

1.1 prompt player 1 for number

1.2 read in number

1.3 clear the screen

2.1 repeat

2.2 prompt player 2 for guess

2.3 read in guess

2.4.1 if guess > number

2.4.2 then

2.4.3 print "guess is too big"

2.4.4 if guess < number

2.4.5 then

2.4.6 print "guess is too small"

2.5 update number of guesses

2.6 until guess is correct

3.1 print message

3.2 print number of guesses

*2. Code the Program*

As before, you should note that the whole point of designing the program is to make it easy to code. Check that the design above corresponds with the program below.

type in the program

PROGRAM guessing; {a guessing game}

VAR

number : INTEGER;

guess : INTEGER;

total : INTEGER;

BEGIN

WRITE('enter the number to guess ');

READLN(number);

CLRSCR;

REPEAT

WRITE('enter your guess ');

READLN(guess);

IF guess > number

THEN

WRITELN('guess is too big');

IF guess < number

THEN

WRITELN('guess is too small');

total := total + 1;

UNTIL guess = number;

WRITELN('well done');

WRITELN('you took ', total, ' guesses')

END.

save the program as **guess2.pas******

compile and run the program

This completes Part 1 of the tutorial, so well done if you've followed everything so far.

## **SECTION 2**

## **Introduction**

You've now covered some of the basic programming ideas and are now in a position to think in more detail about how best to make programs work for you. Solving problems can be a frustrating business but programming is meant to be fun too - remember that everyone makes mistakes and you shouldn't be surprised if your program doesn't work first time...

## **Procedures, procedures...**

All of the programs you've done so far have been fairly short. For more complex tasks though, clearly, the code for the programs is going to be more complicated and much longer. For this reason, and also because it's good practice, most programs are broken down into smaller sections called *procedures*. A procedure, then, is a section of code which does a particular job. This part of the course is a rather simplified treatment of some of the issues involved in using procedures. We should note that, as with most things, there is more to the topic than meets the eye but a more detailed treatment can be left for later.

**Example 19**

To illustrate the use of procedures, we'll use Example 10, the design for which is shown below:

1. get information from user

2. calculate money raised

3. print out results

...which led us to this:

1.1 ask user to enter flavor of chips

1.2 read in flavor

1.3 ask user for number sold on Friday

1.4 read in number sold on Friday

1.5 ask user for number sold on Saturday

1.6 read in number sold on Saturday

1.7 ask user for number sold on Sunday

1.8 read in number sold on Sunday

2.1 calculate total bags sold

2.2 calculate total money raised

3.1 print out flavor

3.2 print number of bags sold

3.3 print total money raised

Notice that, as with many designs, we start with a basic scheme with a small number of steps - in this case, three - and then take each of them in turn and write a more detailed description.

We wish to split our program into smaller 'chunks', or procedures, so we'll decide now that there will be three - one for each of the main steps 1, 2 and 3. Have a look at what each one does then decide on a name for the procedure in the same way that you choose names for variables.

step name

1. get information from user **get\_info******

2. calculate money raised **calc\_sales******

3. print results **results******

The main program now consists of the three procedures.

type in the code below

PROGRAM chips; {to calculate chip sales}

VAR

flavor : STRING\[10\];

friday : INTEGER;

saturday : INTEGER;

sunday : INTEGER;

bags : INTEGER;

sales : REAL;

BEGIN {main program starts here}

get\_info;

calc\_sales;

results

END.

compile the program

The error message that you get isn't really surprising since Pascal knows nothing of your three procedures! We need to describe what each procedure does. Let's take **get\_info** first and remind ourselves of the detailed description for step 1 as given in Example 10

1.1 ask user to enter flavor of chips

1.2 read in flavor

1.3 ask user for number sold on Friday

1.4 read in number sold on Friday

1.5 ask user for number sold on Saturday

1.6 read in number sold on Saturday

1.7 ask user for number sold on Sunday

1.8 read in number sold on Sunday

Our procedure will do just what is required for each of these steps. The code is shown below.

PROCEDURE get\_info; {to get details from user}

BEGIN

WRITE('enter flavor of chips ');

READLN(flavor);

WRITE('enter number sold on Friday ');

READLN(friday);

WRITE('enter number sold on Saturday ');

READLN(saturday);

WRITE('enter number sold on Sunday ');

READLN(sunday)

END;

Notice again how closely the instructions follow the detailed design. The code for the procedure is slotted in before the start of the main program so that we now have:

PROGRAM chips; {to calculate chip sales}

VAR

flavor : STRING\[10\];

friday : INTEGER;

saturday : INTEGER;

sunday : INTEGER;

bags : INTEGER;

sales : REAL;

PROCEDURE get\_info; {to get details from user}

BEGIN

WRITE('enter flavor of chips ');

READLN(flavor);

WRITE('enter number sold on Friday ');

READLN(friday);

WRITE('enter number sold on Saturday ');

READLN(saturday);

WRITE('enter number sold on Sunday ');

READLN(sunday)

END;

BEGIN {main program starts here}

get\_info;

calc\_sales;

results

END.

type in the extra code and save it as **chips2.pas******

compile the program

Again the error message should come as no surprise since we have only entered one of the three procedures so far. Step 2 looked like this and the procedure only has a couple of instructions in it...

2.1 calculate total bags sold

2.2 calculate total money raised

...and the code is...

PROCEDURE calc\_sales; {to calculate the sales}

BEGIN

bags := friday + saturday + sunday;

sales := 0.65 \* bags

END;

...and it slots into the program like this...

PROGRAM chips; {to calculate chip sales}

VAR

flavor : STRING\[10\];

friday : INTEGER;

saturday : INTEGER;

sunday : INTEGER;

bags : INTEGER;

sales : REAL;

PROCEDURE get\_info; {to get details from user}

BEGIN

WRITE('enter flavor of chips ');

READLN(flavor);

WRITE('enter number sold on Friday ');

READLN(friday);

WRITE('enter number sold on Saturday ');

READLN(saturday);

WRITE('enter number sold on Sunday ');

READLN(sunday)

END;

PROCEDURE calc\_sales; {to calculate the sales}

BEGIN

bags := friday + saturday + sunday;

sales := 0.65 \* bags

END;

BEGIN {main program starts here}

get\_info;

calc\_sales;

results

END.

it's your turn now to write the code for the procedure **results** and put it into the program

save the complete program

compile and run it and then show it to your teacher

Congratulations, you've just written your first Pascal procedure!

**Example 20**

Here's the first attempt at a design for Example 14 again:

1. get information from player 1

2. get answer from player 2

3. print appropriate message

Each of these three steps will become a procedure. Let's choose names for them as follows:

step name

1. get information from player 1 **get\_info**

2. get answer from player 2 **get\_answer******

3. print appropriate message **message******

So the program looks like this just now:

PROGRAM quiz; {a quiz game}

VAR

country : STRING\[8\];

capital : STRING\[8\];

answer : STRING\[8\];

BEGIN {main program starts here}

get\_info;

get\_answer;

message

END.

As before, though, if you try to compile this you'll get error messages because there are three procedures - **get\_info, get\_answer** and **message** - which we haven't yet coded. We'll now put in the first two of these and you can complete the other one yourself:

PROGRAM quiz; {a quiz game}

VAR

country : STRING\[8\];

capital : STRING\[8\];

answer : STRING\[8\];

PROCEDURE get\_info; {to get information from player 1}

BEGIN

WRITE('enter name of country ');

READLN(country);

WRITE('enter name of capital ');

READLN(capital);

CLRSCR

END;

PROCEDURE get\_answer; {to get answer from player 2}

BEGIN

WRITE('what is the capital of ', country, '? ');

READLN(answer)

END;

{the other procedure goes in here}

BEGIN {main program starts here}

get\_info;

get\_answer;

message

END.

enter the code above and save it as **cities2.pas******

the procedure **message** below has been done for you, except that the lines have been jumbled up - you need to put them in the right order and put the procedure in the correct place in the program...

PROCEDURE message; {to print an appropriate message}

ELSE

WRITELN('wrong - the answer is ', capital)

IF answer = capital

WRITELN('correct - well done!')

THEN

END;

BEGIN

**Example 21**

We'll go through a complete example now to make sure we've got the hang of things so far.

A company gets orders from its customers and gives a discount of 10% on orders worth more than $200. Whatever the total comes to, sales tax at 5% has to be added. A typical bill, or invoice, might look like this:

value = 220.00

discount = 22.00

subtotal = 198.00

sales tax = 9.90

total = 207.90

If the value is less than $200 then the discount would, of course, be zero but you would still need to add sales tax.

**See your teacher now if you're not sure how this works.**

*1. Design a Solution*

Our first attempt is:

1. get value of order

2. calculate total

3. print invoice

*\[HINT: already you should see that the main program looks like being made up of three procedures\]*

Step 1 is straightforward...

1.1 prompt user for value of order

1.2 read in value of order

Step 2 is more complicated...

2.1 if value is greater than $200

2.2 then

2.3 discount is 10% of value

2.4 else

2.5 discount is zero

2.6 subtotal is value - discount

2.7 sales tax is 5% of subtotal

2.8 total is subtotal + sales tax

Step 3 is simply

3.1 print value

3.2 print discount

3.3 print subtotal

3.4 print sales tax

3.5 print total

The complete design, then, looks like this:

1. get value of order

2. calculate total

3. print invoice

1.1 prompt user for value of order

1.2 read in value of order

2.1 if value is greater than $200

2.2 then

2.3 discount is 10% of value

2.4 else

2.5 discount is zero

2.6 subtotal is value - discount

2.7 sales tax is 5% of subtotal

2.8 total is subtotal + sales tax

3.1 print value

3.2 print discount

3.3 print subtotal

3.4 print sales tax

3.5 print total

So if we use **get\_value, calc\_total** and **invoice** for the procedure names, the outline of the program will look like this:

PROGRAM orders; {to print out an invoice}

VAR

value : REAL;

discount : REAL;

subtotal : REAL;

sales\_tax : REAL;

total : REAL;

{procedure get\_value goes here}

{procedure calc\_total goes here}

{procedure invoice goes here}

BEGIN {main program starts here}

get\_value;

calc\_total;

invoice

END.

type in the outline of the program as above and save it as **invoice.pas******

see your teacher now who will show you how to compile it without getting error messages

add the procedure **get\_value** and compile it to make sure there are no mistakes

add each of the other two procedures in turn, compiling the program after each one

save the complete program and run it.

If you've got this far and understood the course material then, once again, you've done well. There's more to learn, of course, but you've done much of the hard work!

An Introduction to Pascal Programming

An Introduction to Pascal Programming

PAGE 4© John Brewer 1999

PAGE 5

© 1999 John Brewer

An Introduction to Pascal Programming

An Introduction to Pascal Programming

PAGE 44

© John Brewer 1999

PAGE 43

© John Brewer 1999

© 1999 John Brewer

---
*Kaynak: `PROGRAMMİNG İN PASCAL/O-d-e-v-s-i-t-e-s-i-com-18911.doc` — jb — 1999*
