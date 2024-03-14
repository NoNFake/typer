from time import sleep
from os import system

system("cls")

alp: str = "qwertyuiopasdfghjklzxxcvbnm:()/₴_-+.\\!@#$%^&*<>? "
hesh: str = "="

def spell(word, speed):
  str = ""

  var: float = 0
  progress: float = 0

  for i in word:
    for j in alp:
      system("cls")
      length_words = len(word)
      
      print(f"[TYPER]: {str + j}" )

      num_hashes = int(progress / (100 / length_words))
      remaining_spaces = length_words - num_hashes
      
      progress_bar = hesh * num_hashes + "-" * remaining_spaces
      print(f"[PROGRESS]: [{progress_bar}] | [{progress:.2f}%]")
    
      
      if j == i or j == "":
        var += 1
        
        # progress
        str += j
        progress = ((100 * var) / length_words) 
      
      sleep(speed)
  system("pause")
        
word = input("Enter the word: ")
speed = float(input("Enter the speed: "))
spell(word, speed)