import tkinter as tk
from tkinter import ttk, messagebox

from ServicoFixo import ServicoFixo
from ServicoPorHora import ServicoPorHora
from Orcamento import Orcamento


orcamento = Orcamento()


def atualizar_resultado():
    texto = orcamento.listar()
    if not texto:
        texto = "Nenhum serviço adicionado.\n"
    texto += f"\nTotal: R$ {orcamento.calcular_total():.2f}"
    label_resultado.config(text=texto)


def adicionar_servico():
    opcao = escolha.get()

    if opcao == "Limpeza":
        servico = ServicoFixo("Limpeza", 60)
    elif opcao == "Troca de pasta térmica":
        servico = ServicoFixo("Troca de pasta térmica", 40)
    else:
        try:
            horas = float(entrada_horas.get().replace(",", "."))
        except ValueError:
            messagebox.showerror("Erro", "Digite uma quantidade válida de horas.")
            return

        if horas <= 0:
            messagebox.showerror("Erro", "As horas devem ser maiores que zero.")
            return

        servico = ServicoPorHora("Diagnóstico", 30, horas)

    orcamento.adicionar(servico)
    atualizar_resultado()
    abas.select(aba_orcamento)


def limpar_orcamento():
    orcamento.limpar()
    atualizar_resultado()


janela = tk.Tk()
janela.title("PC Manager — Orçamentos")
janela.geometry("430x340")

abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True, padx=12, pady=12)

aba_servicos = ttk.Frame(abas)
aba_orcamento = ttk.Frame(abas)
abas.add(aba_servicos, text="Serviços")
abas.add(aba_orcamento, text="Orçamento")

tk.Label(aba_servicos, text="Escolha o serviço:").pack(pady=(20, 5))
escolha = tk.StringVar(value="Limpeza")
tk.OptionMenu(
    aba_servicos,
    escolha,
    "Limpeza",
    "Troca de pasta térmica",
    "Diagnóstico por hora"
).pack()

tk.Label(aba_servicos, text="Horas (somente para diagnóstico):").pack(pady=(15, 5))
entrada_horas = tk.Entry(aba_servicos)
entrada_horas.insert(0, "1")
entrada_horas.pack()

tk.Button(
    aba_servicos,
    text="Adicionar ao orçamento",
    command=adicionar_servico
).pack(pady=20)

tk.Label(
    aba_orcamento,
    text="Resumo do orçamento",
    font=("Arial", 12, "bold")
).pack(pady=15)

label_resultado = tk.Label(aba_orcamento, justify="left", anchor="w")
label_resultado.pack(padx=15, anchor="w")

tk.Button(
    aba_orcamento,
    text="Limpar orçamento",
    command=limpar_orcamento
).pack(pady=20)

atualizar_resultado()
janela.mainloop()
