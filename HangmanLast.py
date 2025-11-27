import random
RandomWords=["shark","lion","horse","catt","dog","elephant","monkey","donkey","whale","pigeon"]
hangMan=[r"""
  +---+
      |
      |
      |
     ===""",
r"""
  +---+
  O   |
      |
      |
     ===""",
r"""
  +---+
  O   |
  |   |
      |
     ===""",
r"""
  +---+
  O   |
 /|   |
      |
     ===""",
r"""
  +---+
  O   |
 /|\  |
      |
     ===""",
r"""
  +---+
  O   |
 /|\  |
 /    |
     ===""",
r"""
  +---+
  O   |
 /|\  |
 / \  |
     ==="""]
word=random.choice(RandomWords)
print(word)
guess=input("Guess the letter: ").lower()
heart=6
isWord = "_" * len(word)
def guessWord():
    global isWord, heart
    lst = list(isWord)
    for j in range(len(word)):
        if guess == word[j]:
            lst[j] = guess

    if guess in isWord:
        print("do not repeat")
    else:
        heart -= 1

    isWord = "".join(lst)


    print(heart)
    print(isWord)

while heart > 1 and "_" in isWord:

    guessWord()
    guess = input("Guess the letter: ").lower()
    print(hangMan[-heart])








