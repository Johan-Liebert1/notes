"""  
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""

from typing import List
import queue as Q


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = {x for x in wordList}
        charSet = {w for word in wordList for w in word}

        if endWord not in wordList:
            return 0

        # which iteration are we at
        depth = 0

        # how many nodes are there at a certain level of the graph (since BFS traversal)
        lsize = 0

        queue = Q.Queue()
        queue.put(beginWord)

        """
        1. get a word from the queue and do a brute force transformation check, i.e. check in the set if we            
        can get a word from removing a letter from the current word
        keep repeating until we get to the end word 
        """
        while not queue.empty():
            lsize = queue.qsize()
            depth += 1

            for _ in range(lsize):
                current_word = queue.get()

                for i in range(len(current_word)):

                    for c in charSet:
                        # replace every character in current word with every character in the alphabet and check
                        # if that exists in the word list or not
                        next_word = current_word[:i] + c + current_word[i + 1 :]

                        if next_word == endWord:
                            return depth + 1

                        if next_word in wordList:
                            wordList.remove(next_word)
                            queue.put(next_word)

        return 0
