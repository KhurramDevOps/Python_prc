# Methods of string 
# Lowercase() method 10 examples. 
string1 = "HELLO"
print(string1.lower())

string2 = "HELLO WORLD"
print(string2.lower())

string3 = "Example OF Lower CASE"
print(string3.lower())

string4 = "LAHORE"
print(string4.lower())

string5 = "PIAIC"
print(string5.lower())

string6 =  "Pakistan"
print(string6.lower())

string7 = "Im LeArning GEN AI"
print(string7.lower())

string8 = "pyTHON IS AMazing"
print(string8.lower())

string9 = "HOW are YOU"
print(string9.lower())

string10 = "I am LEARNING"
print(string10.lower()) 
# Output: hello, hello world, example of lower case, lahore, piaic, pakistan, im learning gen ai,  python is amazing, how are you, i am learning

# Uppercase() method  10 examples. 
string1 = "hello"
print(string1.upper())

string2 = "hello world"
print(string2.upper())

string3 = "example of upper case"
print(string3.upper())

string4 = "lahore"
print(string4.upper())

string5 = "piaic"
print(string5.upper())

string6 = "pakistan"
print(string6.upper())

string7 = "im learning GEN AI"
print(string7.upper())

string8 = "PYTHon IS amazing"
print(string8.upper())

string9 = "how are you"
print(string9.upper())

string10 = "I AM LEARNING"
print(string10.upper())
# Output: HELLO, HELLO WORLD, EXAMPLE OF UPPER CASE, LAHORE, PIAIC, PAKISTAN,  IM LEARNING GEN AI, PYTHON IS AMAZING, HOW ARE YOU, I AM LEARNING

# titlecase() method  10 examples. 
city1 = "LAhore is the city of gardens"
print(city1.title())

city2 = "karachi is the city of lights"
print(city2.title())

city3 = "islamabad is the capital of paksitan"
print(city3.title())

city4 = "multan"
print(city4.title())

city5 = "faislabad"
print(city5.title())

city6 = "peshAWAR"
print(city6.title())

city7 = "QUETTA"
print(city7.title())

city8 = "sUKKUR"
print(city8.title())

city9 = "gWADar"
print(city9.title())

city10 = "hydERABAD"
print(city10.title())
# Output: Lahore Is The City OF Gardens, Karachi Is The City Of Lights,etc

# swapcase() method 10 examples 
name1 = "MUHHAMAD khurram"
print(name1.swapcase())

name2 = "muhhamad KHURRAM"
print(name2.swapcase())

name3 = "QUAID_E_azam"
print(name3.swapcase())

name4 = "mohmmad Ali"
print(name4.swapcase())

name5 = "ALLAMA iqbal"
print(name5.swapcase())


name6 = "hussain"
print(name6.swapcase())

name7 = "hassan"
print(name7.swapcase())

name8 = "FAISAL MOSQUE"
print(name8.swapcase())

name9 = "badshahi masjid"
print(name9.swapcase())

name10 = "islamic republic OF pakistan"
print(name10.swapcase())
# Output: muhammad KHURRAM, MUHHAMAD khurram,  quaid_e_AZAM, mohmmad ALI, allama IQBAL, etc

# capitalize() method  10 examples 
line1 = "hello world"
print(line1.capitalize())

line2 = "hello World Again"
print(line2.capitalize())

line3 = "hello WORLD AGAIN"
print(line3.capitalize())

line4 = "my name is khurram"
print(line4.capitalize())

line5 = "I AM THE STUDENT OF PIAIC"
print(line5.capitalize())

line6 = "im learning PYTHON"
print(line6.capitalize())

line7 = "my age is 18"
print(line7.capitalize())

line8 = "STATUE OF LIBERTY"
print(line8.capitalize())

line9 = "work hard"
print(line9.capitalize())

line10 = "saudi Arabia"
print(line10.capitalize())
# Output: Hello world, Hello world again, etc 

# casefold() method 10  examples.
# casefold method same work as  lower() method but it is more aggressive in removing case distinctions, so it is more preferable
text1 = "HEy EVERYONE"
print(text1.casefold())

text2 = "I AM THE STUDENT OF PIAIC"
print(text2.casefold())

text3 = "HOPE YOU aRE FINE"
print(text3.casefold())

text4 = "I AM FROM PAKISTAN"
print(text4.casefold())

text5 = "I AM MUSLIM"
print(text5.casefold())

