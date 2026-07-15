from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in wordList:
            return 0
        q = deque([(beginWord,1)])
        while q:
            word,step = q.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + j + word[i+1:]

                    if new_word in words:
                        q.append((new_word,step + 1))
                        words.remove(new_word)
        return 0                      
