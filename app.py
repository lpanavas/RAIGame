import tkinter as tk
import openai
import json
import time

class AI_Ethics_Game:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # Data storage
        self.data = []

        # Scenario and prompts
        self.scenario = "Hello, and welcome to Ethicorp. As a product manager, you're tasked with deciding whether our new AI-powered virtual assistant should be designed to access and learn from a user's personal data - like location history, browsing habits, and communication patterns - to provide a more personalized and efficient service. This will greatly improve the user experience, but it does involve using more of their personal data. What do you choose?"

        # Input box
        self.input_var = tk.StringVar()
        self.input_box = tk.Entry(self.frame, textvariable=self.input_var)
        self.input_box.pack()

        # Output box
        self.output_var = tk.StringVar()
        self.output_box = tk.Label(self.frame, textvariable=self.output_var, wraplength=480)
        self.output_box.pack()

        # Submit button
        self.submit_button = tk.Button(self.frame, text="Submit", command=self.submit)
        self.submit_button.pack()

        # Set up OpenAI API
        openai.api_key = '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'

        # Start game
        self.start_time = time.time()
        self.output_var.set(self.scenario)

    def submit(self):
        # Get user input
        user_input = self.input_var.get()

        # Record response time
        response_time = time.time() - self.start_time

        # Generate chatbot response
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=self.scenario + "\n" + user_input,
            max_tokens=150,
            n=2
        )
        chatbot_responses = [choice.text.strip() for choice in response.choices]

        # Store data
        self.data.append({
            "input": user_input,
            "responses": chatbot_responses,
            "response_time": response_time
        })

        # Show chatbot responses
        self.output_var.set("Option 1: " + chatbot_responses[0] + "\nOption 2: " + chatbot_responses[1])

        # Clear input box
        self.input_var.set("")

        # Update start time
        self.start_time = time.time()

        # Check if user wants to stop
        if user_input.lower() == "stop":
            self.export_data()
            self.master.quit()

    def export_data(self):
        # Export data to JSON
        with open("data.json", "w") as f:
            json.dump(self.data, f)

def main():
    root = tk.Tk()
    root.geometry("500x300")
    game = AI_Ethics_Game(root)
    root.mainloop()

if __name__ == "__main__":
    main()
