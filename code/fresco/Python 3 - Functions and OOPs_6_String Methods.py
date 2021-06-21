zenPython = '''
The Zen of Python, by Tim Peters 

Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
Flat is better than nested.
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea.
''' 

words = zenPython.split()
words = [word.strip(',').strip('.').strip('-').strip('*').strip('!').strip(' ') for word in words]
words = [word.lower() for word in words]
unique_words = list(set(words))
  
word_frequency = {word: words.count(word) for word in unique_words}
#newDict = {key: value for (key, value) in dictOfNames.items() if len(value) == 6 }
frequent_words = {key: value for (key, value) in word_frequency.items() if value > 5 }
#print(frequent_words)
print(len(frequent_words))
#print(word_frequency['the'])