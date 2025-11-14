
word=input("player1-choose your word--")
print(""" Art by Joan G. Stark
          ___   .--.
    .--.-"   "-' .- |
   / .-,`          .'
   \   `           \
    '.            ! \
      |     !  .--.  |
      \        '--'  /.____
     /`-.     \__,'.'      `\
  __/   \`-.____.-' `\      /
  | `---`'-'._/-`     \----'    _ 
  |,-'`  /             |    _.-' `\
 .'     /              |--'`     / |
/      /\              `         | |
|   .\/  \      .--. __          \ |
 '-'      '._       /  `\         /
    jgs      `\    '     |------'`
               \  |      |
                \        /
                 '._  _.'
                    ``""")
print(len(word))
list_of_word= list(word)
merge_list_of_word=""
heart=0
metter=0
HANGMAN_PICS = [
r"""
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
     ==="""
]


for letter in list_of_word:
    letter="_"
    merge_list_of_word+=letter

print("unknown word"+ merge_list_of_word)
merge_finding_name=""

finding_name=list(merge_list_of_word)
while heart<7 and "_" in finding_name:
    player_2 = input("player2-choose your letter--")
    if player_2 in word:
        print(player_2)
        for index in range(len(word)):
            if player_2 == word[index]:
                finding_name[index]=word[index]
                merge_finding_name="".join(finding_name)

                print(merge_finding_name)
                if "_" not in finding_name:
                    print("halaldi qaqa")


    else:
        print(HANGMAN_PICS[heart])
        heart += 1


        if heart == 7:
            print("You lose")




