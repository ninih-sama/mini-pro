import tkinter as tk
from tkinter import messagebox

# Quiz Questions
questions = [
    {
        "question": "Quelle est la capitale de la France ?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Quelle planète est surnommée la planète rouge ?",
        "options": ["A. Terre", "B. Mars", "C. Jupiter", "D. Vénus"],
        "answer": "B"
    },
    {
        "question": "Qui a écrit 'Le Petit Prince' ?",
        "options": ["A. Victor Hugo", "B. Antoine de Saint-Exupéry", "C. Marcel Proust", "D. Albert Camus"],
        "answer": "B"
    },
    {
        "question": "Quelle est la formule chimique de l'eau ?",
        "options": ["A. CO2", "B. H2O", "C. O2", "D. NaCl"],
        "answer": "B"
    },
    {
        "question": "Quel pays a accueilli les Jeux Olympiques d'été de 2016 ?",
        "options": ["A. Chine", "B. Brésil", "C. Royaume-Uni", "D. Russie"],
        "answer": "B"
    },
    {
        "question": "Qui a peint la Joconde ?",
        "options": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Léonard de Vinci", "D. Michel-Ange"],
        "answer": "C"
    },
    {
        "question": "Quel est le plus grand mammifère du monde ?",
        "options": ["A. Éléphant", "B. Baleine bleue", "C. Girafe", "D. Hippopotame"],
        "answer": "B"
    },
    {
        "question": "Quelle langue est principalement parlée au Brésil ?",
        "options": ["A. Espagnol", "B. Portugais", "C. Français", "D. Anglais"],
        "answer": "B"
    },
    {
        "question": "Combien y a-t-il de continents sur Terre ?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Quel est le point d'ébullition de l'eau au niveau de la mer en degrés Celsius ?",
        "options": ["A. 90°C", "B. 95°C", "C. 100°C", "D. 110°C"],
        "answer": "C"
    },
    {
        "question": "Quel est l'organe principal du système respiratoire ?",
        "options": ["A. Cœur", "B. Estomac", "C. Poumon", "D. Foie"],
        "answer": "C"
    },
    {
        "question": "Qui a écrit 'Les Misérables' ?",
        "options": ["A. Victor Hugo", "B. Emile Zola", "C. Gustave Flaubert", "D. Alexandre Dumas"],
        "answer": "A"
    },
    {
        "question": "Quel est l'élément chimique dont le symbole est 'Fe' ?",
        "options": ["A. Fer", "B. Fluor", "C. Francium", "D. Phosphore"],
        "answer": "A"
    },
    {
        "question": "Quelle est la monnaie officielle du Japon ?",
        "options": ["A. Yen", "B. Won", "C. Dollar", "D. Euro"],
        "answer": "A"
    },
    {
        "question": "En quelle année l'homme a-t-il marché sur la Lune pour la première fois ?",
        "options": ["A. 1965", "B. 1969", "C. 1972", "D. 1980"],
        "answer": "B"
    },
    {
        "question": "Quel est le plus long fleuve du monde ?",
        "options": ["A. Amazone", "B. Nil", "C. Mississippi", "D. Yangtsé"],
        "answer": "B"
    },
    {
        "question": "Quelle est la capitale de l’Australie ?",
        "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"],
        "answer": "C"
    },
    {
        "question": "Quel est le symbole chimique de l'or ?",
        "options": ["A. Au", "B. Ag", "C. Pb", "D. Pt"],
        "answer": "A"
    },
    {
        "question": "Quel est le plus grand océan sur Terre ?",
        "options": ["A. Atlantique", "B. Indien", "C. Pacifique", "D. Arctique"],
        "answer": "C"
    },
    {
        "question": "Quel est le sport le plus pratiqué dans le monde ?",
        "options": ["A. Tennis", "B. Football", "C. Basket-ball", "D. Cricket"],
        "answer": "B"
    },
    {
        "question": "Qui est l'auteur de 'Harry Potter' ?",
        "options": ["A. J.K. Rowling", "B. Stephen King", "C. J.R.R. Tolkien", "D. George R.R. Martin"],
        "answer": "A"
    },
    {
        "question": "Quel pays est connu comme le pays du Soleil Levant ?",
        "options": ["A. Chine", "B. Corée du Sud", "C. Japon", "D. Thaïlande"],
        "answer": "C"
    },
    {
        "question": "Quelle est la langue officielle de l’Argentine ?",
        "options": ["A. Portugais", "B. Espagnol", "C. Italien", "D. Français"],
        "answer": "B"
    },
    {
        "question": "Quelle est la capitale du Canada ?",
        "options": ["A. Toronto", "B. Ottawa", "C. Vancouver", "D. Montréal"],
        "answer": "B"
    },
    {
        "question": "Quel est le plus petit état du monde ?",
        "options": ["A. Monaco", "B. Vatican", "C. Malte", "D. Saint-Marin"],
        "answer": "B"
    },
    {
        "question": "Combien de joueurs y a-t-il dans une équipe de football sur le terrain ?",
        "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
        "answer": "C"
    },
    {
        "question": "Qui a découvert la gravité après qu’une pomme lui soit tombée sur la tête ?",
        "options": ["A. Albert Einstein", "B. Isaac Newton", "C. Galileo Galilei", "D. Nikola Tesla"],
        "answer": "B"
    },
    {
        "question": "Quel est le principal gaz responsable de l’effet de serre ?",
        "options": ["A. Oxygène", "B. Azote", "C. Dioxyde de carbone", "D. Hydrogène"],
        "answer": "C"
    },
    {
        "question": "Quelle est la capitale de l’Italie ?",
        "options": ["A. Milan", "B. Venise", "C. Rome", "D. Naples"],
        "answer": "C"
    },
    {
        "question": "Quel est l’organe qui pompe le sang dans le corps humain ?",
        "options": ["A. Poumon", "B. Cerveau", "C. Cœur", "D. Estomac"],
        "answer": "C"
    },
    {
        "question": "Combien de côtés a un hexagone ?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "B"
    },
    {
        "question": "Qui a écrit 'Candide' ?",
        "options": ["A. Voltaire", "B. Rousseau", "C. Diderot", "D. Montesquieu"],
        "answer": "A"
    }
]

    # Ajoute les autres questions ici...


# GUI Quiz Class
class QuizApp:
    def __init__(self, master):
        self.master = master
        master.title("Python Quiz")
        master.geometry("500x300")

        self.question_index = 0
        self.score = 0

        self.question_label = tk.Label(master, text="", wraplength=450, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()

        self.radio_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(master, text="", variable=self.var, value="", font=("Arial", 12))
            btn.pack(anchor="w", padx=50)
            self.radio_buttons.append(btn)

        self.submit_btn = tk.Button(master, text="Submit", command=self.submit_answer)
        self.submit_btn.pack(pady=20)

        self.load_question()

    def load_question(self):
        self.var.set(None)
        q = questions[self.question_index]
        self.question_label.config(text=f"Q{self.question_index + 1}: {q['question']}")
        for i, option in enumerate(q["options"]):
            self.radio_buttons[i].config(text=option, value=option[0])

    def submit_answer(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an option!")
            return

        correct = questions[self.question_index]["answer"]
        if selected == correct:
            self.score += 10

        self.question_index += 1
        if self.question_index < len(questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        result = f"Your final score is: {self.score}/{len(questions)*10}\n"
        if self.score == len(questions)*10:
            result += "🎉 Excellent!"
        elif self.score >= 70:
            result += "👍 Good job!"
        else:
            result += "💡 Better luck next time!"

        messagebox.showinfo("Quiz Finished", result)
        self.master.quit()

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
