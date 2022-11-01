# PROPERTIES
# Com o property() do Python, você pode criar atributos gerenciados em suas classes. 
# Você pode usar atributos gerenciados, também conhecidos como propriedades, 
# quando precisar modificar sua implementação interna sem alterar a API pública da classe.
# @property : um decorador, que é uma função que  executa antes da função.



class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter # modificação - para poder modificar o x
    def x(self, value):
        self._x += value

    @x.deleter # deleção
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
