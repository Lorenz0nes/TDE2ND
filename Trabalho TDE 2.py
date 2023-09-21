def f(x):
    return x ** 2

def g(x):
    return x - 1

def compose_functions(f, g):
    def composed_function(x):
        return f(g(x))
    return composed_function

gf = compose_functions(g, f)
gg = compose_functions(g, g)
ff = compose_functions(f, f)
fg = compose_functions(f, g)

# Exemplos de cálculos para as composições
x_values = [4, 3, 5] # Somente mudar os números para ter algum resultado

print("(g ° f)(x):")
for x in x_values:
    result = gf(x)
    print(f"  (g ° f)({x}) = {result}")

print("\n(g ° g)(x):")
for x in x_values:
    result = gg(x)
    print(f"  (g ° g)({x}) = {result}")

print("\n(f ° f)(x):")
for x in x_values:
    result = ff(x)
    print(f"  (f ° f)({x}) = {result}")

print("\n(f ° g)(x):")
for x in x_values:
    result = fg(x)
    print(f"  (f ° g)({x}) = {result}")
