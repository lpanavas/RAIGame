
import tkinter as tk
from threading import Timer
import openai

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.responses = []
        self.scores = []
        openai.api_key = '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'
        self.create_widgets()

    def create_widgets(self):
        self.info = tk.Label(self, text="You have 60 seconds. Enter as many uses for facial recognition technology as you can think of!")
        self.info.grid(row=0)

        self.entry = tk.Entry(self)
        self.entry.grid(row=1)

        self.submit_button = tk.Button(self, text="Submit", command=self.collect_and_score_response)
        self.submit_button.grid(row=2)

        self.quit_button = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit_button.grid(row=3)

        self.time_remaining = 60
        self.timer_label = tk.Label(self, text="Time remaining: 60")
        self.timer_label.grid(row=4)

        self.score = 0
        self.score_label = tk.Label(self, text="Current score: 0")
        self.score_label.grid(row=5)

        self.update_timer()

    def update_timer(self):
        self.time_remaining -= 1
        self.timer_label['text'] = f"Time remaining: {self.time_remaining}"
        if self.time_remaining > 0:
            self.after(1000, self.update_timer)
        else:
            self.summarize_scores()

    def collect_and_score_response(self):
        response = self.entry.get()
        if response not in self.responses:
            self.responses.append(response)
            score = self.score_response(response)
            self.score += score
            self.score_label['text'] = f"Current score: {self.score}"
        self.entry.delete(0, 'end')

    def score_response(self, response):
    # Call the OpenAI API to check if the response is a plausible use of facial recognition technology
        result = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"'{response}' is a plausible use of facial recognition technology. True or false?",
            max_tokens=3
        )
        answer = result.choices[0].text.strip().lower()
        print(answer)
        return 1 if answer == 'true' else 0


    def summarize_scores(self):
        total_score = sum(self.scores)

        self.info['text'] = f"Time's up! Your total score is {total_score}."

root = tk.Tk()
root.geometry("500x300")


app = Application(master=root)
app.mainloop()
