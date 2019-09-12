# Becoming a 10x Software Developer : The Journey continues — Day 8

September 12, 2019

Hello Everyone,

I request you to go through my previous blog to be up-to-date with my progress. However I will try my level best to keep things as simple and easy to understand without any prior research.

## Collection data types

In Python programming language there are 4 collection data type namely,
1. List
2. Dictionary
3. Tuple
4. Set

Today, we have covered lists, dictionary and tuples.

### List

List is a collection which is ordered and changeable. It allows duplicate members.
Ex.
```
l = ["Hello" , 23 , 4.54 , "World"]
l = ["qwerty" , 34 , ["pot" , 'luck' , "crazy"] , "true"]
l[0] = 'qwertry'
l[2][1] = 'pot'
```
```
* l[::-1]  : reverses the list
* z = l.extend(p) : If l and p are two lists, z would store the list p appended to l.
* del l[index] : Deletes the mentioned index's value
* l.remove(value) : Removes 'value' if it is present in the list
* value in list : returns true if value present in the list and returns false if not present
* Similarly 'value not in list' returns true if value not present in list
* list.append(value) : appends value to the list
* list.index(value) : returns the index of value in the list
* list.sort() : Sorts the list in ascending order
* list.sort(reversed = 'True') : Sorts the list in descending order
```

### Dictionary

Dictionary is a collection which is unordered, changeable and indexed. No duplicate members is present. Elements in dictionary are always stored as key-value pairs.
```
* dict[key] = value
* dict.key() = [key1, key2, key3, ....]
* dict.values() = [value1, value2, value3, ....]
```
Ex.
```
dict = { "python":2019 , "cpp":2011 , "c":2015 }
dict = { "python":2019 , {"high":"level" , "low":"level"} , "cpp":2011 }
```

### Tuple

Tuple is a collection which is ordered and unchangeable. It allows duplicate members.
```
* p = ('a') : defines p as a string because of only value being inputted
* p = ('a',) : defines p as a tuple even without more than one entry
* t.item() : returns the list of items in the tuple t
```
Ex.
```
t = ('a' , 'b')
t = ('a' , 'b' , ("Hello" , "there") )
```

The remaining collection data type set() would be covered during the next session. That sums up the content for the day's discussion.

Signing off
