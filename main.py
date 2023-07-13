# main.py

import random
import time 

sen = ["Fusajiro Yamauchi invented Nintendo in 1889.", "Amazon began in the garage of Jeff Bezoz in 1994.", "America won the Space Race in 1969 with Neil Armstrong.", "Koala fingerprints are extremely similar to human fingerprints!"]
sentence = sen[random.randint(0,3)]

words = 0
for i in range(len(sentence)):
  if sentence[i] == " " or sentence[i] == "." or sentence[i] == "!":
    words += 1 


print("Type Racer") 
enter = input("Player 1, Press any key to begin: ") 
print("Ready...")
time.sleep(1)
print("Set...")
time.sleep(1)
print("Type!")

print("[ " + sentence + " ]")
typer = ""
while typer != sentence:
    start = time.time()
    typer = input("")
    if typer != sentence:
      print("Error: Bad message!")

end = time.time()
interval = end - start
wpm = (words/interval) * 60
print("Player 1: " + str(interval))
print("WPM: " + str(wpm))

enter2 = input("Player 2, Press any key to begin: ") 
print("Ready...")
time.sleep(1)
print("Set...")
time.sleep(1)
print("Type!")

print("[ " + sentence + " ]")
typer = ""
while typer != sentence:
    start = time.time()
    typer = input("")
    if typer != sentence:
      print("Error: Bad message!")
    
end = time.time()
interval2 = end - start
wpm2 = (words/interval2) * 60
print("Player 2: " + str(interval2))
print("WPM: " + str(wpm2))

if wpm > wpm2:
  print("P1 Won!")
elif wpm < wpm2:
  print("P2 Won!")
else:
  print("Tie!")

  
