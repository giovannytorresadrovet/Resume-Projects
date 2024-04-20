questions = [
{
    "prompt": "What does CIA stand for in the context of information security?",
    "options": ["A. Confidentiality, Integrity, Availability", "B. Central Intelligence Agency", "C. Computer Incident Assessment", "D. Certified Information Assurance"],
    "answer": "A"
},

{
    "prompt": "A VPN of five nodes uses symmetric encryption to transmit data securely, all sharing the same secret key. How many new keys would be needed to re-establish secure communications to all nodes if there is a key compromise? 	",
    "options": ["A. 15", "B. 5", "C. 10", "D. 1"],
    "answer": "A"
},
{
    "prompt": "Which of the following is NOT a common encryption algorithm?",
    "options": ["A. AES", "B. DES", "C. RSA", "D. MD5"],
    "answer": "D"
},

{
    "prompt": "What does SSL/TLS provide?",
    "options": ["A. Encryption and authentication", "B. Compression and data integrity", "C. Only encryption", "D. Only authentication"],
    "answer": "A"
},

{
    "prompt": "Which of the following is a type of network attack where an attacker intercepts communication between two parties and injects malicious content?",
    "options": ["A. DoS attack", "B. Man-in-the-Middle (MitM) attack", "C. Cross-Site Scripting (XSS) attack", "D. Phishing attack"],
    "answer": "B"
}
]

def run_quiz(questions):
    score = 0
    for question in questions:
            print(question["prompt"])
            for option in question["options"]:
                print(option)
            answer = input("Enter your answer:").upper()
            if answer == question["answer"]:
                 print("Correct!!\n")
                 score += 1
                 
            else:
                print("Wrong!! The correct answer was:",question["answer"], "\n")
        
    print(f"Your score is: {score} out of {len(questions)} questions.")

run_quiz(questions)
