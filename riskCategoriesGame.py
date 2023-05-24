import random

class AIRiskClassificationGame:
    def __init__(self):
        self.score = 0
        self.rounds = 0
        self.ai_systems = [
           {"description": "A facial recognition AI system used for real-time biometric identification in publicly accessible spaces.", "answer": "unacceptable"},
            {"description": "A facial recognition AI system used for post-event biometric identification in publicly accessible spaces.", "answer": "high"},
            {"description": "A facial recognition AI system used for biometric identification in private spaces.", "answer": "high"},
            {"description": "A facial recognition AI system used by law enforcement to assess the risk of a person reoffending.", "answer": "high"},
            {"description": "A facial recognition AI system used by law enforcement to evaluate the reliability of evidence in criminal investigations.", "answer": "high"},
            {"description": "A facial recognition AI system used for identity verification in immigration, asylum, and border control management.", "answer": "high"},
            {"description": "A facial recognition AI system used for evaluating the eligibility of individuals for public assistance benefits and services.", "answer": "high"},
            {"description": "A facial recognition AI system used in the recruitment or selection process of a job.", "answer": "high"},
            {"description": "A facial recognition AI system used for the purpose of determining access to educational and vocational training institutions.", "answer": "high"},
            {"description": "A facial recognition AI system used for the management and operation of critical infrastructure, such as traffic management.", "answer": "high"},
              {"description": "A facial recognition AI system used to unlock a personal smartphone.", "answer": "low"},
            {"description": "A facial recognition AI system used to tag friends in personal photos on social media.", "answer": "low"},
            {"description": "A facial recognition AI system used to personalize user experience in a digital platform.", "answer": "low"},
            {"description": "A facial recognition AI system used for age verification on a website selling age-restricted goods.", "answer": "low"},
            {"description": "A facial recognition AI system used for patient identification in a private hospital setting.", "answer": "low"},
            {"description": "A facial recognition AI system used in a home security system.", "answer": "low"},
            {"description": "A facial recognition AI system used for employee check-in at a privately owned company.", "answer": "low"},
            {"description": "A facial recognition AI system used for personalizing advertisements on a digital platform.", "answer": "low"},
            {"description": "A facial recognition AI system used for identifying individuals in personal event videos.", "answer": "low"},
            {"description": "A facial recognition AI system used for finding look-alike faces in a celebrity database.", "answer": "low"},
            {"description": "A facial recognition AI system used for mass surveillance in public spaces.", "answer": "unacceptable"},
    {"description": "A facial recognition AI system used for real-time identification of individuals in a crowd without their consent.", "answer": "unacceptable"},
    {"description": "A facial recognition AI system used for determining individuals' political affiliations or religious beliefs.", "answer": "unacceptable"},
    {"description": "A facial recognition AI system used for making automated decisions about individuals' eligibility for social benefits.", "answer": "unacceptable"},
    {"description": "A facial recognition AI system used for predicting individuals' future behavior or likelihood of committing a crime.", "answer": "unacceptable"},
    {"description": "A facial recognition AI system used for determining individuals' credit scores or financial trustworthiness.", "answer": "unacceptable"},
    {"description": "A facial recognition AI system used for making automated hiring decisions without human oversight.", "answer": "unacceptable"},
    {"description": "A facial recognition AI system used for profiling individuals based on their appearance or ethnicity.", "answer": "unacceptable"},
    {"description": "A facial recognition AI system used for making automated decisions about individuals' health or medical treatment.", "answer": "unacceptable"},
    {"description": "A facial recognition AI system used for creating deepfakes or manipulating individuals' images without their consent.", "answer": "unacceptable"},

        ]
        self.risk_levels = ["unacceptable", "high", "low"]

    def play_round(self):
        ai_system = random.choice(self.ai_systems)
        print(f"\nDescription of AI system: {ai_system['description']}")
        print("What is the risk classification of this AI system according to the EU's AI regulations?")
        print("Options: unacceptable, high, low")
        player_answer = input("Your answer: ").lower()

        if player_answer == ai_system['answer']:
            self.score += 1
            print(f"Correct! Your score is now {self.score}.")
        else:
            print(f"Sorry, that's incorrect. The correct answer is {ai_system['answer']}.")

        self.rounds += 1

    def play_game(self, num_rounds=5):
        print("Welcome to the AI Risk Classification Challenge!")
        for _ in range(num_rounds):
            self.play_round()

        print(f"\nGame over! Your final score is {self.score} out of {self.rounds}.")
        print("include Contesting an answer")

game = AIRiskClassificationGame()
game.play_game()
