## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>>Without Cleaning the Data, here is the raw output from value_counts

```
 Ph.D.                 15
 PhD                    7
 Ph.D                   4
 Sc.D.                  4
 MD MPH Ph.D            1
Ph.D.                   1
 B.S.Ed. M.S. Ph.D.     1
 PhD ScD                1
0                       1
 ScD                    1
 JD MA MPH MS PhD       1
```

```
import pandas as pd
import numpy as np
df = pd.read_csv('faculty.csv')
df.rename(columns=lambda x: x.strip())
counts = df["degree"].value_counts()
```


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> From value_counts, there are only 2, the rest are mispelled versions.

```
Professor of Biostatistics              13
Associate Professor of Biostatistics    12
Assistant Professor of Biostatistics    11
Assistant Professor is Biostatistics     1
```

```
import pandas as pd
import numpy as np
df = pd.read_csv('faculty.csv')
df.rename(columns=lambda x: x.strip())
counts = df["title"].value_counts()
print(counts)
```

####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>>Ok

```
['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', .....]
```


```
import pandas as pd
import numpy as np
df = pd.read_csv('faculty.csv')
df.rename(columns=lambda x: x.strip())
print(df["email"].tolist())
```


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> Below is the output from pandas' value_counts––I'm a one trick pony. 

```
mail.med.upenn.edu    23
upenn.edu             12
email.chop.edu         1
cceb.med.upenn.edu     1
```

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)
>>Ok

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

>>Ok

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

>> Ok––I'm just going with pandas for this exercise. Probably overkill.

```
{'A. Russell Localio': [' JD MA MPH MS PhD',
  'Associate Professor of Biostatistics',
  'rlocalio@upenn.edu'],
 'Alisa Jane Stephens': [' Ph.D.',
  'Assistant Professor of Biostatistics',
  'alisaste@mail.med.upenn.edu'],
 'Andrea Beth Troxel': [' ScD',
  'Professor of Biostatistics',
  'atroxel@mail.med.upenn.edu'],
```

```
import pandas as pd
import numpy as np
df = pd.read_csv('faculty.csv')
df.columns = df.columns.str.strip()
df.rename(columns=lambda x: x.strip())
df.set_index('name').T.to_dict('list')
```

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```


>> Ok. Question--Why would you want a key as an array? 

```
{('Warren', 'B.'): ['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu'], ('Susan', 'S'): [' Ph.D.', 'Professor of Biostatistics', 'sellenbe@upenn.edu'], ('Rebecca', 'A'): [' PhD', 'Associate Professor of Biostatistics', 'rhubb@mail.med.upenn.edu'],
```

```
import pandas as pd
import numpy as np
df = pd.read_csv('faculty.csv')
df.columns = df.columns.str.strip()
df.rename(columns=lambda x: x.strip())
df["fn"], df["ln"] = zip(*df["name"].str.split().tolist())
del df["name"]
df = df[['fn', 'ln', 'degree', 'title', 'email']]

dict = df.set_index(['fn','ln']).T.to_dict('list')
print(dict)
```


####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>> Are we still using a key array? If so, here you go

```
{('Li', 'Yimei'): [' Ph.D.', 'Assistant Professor of Biostatistics', 'liy3@email.chop.edu'], ('A.', 'Jason'): [' Ph.D.', 'Associate Professor of Biostatistics', 'jaroy@mail.med.upenn.edu'], ('Elana', 'Michelle'): [' PhD', 'Assistant Professor is Biostatistics', 'michross@upenn.edu'],
```

```
import pandas as pd
import numpy as np
df = pd.read_csv('faculty.csv')
df.columns = df.columns.str.strip()
df.rename(columns=lambda x: x.strip())
df["fn"], df["ln"] = zip(*df["name"].str.split().tolist())
del df["name"]
df = df[['fn', 'ln', 'degree', 'title', 'email']]

dict = df.set_index(['ln','fn']).T.to_dict('list')
print(dict)
```

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

>> Ok

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

