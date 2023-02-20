with open("./Input/Names/invited_names.txt") as names:
    people = names.readlines()
for people_names in people:
    invite = people_names.strip()
    with open("./Input/Letters/starting_letter.txt") as letter:
        text = letter.read()
        content = text.replace("[name]", invite)
        with open(f"./Output/ReadyToSend/ready_to_send_to_{invite}.txt", mode='w') as real_letter:
            real_letter.write(content)
