def bissecao(func, a, b, max_iter=50, tol_err=1E-6):
    '''
    Solução aproximada de f(x)=0 no intervalo [a,b] pelo método da bisseção.

    Parâmetros
    ----------
    func : função
        A função para a qual estamos tentando aproximar a solução f(x)=0.
    a,b : números
        O intervalo no qual será procurada a solução.
    max_iter : (positivo) inteiro
        O número máximo de iterações que do método.
    tol_err : (positivo) real
        A tolerância aceita para a aproximação da resposta, f(x)<tol_err.

    Retorna
    -------
    x : número
        Raiz da função, dentro da tolerância do erro, calculada pelo método
        da bisseção. Retorna None se não houver raiz dentro do intervalo
        fornecido.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> bissecao(f,1,2,25)
    1.618033990263939
    >>> f = lambda x: (2*x - 1)*(x - 3)
    >>> bissecao(f,0,1,10)
    0.5
    '''

    #calcular a função nos valores iniciais
    f_a = func(a)
    f_b = func(b)

    #verificar se algum dos valores já não é a própria resposta
    if(abs(f_a)<tol_err):
        print("Resposta encontrada")
        print("x = ", a)
        print("Iterações: ", 0)
        return a

    if(abs(f_b)<tol_err):
        print("Resposta encontrada")
        print("x = ", b)
        print("Iterações: ", 0)
        return b

    #verificar se o intervalo fornecido é válido
    if((f_a*f_b)>0):
        print("Intervalo incorreto")
        return None

    #cálculo do método da bisseção
    for n in range(max_iter):
        x = (a+b)/2           #usando o valor médio do intervalo como estimativa
        f_x = func(x)
        if (abs(f_x) < tol_err):
            print("Resposta encontrada")
            print("x = ", x)
            print("Iterações: ", n+1)
            return x

        if (f_a*f_x < 0):
            a = a
            b = x
        elif (f_b*f_x < 0):
            a = x
            b = b

        f_a = func(a)
        f_b = func(b)

    print("Máximo número de iterações atingido")
    print("x = ", 0.5*(a+b))

    return 0.5*(a+b)


def dummy_function(input):
    output = 2*input
    return output
