# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

* ls lists invisible files
* ls -a -> include invisible files
* ls -l -> file lists in permissions, ownership, group––verbose mode
* ls -lh -> same as ls -l and include file sizes
* ls -lah -> same as above and includes invisible files
* ls -t  -> sorts by time modified
* ls -Glp -> long format with color mode enabled, writes a slash after directory items

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

* -R display of subdirectories is a plus
* -P lists actual link over reference
* -u gives time of last access
* -S sorts by filesize
* -k prints in kilobytes

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

Xargs displays whatever comes to its stdin. The below returns lines of 4 characters
`echo a b c d e f g h | xargs -n 4`
returns 
``` a b c d
e f g h
```
 

