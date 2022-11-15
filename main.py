from tkinter import Tk, Label, Text, Button, messagebox


# Recebe o input e reformata a string
def input(widget):
      text = widget.get('1.0', 'end')
      
      if text == '\n':
            messagebox.showerror("ERRO!", "Você não digitou nada!")
            return False
      
      text = text.upper().replace(',', '').replace('.', '')
      word_counter(text)


# Faz o processo de contagem de palavras e armazena as mesmas em um dicionário
def word_counter(text):
      splited_text = text.split()
      word_dictionary = dict()
      
      for word in splited_text:
            if word in word_dictionary.keys():
                  word_dictionary[word] += 1
            else:
                  word_dictionary[word] = 1
      
      # Organizando em ordem crescente
      word_dictionary = dict(sorted(word_dictionary.items(),
                                    key=lambda x: x[1], 
                                    reverse=True))
      
      summon_window(word_dictionary)


# Cria a window com as respostas
def summon_window(dictionary):
      new_window = Tk()
      new_window.resizable(False, False)
      new_window.title("Frequency")
      
      for k, v in dictionary.items():
            Label(new_window, text=f'{k} = {v}',
                  font=('Arial', 15)).pack(padx=10)


# Window
window = Tk()
window.resizable(False, False)
window.title("Word Frequency")

# Widgets
Label(window, text="Insira o texto abaixo",
      font=('Arial', 20), pady=20, padx=10).pack()

input_widget = Text(window, height=10, font=('Times New Roman', 12))
input_widget.pack(padx=10, pady=5)

Button(window, text='CONTAR', font=('Arial', 15),padx=10,
       pady=10, command=lambda: input(input_widget)).pack()


window.mainloop()
