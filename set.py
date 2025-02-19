Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#set
my_set=(1,2,3,4,5)
my_set
(1, 2, 3, 4, 5)
my_set1=set("hello")
my_set1
{'l', 'o', 'e', 'h'}
##set from list
new_set=set([1,2,3,4])
new_set
{1, 2, 3, 4}
##set of characters so it will add one by one all character
my_set=set("mango")
my_set
{'o', 'a', 'm', 'g', 'n'}
##You can pass tuple to set
my_set=set((1,2,3,4))
my_set
{1, 2, 3, 4}
##ordered set
my_set={4,2,6,1,8}
my_set
{1, 2, 4, 6, 8}
##Add element into set
my_set.add("C++")
my_set
{1, 2, 4, 6, 8, 'C++'}
>>> ##Set of Differnent Data types
>>> new_set={1,"apple",1.1,"true}
...          
SyntaxError: unterminated string literal (detected at line 1)
>>> new_set={1,"apple",1.1,true}
...          
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    new_set={1,"apple",1.1,true}
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> new_set={1,"apple",1.1,'true'}
...          
>>> new_set
...          
{1.1, 'apple', 1, 'true'}
>>> ##Remove a set
...          
>>> new_set.remove(1.1)
...          
>>> new_set
...          
{'apple', 1, 'true'}
>>> ##POP element of set
...          
>>> new_set.pop()
...          
'apple'
>>> my_set
...          
{1, 2, 4, 6, 8, 'C++'}
>>> new_set
...          
{1, 'true'}
>>> ##clear element
...          
>>> new-set.clear()
...          
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    new-set.clear()
NameError: name 'new' is not defined
>>> new_set.clear()
...          
>>> new_set
...          
set()
