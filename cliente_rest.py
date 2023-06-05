import requests
from tkinter import Tk, Label, Button, Entry

def send_request(operation):
    if operation == "operações":
        response = requests.get(f"http://ec2-3-133-82-159.us-east-2.compute.amazonaws.com:3000/calculadora/operacoes")
    
    else:
        num1 = entry_num1.get()
        num2 = entry_num2.get()
        response = requests.post(f"http://ec2-3-133-82-159.us-east-2.compute.amazonaws.com:3000/calculadora/operacoes/{operation}/{num1}/{num2}")
    
    result = response.json()
    label_result.config(text=result)

# Configurar a janela
window = Tk()
window.title("Calculadora")
window.geometry("600x500")

# Configurar os campos de texto
entry_num1 = Entry(window)
entry_num1.pack()

entry_num2 = Entry(window)
entry_num2.pack()

# Configurar os botões
button_operacoes = Button(window, text="Operações", command=lambda: send_request("operações"))
button_operacoes.pack()

button_soma = Button(window, text="+", command=lambda: send_request("soma"))
button_soma.pack()

button_subtracao = Button(window, text="-", command=lambda: send_request("subtrai"))
button_subtracao.pack()

button_multiplicacao = Button(window, text="*", command=lambda: send_request("multiplica"))
button_multiplicacao.pack()

button_divisao = Button(window, text="/", command=lambda: send_request("divide"))
button_divisao.pack()

# Configurar o rótulo para exibir o resultado
label_result = Label(window, text="")
label_result.pack()

# Executar a janela
window.mainloop()