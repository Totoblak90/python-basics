#TODO: Create a letter using starting_letter.txt 
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    s_l_content = starting_letter.read()

with open("./Input/Names/invited_names.txt") as names_file:
    names_list = [name.strip() for name in names_file]

letter_list = []

for name in names_list:
    new_letter = s_l_content.replace('[name]', name)
    letter_list.append(new_letter)

for index, letter in enumerate(letter_list):
    with open(f"./Output/ReadyToSend/{names_list[index]}.txt", mode="w") as l:
        l.write(letter)

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp