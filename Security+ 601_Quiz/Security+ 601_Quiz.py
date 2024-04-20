import random

class Question:
    def __init__(self, prompt, answers, correct_answer):
        self.prompt = prompt
        self.answers = answers
        self.correct_answer = correct_answer

    def shuffle_answers(self):
        random.shuffle(self.answers)

questions = [
    Question("1. A VPN of five nodes uses symmetric encryption to transmit data securely, all sharing the same secret key. How many new keys would be needed to re-establish secure communications to all nodes if there is a key compromise?\n"
             "   a. 15\n"
             "   b. 5\n"
             "   c. 10\n"
             "   d. 1\n"
             "Your answer: ", ["a", "b", "c", "d"], "d"),

    Question("2. RC4 is which of the following algorithm?\n"
             "   a. asymmetric and a stream cipher\n"
             "   b. asymmetric\n"
             "   c. stream cipher\n"
             "   d. neither asymmetric or a stream cipher\n"
             "Your answer: ", ["a", "b", "c", "d"], "c"),

    Question("3. An attacker has been analyzing encrypted data that he intercepted. He knows that the end of the data includes a template sent with all similar messages. He uses this knowledge to decrypt the message. Which of the following types of attacks BEST describes this attack? \n"
             "   a. Known ciphertext\n"
             "   b. Known plaintext\n"
             "   c. Brute force\n"
             "   d. Rainbow table\n"
             "Your answer: ", ["a", "b", "c", "d"], "b"),

    Question("4. Despite having implemented password policies, users continue to set the same passwords and reuse old passwords. Which of the following controls would help prevent policy violations? \n"
             "   a. Password expiration\n"
             "   b. Password length\n"
             "   c. Password complexity\n"
             "   d. Password history\n"
             "   e. Password lockout\n"
             "Your answer: ", ["a", "b", "c", "d"], "b and d"),

    Question("5. How many keys would be required for 10 users to fully communicate using an asymmetric system? \n"
             "   a. 10\n"
             "   b. 20\n"
             "   c. 50\n"
             "   d. 45\n"
             "Your answer: ", ["a", "b", "c", "d"], "b"),

    Question("6. A digital certificate ____________. \n"
             "   a. Includes a time period for which it is valid\n"
             "   b. Contains the private key\n"
             "   c. Construction is governed by the X.905 standard\n"
             "   d. Is none of the above\n"
             "Your answer: ", ["a", "b", "c", "d"], "a"),
    
    Question("7. Which part of Public Key Infrastructure (PKI) verifies the applicant? \n"
             "   a. Certificate authority\n"
             "   b. Verification authority\n"
             "   c. Validation authority\n"
             "   d. Registration authority\n"
             "Your answer: ", ["a", "b", "c", "d"], "d"),

    Question("8. Which TCP/IP ports does SNMP usually use? \n"
             "   a. Ports 25 and 110\n"
             "   b. Ports 138 and 139\n"
             "   c. Ports 161 and 162\n"
             "   d. Ports 80 and 443\n"
             "Your answer: ", ["a", "b", "c", "d"], "c"),

    Question("9. Which version of SNMP makes sniffing management traffic difficult due to encryption? \n"
             "   a. SNMPv3\n"
             "   b. SNMPv2\n"
             "   c. SNMPv1\n"
             "   d. All of the above\n"
             "Your answer: ", ["a", "b", "c", "d"], "a"),

    Question("10. A network operations manager has added a second row of server racks in the datacenter. These racks face the opposite direction of the first row of racks. Which of the following is the reason the manager installed the racks this way? \n"
             "   a. To lower energy consumption by sharing power outlets\n"
             "   b. To create environmental hot and cold isles\n"
             "   c. To eliminate the potential for electromagnetic interference\n"
             "   d. To maximize fire suppression capabilities\n"
             "Your answer: "", ["a", "b", "c", "d"], "b"),
]

def run_quiz(questions):
    random.shuffle(questions)  # Shuffle the questions
    score = 0
    for question in questions:
        question.shuffle_answers()  # Shuffle the answers for each question
        print(question.prompt)
        for answer in question.answers:
            print(answer)
        user_answer = input("Your answer: ").strip().lower()  # Convert user's input to lowercase
        if user_answer == question.correct_answer.lower():  # Compare lowercase answers
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")
    print("You got", score, "out of", len(questions), "questions correct.")

run_quiz(questions)