text6 = "I AM FROM LAhore"
print(text6.casefold())

text7 = "lahore is so BEAUTIFUL"
print(text7.casefold())

# As WE know casefold() method helps with changing letters in lower case example 
text8 = "β" #this is german letter
print(text8)
answer2 = (text8.casefold()) #this wil print "ss"
print(answer2)
# here we use lower case method to judge the differene 
text9 = "β"
print(text9)
answer = (text9.lower()) #this will print "β" 
print(answer)
#conclusion: so both have same function to lower the words but casefold also support in other languages as you see above

text10 = "ö"
print(text10)
print(text10.casefold()) #this will print "o"

# Output: hey everyone,  i am the student of piaic, hope you are fine, i am from pakistan, etc

# centre() method  10 examples. 
msg1 = "country name pakistan "
new_string = msg1.center(24)
print(new_string)# here fillchar not provided so takes space by default.

msg2 = "Muhammad Khurram "
new_string2 = msg2.center(20)
print(new_string2)

msg3 = "mountains"
new_string3 = msg3.center(30)
print(new_string3)

msg4 = "thar desert"
new_string4 = msg4.center(35)
print(new_string4)

msg5 = "indus river"
new_string5 = msg5.center(25)
print(new_string5)

msg6 = "indus valley civilization"
new_string6 = msg6.center(40)
print(new_string6)

msg7 = "abracadabra"
new_string7 = msg7.center(20,"*")
print(new_string7)

msg8 = "horror house"
new_string8 = msg8.center(25,"#")
print(new_string8)

msg9 = "indian subcontinent"
new_string9 = msg9.center(35,"-")   
print(new_string9)  

msg10 = "pacific ocean"
new_string10 = msg10.center(30,"^")
print(new_string10)

# endswith() method   10 examples. 
statment1 = "my name is khurram"
print(statment1.endswith("ram")) # this will print True

statement2 = "wow amazing"
print(statement2.endswith("ing")) # this will print True

statement3 = "hello friend"
print(statement3.endswith("ends")) # this will print false

statement4 = "nice work"
print(statement4.endswith("ing")) # this will print false

statement5 = "wonderful picture"
print(statement5.endswith("ture")) # this will print True

statement6 = "beautiful house"
print(statement6.endswith("ouse",12,15)) # this will print False

statement7 = "beautiful room"
print(statement7.endswith("room",10,16)) # this will print True

statement8 = "python practice"
print(statement8.endswith("ice",12,17)) # this will print True

statement9 = "python is interesting"
print(statement9.endswith("interesting",0,20)) # this will print false

statement10 = "i love my mother"
print(statement10.endswith("mother",5,10)) # this will print False

# expandtab() method    10 examples. 
var1  = "hello\tworld"
print(var1.expandtabs(10)) # this will print hello     world

var2 = "name\tkhurram"
print(var2.expandtabs(15)) 

var3 = "python\tis\tfun"
print(var3.expandtabs(20)) 

var4 = "i love\tmy\tfamily"
print(var3.expandtabs(25)) 

var5 = "my age\tis\t18"
print(var5.expandtabs(30)) 

var6 = "i am\tfrom\tlahore"
print(var6.expandtabs(35))

var7 = "my name\tis\tkhurram"
print(var7.expandtabs(28))

var8 = "i love\tmy\tcity"
print(var8.expandtabs(32))

var9 = "learning is \tmy\thobby"
print(var9.expandtabs(36))

var10 = "i \tlove\tpakistan"
print(var10.expandtabs(40))

# find() method 10 examples
sample1 = "this is chair"
print(sample1.find("is")) # this will print 2

sample2 = "i love my family"
print(sample2.find("my")) # this will print 7

sample3 = "python is fun"
print(sample3.find("fun")) # this will print 10

sample4 = "minar-e-pakistan"
print(sample4.find("e")) # this will print 6

sample5 = "i love my pakistan"
print(sample5.find("pakistan")) # this will print 10

sample6 = "karachi is the city of the lights"
print(sample6.find("i",7)) #this  will print 8

sample7 = "khurram khurram"
print(sample7.find("khurram",7)) #this will  print 8

sample8 = "sahara desert is the big desert"
print(sample8.find("desert",13,)) #this will print 25

sample9 = "mountain everest is  the highest mountain"
print(sample9.find("mountain",8)) #this will print 33

sample10 = "islamabad is the capital of the pakistan"
print(sample10.find("the",16)) #this will print 28
