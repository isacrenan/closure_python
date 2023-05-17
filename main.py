
'''função que recebe um multiplicador e cria outra função que multiplica
trplica ou quadruplica um número e exibe o valor no terminal'''



#recebe o valor do multiplicador
def multiplicador(multiplicador): 
    
    #recebe o numero a ser multiplicador * o multiplicador
    def multiplicar(num): 
        
        # retorna o valor da função dentro da função
        return num * multiplicador
    
    #retorna outra função dentro do escopo da função sem executar
    return multiplicar
        
        
#chamada da função passando o valor do multiplicador
multiplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)


#passar o numero que será usado * o multiplicador e executa a função dentro do escopo da primeira função
# E exibe o valor no terminal
print(multiplicar(200))
print(triplicar(300))
print(quadruplicar(400))