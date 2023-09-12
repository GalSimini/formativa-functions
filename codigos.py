#dupla: Gabriel Marques Simini / Enrico Bernz Reichow Santos
# g f
def composicao_g_de_f(x, f, g):
    return g(f(x))

# g g
def composicao_g_de_g(x, g):
    return g(g(x))

# f  f
def composicao_f_de_f(x, f):
    return f(f(x))

# f  g
def composicao_f_de_g(x, f, g):
    return f(g(x))

# pegar as funções
f_formula = input("Digite a função f(x): ")
g_formula = input("Digite a função g(x): ")

# fazer as formulas aqui
def f(x):
    return eval(f_formula)

def g(x):
    return eval(g_formula)

#valor de x pra fazer a conta
valor_x = float(input("Digite o valor de x: "))

# ta armazenando a resp
resultado_g_de_f = composicao_g_de_f(valor_x, f, g)
resultado_g_de_g = composicao_g_de_g(valor_x, g)
resultado_f_de_f = composicao_f_de_f(valor_x, f)
resultado_f_de_g = composicao_f_de_g(valor_x, f, g)

# aqui ta printando
print(f"g ° f(x) = {resultado_g_de_f}")
print(f"g ° g(x) = {resultado_g_de_g}")
print(f"f ° f(x) = {resultado_f_de_f}")
print(f"f ° g(x) = {resultado_f_de_g}")

#seguinte deu trabalho pra fazer isso sor da um pontinho pra nois ai tmj (UwU)