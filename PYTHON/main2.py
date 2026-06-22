from collections import deque

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    wordSet = set(wordList)
    queue = deque([(beginWord, 1)])

    while queue:
        word, steps = queue.popleft()

        if word == endWord:
            return steps

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                nextWord = word[:i] + c + word[i+1:]

                if nextWord in wordSet:
                    wordSet.remove(nextWord)
                    queue.append((nextWord, steps + 1))

    return 0
