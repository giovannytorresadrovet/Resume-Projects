import random

class Question:
    def __init__(self, prompt, correct_answers):
        self.prompt = prompt
        self.correct_answers = correct_answers
        self.answers = []

    def add_answer(self, answer):
        self.answers.append(answer)

    def shuffle_answers(self):
        random.shuffle(self.answers)

# Define the questions
questions = [
    Question("1. A VPN of five nodes uses symmetric encryption to transmit data securely, all sharing the same secret key. How many new keys would be needed to re-establish secure communications to all nodes if there is a key compromise?\n", ["d"]),
    Question("2. RC4 is which of the following algorithm?\n", ["c"]),
    Question("3. An attacker has been analyzing encrypted data that he intercepted. He knows that the end of the data includes a template sent with all similar messages. He uses this knowledge to decrypt the message. Which of the following types of attacks BEST describes this attack? \n", ["b"]),
    Question("4. Despite having implemented password policies, users continue to set the same passwords and reuse old passwords. Which of the following controls would help prevent policy violations? \n", ["a", "d"]),
    Question("5. How many keys would be required for 10 users to fully communicate using an asymmetric system? \n", ["b"]),
    Question("6. A digital certificate ____________. \n", ["a"]),
    Question("7. Which part of Public Key Infrastructure (PKI) verifies the applicant? \n", ["d"]),
    Question("8. Which TCP/IP ports does SNMP usually use? \n", ["c"]),
    Question("9. Which version of SNMP makes sniffing management traffic difficult due to encryption? \n", ["b"]),
    Question("10. NetBIOS is used in older Windows systems for file and print sharing over a LAN. Which port does NetBIOS use? \n", ["d"]),
    Question("11. The CEO recently decided that only a limited number of authorized company workstations will be able to connect to the internet via Wi-Fi enabled network. Which of the following would BEST accomplish this goal? \n", ["b"]),
    Question("12. Which of the following does PTR map? \n", ["d"]),
    Question("13. A network operations manager has added a second row of server racks in the datacenter. These racks face the opposite direction of the first row of racks. Which of the following is the reason the manager installed the racks this way and why? \n", ["b"])
]

# Add answers for each question
questions[0].add_answer("a. 15")
questions[0].add_answer("b. 5")
questions[0].add_answer("c. 10")
questions[0].add_answer("d. 1")

questions[1].add_answer("a. asymmetric and a stream cipher")
questions[1].add_answer("b. asymmetric")
questions[1].add_answer("c. stream cipher")
questions[1].add_answer("d. neither asymmetric or a stream cipher")

questions[2].add_answer("a. Known ciphertext")
questions[2].add_answer("b. Known plaintext")
questions[2].add_answer("c. Brute force")
questions[2].add_answer("d. Rainbow table")

questions[3].add_answer("a. Password expiration")
questions[3].add_answer("b. Password length")
questions[3].add_answer("c. Password complexity")
questions[3].add_answer("d. Password history")
questions[3].add_answer("e. Password lockout")

questions[4].add_answer("a. 10")
questions[4].add_answer("b. 20")
questions[4].add_answer("c. 50")
questions[4].add_answer("d. 45")

questions[5].add_answer("a. Includes a time period for which it is valid")
questions[5].add_answer("b. Contains the private key")
questions[5].add_answer("c. Construction is governed by the X.905 standard")
questions[5].add_answer("d. Is none of the above")

questions[6].add_answer("a. Certificate authority")
questions[6].add_answer("b. Verification authority")
questions[6].add_answer("c. Validation authority")
questions[6].add_answer("d. Registration authority")

questions[7].add_answer("a. Ports 25 and 110")
questions[7].add_answer("b. Ports 138 and 139")
questions[7].add_answer("c. Ports 161 and 162")
questions[7].add_answer("d. Ports 80 and 443")

questions[8].add_answer("a. SNMPv3")
questions[8].add_answer("b. SNMPv2")
questions[8].add_answer("c. SNMPv1")
questions[8].add_answer("d. All of the above")

questions[9].add_answer("a. Use content filtering")
questions[9].add_answer("b. Enable MAC address filtering")
questions[9].add_answer("c. Enable RAS on the network firewall")
questions[9].add_answer("d. Install and configue IDS")

questions[10].add_answer("a. 137")
questions[10].add_answer("b. 138")
questions[10].add_answer("c. 139")
questions[10].add_answer("d. All of the above")

questions[11].add_answer("a. MAC address to IP address")
questions[11].add_answer("b. Host name to IP address")
questions[11].add_answer("c. IP address to MAC address")
questions[11].add_answer("d. IP address to host name")

questions[12].add_answer("a. To lower energy consumption by sharing power outlets")
questions[12].add_answer("b. To create environmental hot and cold isles")
questions[12].add_answer("c. To eliminate the potential for electromagnetic interference")
questions[12].add_answer("d. To maximize fire suppression capabilities")



# Shuffle the questions
random.shuffle(questions)

# Run the quiz
score = 0
for question in questions:
    question.shuffle_answers()
    print(question.prompt)
    for answer in question.answers:
        print(answer)
    user_answer = input("Your answer: ")
    if user_answer.lower() in question.correct_answers:  # Compare lowercase answers
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect!\n")

print("You got", score, "out of", len(questions), "questions correct.")
