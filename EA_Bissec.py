def bissecao(func, a, b, max_iter=50, tol_err=1E-3):
    '''Solução aproximada de f(x)=0 no intervalo [a,b] pelo método da bisseção.

    Parâmetros
    ----------
    func : função
        A função para a qual estamos tentando aproximar a solução f(x)=0.
    a,b : números
        O intervalo no qual será procurada a solução. A função retorna None
        se f(a)*f(b) >= 0, já que a solução não é garantida.
    max_iter : (positivo) inteiro
        O número máximo de iterações que do método.
    tol_err : (positivo) real
        A tolerância aceita para a aproximação da resposta, f(x)<tol_err.

    Retorna
    -------
    x : número
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.

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
        x = 0.5*(a+b)           #usando o valor médio do intervalo como estimativa
        f_x = func(x)
        if (f_a*f_x < 0):
            a = a
            b = x
        elif (f_b*f_x < 0):
            a = x
            b = b
        elif (abs(f_x) < tol_err):
            print("Resposta encontrada")
            print("x = ", x)
            print("Iterações: ", n+1)
            return x
        else:
            print("Método falhou.")
            return None
    
    print("Máximo número de iterações atingido")
    print("x = ", 0.5*(a+b))
    return 0.5*(a+b)


def dummy_function(input):
    output = 2*input
    return output
