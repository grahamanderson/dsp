# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>>Tuples, you can't add/delete objects from it. Lists, you can add/delete/amend/whatever-you-want.  Both sequences of elements.
For syntax, tuples use parens, lists use brackets.
Tuples are much faster for searching. Tuples great for storing contants.

Dictionary keys must be immutable––Tuples are immutable. 
Lists are disqualified as they can be added/amended/deleted


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>>In sets, there are no duplicate elements. Sets are much faster. In lists, elements can be overwritten, changed, assigned. 
As there are no duplicate elements, sets are faster. At times (like in 05b), I use sets to find unique values

```
list_array = ['apple', 'pear', 'orange']
set = {'dali', 'nihilist', 'surrealism'}
```




---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

lambda allow you to create small anonymous functions...great when when the function is simple and you don't want to write a formal one with all the syntax and such. Especially true when working row/col calcs in Pandas

>>Lambda example––stripping whitespace from column names in a dataframe(used in 05b-python)

```
df.rename(columns=lambda x: x.strip())
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>>List comprehension are a way to iterate over items in a list. 
You can also use lambda for this task--especially works well with pandas


```
# List Comprehension: Count how many p items in large sample >= .18
over_18_count = len([p for p in large_sample if p>= .18])
```

>>Maps applies a function to items in a list
Works particularly well with lambda

```
# Map Example
# Square every item in the items array. Myself, I prefer numpy which allows you  easy array calcs(below) 
items = [1, 2, 3, 4, 5]
list(map((lambda x: x**2), items))

# Numpy example (more elegant, imo)
a = np.array([2,3,4])*2) = [4,6,8]

```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
from datetime import datetime
date_format = '%m-%d-%Y'
date_start = '01-02-2013'    
date_stop = '07-28-2015'

def delta_calc(date_start, date_stop, date_format):
    a = datetime.strptime(date_start, date_format)
    b = datetime.strptime(date_stop, date_format) 
    delta = b-a 
    return delta

delta = delta_calc(date_start,date_stop,date_format)
print("{0} days have passed".format(delta.days))
```

>> 937 days have passed

b.  
```
date_start = '12312013'  
date_stop = '05282015'
date_format = "%m%d%Y"

delta = delta_calc(date_start,date_stop,date_format)
print("{0} days have passed".format(delta.days))
```

>> 513 days have passed

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'
date_format = '%d-%b-%Y' 

delta = datetime.strptime(date_stop, date_format) - datetime.strptime(date_start, date_format)
print("{0} days have passed".format(delta.days))
```

>> 7,850 days have passed

Place code in this file: [q5_datetime.py](python/q5_datetime.py)
>>Done. I also coded this in Jupyter. Here is the [Gist](https://gist.github.com/a2f79db22757a127a96d4dfbb2c8f905).

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)
>>Ok

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)
>>Ok
---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





