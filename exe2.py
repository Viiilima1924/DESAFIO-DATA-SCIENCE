import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def plot_data():
    #  ler CSV file
    data = pd.read_csv('deaths-temperature-gasparrini new.csv')

    # Extrair data
    pais = data['country']
    temp = data['Extreme cold']

    # Criar a figura
    fig, grafico = plt.subplots()
    grafico.plot(pais, temp, marker='o', linestyle='-', color='b')

    # add as labels
    grafico.set_xlabel('país')
    grafico.set_ylabel('Temperatura')
    grafico.set_title('Temperatura extremamente frias nos países')

    # mostrar o grafico
    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# janela tkinter
janela = tk.Tk()
janela.title('Qual país teve a menor temperatura?')

# button
botao = tk.Button(janela, text='Exibir Gráfico', command=plot_data)
botao.pack(pady=20)

# loop tkinter
janela.mainloop()
