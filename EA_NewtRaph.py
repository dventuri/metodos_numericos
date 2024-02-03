def newton_raphson(func, Dfunc, x0, max_iter=50, tol_err=1E-6):
    '''
    Solução aproximada de f(x)=0 a partir de uma estimativa inicial x0 pelo
    método de Newton-Raphson.
    '''

    # verificar se a estimativa inicial já não é a resposta
    if(abs(func(x0)) <= tol_err):
        print("Resposta encontrada")
        print("x = ", x0)
        print("Iterações: ", 0)
        return x0

    # início do método
    for i in range(max_iter):

        x_novo = x0 - func(x0)/Dfunc(x0)

        # verificar se a derivada da função é não-nula
        if(Dfunc(x0) == 0):
            print("Derivada nula, impossível continuar.")
            return None

        if(abs(func(x_novo)) <= tol_err):
            print("Resposta encontrada")
            print("x = ", x_novo)
            print("Iterações: ", i+1)
            return x_novo

        x0 = x_novo

    print("Máximo número de iterações atingido")
    print("x = ", x_novo)

    return x_novo
