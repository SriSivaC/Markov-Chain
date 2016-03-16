import random
class markovChain():
    def __init__(self, elements, end):
        if '' in elements:
            elements.remove('')
        self.elements=elements
        self.end=end
        startingElements=[]
        orderedElements={}
        elementsIndex=0
        for element in elements:
            if (not element in orderedElements) and element!=end:
                orderedElements[element]=[]
            if element in orderedElements and (elementsIndex==0 or elements[elementsIndex-1]==self.end):
                startingElements.append(element)
            elif elements[elementsIndex-1] in orderedElements:
                orderedElements[elements[elementsIndex-1]].append(element)
            elementsIndex+=1
        self.startingElements=startingElements
        self.orderedElements=orderedElements
    def generate(self, sep='', end=''):
        r=random.choice(self.startingElements)
        element=random.choice(self.orderedElements[r])
        while element!=self.end:
            r+=sep+element
            element=random.choice(self.orderedElements[element])
        return r+end
    
#RANDOM WORDS#
##file=open('wordlist.txt', 'r')
##words=[]
##for word in file.readlines():
##    words.extend(list(word))
##print(len(words))
##file.close()
##markov=markovChain(words, '\n')
##while 1:
##    input(markov.generate())

#RANDOM SENTENCES#
sentences='A Markov chain , named after Andrey Markov, is a random process that undergoes transitions from one state to another on a state space. It must possess a \
property that is usually characterized as "memoryless": the probability distribution of the next state depends only on the current state and not on the sequence of \
events that preceded it. This specific kind of "memorylessness" is called the Markov property. Markov chains have many applications as statistical models of \
real-world processes.'
sentences=sentences.replace('.',' . ').replace('  ',' ').split(' ')
markov=markovChain(sentences, '.')
while 1:
    input(markov.generate(' ','.'))

#RANDOM LYRICS#
##file=open('lyrics.txt', 'r')
##lyrics=[]
##for line in file.readlines():
##    if line!='\n':
##        line=line.replace('\n', ' \n')
##        lyrics.extend(line.split(' '))
##file.close()
##markov=markovChain(lyrics, '\n')
##while 1:
##    input(markov.generate(' '))
