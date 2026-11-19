PC MANAGER — SEMINÁRIO DE POO

ESTRUTURA (todos os arquivos na mesma pasta)
PC_Manager/
  Servico.py         -> Classe base: nome e metodo calcular_preco
  ServicoFixo.py     -> Herança: preco fixo
  ServicoPorHora.py  -> Herança: preco multiplicado pelas horas
  Orcamento.py       -> Guarda os serviços e soma os preços
  main.py            -> Interface gráfica com Tkinter

COMO EXECUTAR
1. Instale Python com suporte a Tkinter.
2. Mantenha os arquivos .py juntos na mesma pasta.
3. Abra um terminal nessa pasta.
4. Execute: python main.py
   (No Windows, pode ser: py main.py)

COMO TESTAR
- Escolha "Limpeza" e clique em "Adicionar ao orçamento": R$ 60.00
- Escolha "Troca de pasta térmica": total de R$ 100.00
- Escolha "Diagnóstico por hora", digite 2: total de R$ 160.00
- Clique em "Limpar orçamento": total de R$ 0.00

CONCEITOS PARA EXPLICAR
- __init__: construtor que inicializa o objeto.
- self: referencia ao proprio objeto.
- __nome: encapsulamento (name mangling).
- @property: permite ler nome como atributo (servico.nome).
- super(): chama o construtor da classe pai.
- Herança: ServicoFixo e ServicoPorHora herdam de Servico.
- Polimorfismo: calcular_preco() faz calculos diferentes.
- Relacionamento: Orcamento armazena objetos de serviço.
- append(): insere um serviço na lista.
- mainloop(): roda o loop de eventos da janela.

OBSERVACAO
Rode apenas main.py. Os outros arquivos definem classes e são importados.
Sem banco de dados, porque o enunciado de POO não o exige.
