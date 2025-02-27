from graphviz import Digraph

def split_number(num):
    """
    Divide um número inteiro 'num' em duas partes (high e low)
    """
    s = str(num)
    n = len(s)
    m = n // 2
    # Divide em string
    high_str = s[:-m] if m < n else ""   # Parte da esquerda
    low_str = s[-m:] if m > 0 else s
    # Converte de volta para int 
    # high, low = int(high_str), int(low_str)
    return high_str, low_str

def karatsuba_flowchart():
    # 1. Recebe inputs
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))

    # 2. Configura o diagrama
    dot = Digraph("Karatsuba_Fluxogram_Dinamico", format="png")
    dot.attr(rankdir='TB', size='10')

    # 3. Definir nós (com texto dinâmico baseado em x, y)
    DefineXY_text = f"Definir x={x} e y={y}"
    Check_text = f"x < 10 ou y < 10?\n({x} < 10 or {y} < 10?)"

    # Multiplicação direta (se x<10 or y<10)
    direct_mult_label = f"Multiplicação Direta:\n{x} * {y}"

    # Dividir x e y (obter x_high, x_low)
    x_high_str, x_low_str = split_number(x)
    y_high_str, y_low_str = split_number(y)

    DivideX = f"Dividir x => x_high={x_high_str}, x_low={x_low_str}"
    DivideY = f"Dividir y => y_high={y_high_str}, y_low={y_low_str}"

    # Exemplo para 'n = max(dígitos de x, y)' e 'm = n//2'
    # Aqui calculamos de fato
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    CalcN_label = f"n = max(dígitos de {x}, {y}) = {n}"
    CalcM_label = f"m = {n} // 2 = {m}"

    # Lógicas do z0,z1,z2 como texto
    z0_label = f"z0 = karatsuba({x_low_str}, {y_low_str})"
    z1_label = f"z1 = karatsuba(({x_low_str} + {x_high_str}), ({y_low_str} + {y_high_str}))"
    z2_label = f"z2 = karatsuba({x_high_str}, {y_high_str})"

    # Combinar - texto genérico
    Combine_label = "Combinar: (z2 * 10^(2m)) + ((z1 - z2 - z0) * 10^m) + z0"

    # Nós
    dot.node("Start", "Início", shape="oval")
    dot.node("DefineXY", DefineXY_text, shape="rectangle")
    dot.node("Check", Check_text, shape="diamond")
    dot.node("DirectMult", direct_mult_label, shape="rectangle")
    dot.node("CalcN", CalcN_label, shape="rectangle")
    dot.node("CalcM", CalcM_label, shape="rectangle")
    dot.node("DivideX", DivideX, shape="rectangle")
    dot.node("DivideY", DivideY, shape="rectangle")
    dot.node("RecZ0", z0_label, shape="rectangle")
    dot.node("RecZ1", z1_label, shape="rectangle")
    dot.node("RecZ2", z2_label, shape="rectangle")
    dot.node("Combine", Combine_label, shape="rectangle")
    dot.node("Return", "Retornar resultado", shape="rectangle")
    dot.node("End", "Fim", shape="oval")

    # Conexões
    dot.edge("Start", "DefineXY")
    dot.edge("DefineXY", "Check")
    dot.edge("Check", "DirectMult", label="Sim")
    dot.edge("DirectMult", "Return")
    dot.edge("Check", "CalcN", label="Não")
    dot.edge("CalcN", "CalcM")
    dot.edge("CalcM", "DivideX")
    dot.edge("DivideX", "DivideY")
    dot.edge("DivideY", "RecZ0")
    dot.edge("RecZ0", "RecZ1")
    dot.edge("RecZ1", "RecZ2")
    dot.edge("RecZ2", "Combine")
    dot.edge("Combine", "Return")
    dot.edge("Return", "End")

    # 4. Gera o diagrama em PNG
    diagram_filename = dot.render("Karatsuba_Fluxogram_Dinamico", format="png")
    print(f"Fluxograma gerado: {diagram_filename}")

if __name__ == "__main__":
    karatsuba_flowchart()
