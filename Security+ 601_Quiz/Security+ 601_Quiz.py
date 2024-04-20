import random

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question("1. A VPN of five nodes uses symmetric encryption to transmit data securely, all sharing the same secret key. How many new keys would be needed to re-establish secure communications to all nodes if there is a key compromise?\n"
             "   a. 15\n"
             "   b. 5\n"
             "   c. 10\n"
             "   d. 1\n"
             "Your answer: ", "c"),

    Question("2. RC4 is which of the following algorithm?\n"
             "   a. asymmetric and a stream cipher\n"
             "   b. asymmetric\n"
             "   c. stream cipher\n"
             "   d. neither asymmetric or a stream cipher\n"
             "Your answer: ", "c"),

    Question("3. An attacker has been analyzing encrypted data that he intercepted. He knows that the end of the data includes a template sent with all similar messages. He uses this knowledge to decrypt the message. Which of the following types of attacks BEST describes this attack? \n"
             "   a. Known ciphertext\n"
             "   b. Known plaintext\n"
             "   c. Brute force\n"
             "   d. Rainbow table\n"
             "Your answer: ", "_____"),

    Question("75. A network operations manager has added a second row of server racks in the datacenter. These racks face the opposite direction of the first row of racks. Which of the following is the reason the manager installed the racks this way? \n"
             "   a. To lower energy consumption by sharing power outlets\n"
             "   b. To create environmental hot and cold isles\n"
             "   c. To eliminate the potential for electromagnetic interference\n"
             "   d. To maximize fire suppression capabilities\n"
             "Your answer: ", "b")
]

def run_quiz(questions):
    random.shuffle(questions)  # Shuffle the questions
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")
    print("You got", score, "out of", len(questions), "questions correct.")

run_quiz(questions)
