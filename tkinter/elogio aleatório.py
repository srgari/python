# elogio aleatório
# w.counter = 0
# ttk.Label(w, text = 'Ou receba uma frase motivacional, em inglês', font = 'arial, 14').grid(column = 1, row = 7)
# def random_compliment():
#     if w.counter < 10:
#         l = ['I like you', 'you can do it!','you are golden!',
#         'you are terrific!',
#         'you brighten my day',
#         'you are my sunshine']
#         tk.Label(w, text = f'                                                                  ',  font=("Helvetica", 16)).grid(row = 8, column = 1,)
#         tk.Label(w, text = np.random.choice(l),  anchor = 'e', font=("Helvetica", 16)).grid(row = 9, column = 1)
#         w.counter = w.counter + 1
#     else:
#         l = ["that's enough for today",
#         "It doesn't get any better than this!",
#         "Enjoying yourself?"]
#         tk.Label(w, text = '                                                               ',font=("Helvetica", 16)).grid(row = 8, column = 1)
#         tk.Label(w, text = np.random.choice(l),font=("Helvetica", 16)).grid(row = 8, column = 1)

# tk.Button(w, text = f'compliment', command = random_compliment).grid(row = 8, column = 1)