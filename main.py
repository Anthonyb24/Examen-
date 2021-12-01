

print("Anthony Ojo")


A="""In this part How count it? My experiences in ¡Supérate! Since 019 that I started there a lot of things 
that I have learned and these have gone of a lot of help in my life. However, these years as knowledge, as of
fears haven’t gone easy but having their advantages, and also knowing new topic and also having experiences. 

First year, I remember that this year I had that get used to manage. The first program that I remember is Python.
It for me was very difficult but the same time was every easy. I made a project with one partner about a hotel
where is all elements as price, rooms, and also if People can have a discount. Sincerely I liked this project
because I learned to use a new tool and also had an experience of working in team. 

Other experience was Filmora that is app for making videos. In this project I worked in teams of this way with 
make a video about one person sang, other was recording and other edited video.

Although, it is not only unique tools that   I had learned this year but these have highlighted my story here.

Second year, this year is when in Panama arrived the pandemic and for my and also I think that for others was a 
difficult year. But in this year I had other teacher in this way I can learned new thing as Power Bi where I made
some analysis with excel and I needed to use of information necessary in the project. Also, I learned about excel 
where I made different table about clients and also use a lot of design. As also use Hyperlink and some functions 
for use in the tables.  

Third year, I have learned a lot of things as I was working in excel for my test of excel. Where I learned about 
functions of mathematic, text and also other. On the hand I worked in different projects inside of it. Additionally
, I learned about Jupyter who is aplication for making code and making matrix in that."""

print(A)


print("https://superate2014-my.sharepoint.com/:w:/r/personal/anthony_ojo_provivienda_superate_org_pa/_layouts/15/Doc.aspx?sourcedoc=%7BA6C0CAD2-E523-46FD-9611-C49633CCE449%7D&file=Ensayo%20Informatica%2018-11-2021.docx&action=default&mobileredirect=true")



My_array=[1,3,4,5,3,1,7,7,7,7,7,7,7,8,9,8,9]


mayor = 0
Number=0

for i in My_array:
    secuences = My_array.count(i)
    
    if secuences>mayor:
       mayor = secuences
       Number = i
       
print("Longest")
print(mayor)
print("Number")
print(Number)


print()
print("Reykeel Acosta")

a = ['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a']
b = ['a', 'c', 'd', 'b', 'b', 'd', 'a', 'c']


print(a)
print(b)

Te = len(a)
n = len(a) // 2 

for i in range(n):
	if a[i] == a[Te - 1]:
		symmetric = True
	else:
		symmetric = False
		break
	Te = Te - 1

if symmetric:
	print("symmetric")
else:
	print("asymmetric")



Te = len(b)
n = len(b) // 2 

for i in range(n):
	if b[i] == b[Te - 1]:
		symmetric = True
	else:
		symmetric = False
		break
	Te = Te - 1

if symmetric:
	print("symmetric")
else:
	print("asymmetric")

