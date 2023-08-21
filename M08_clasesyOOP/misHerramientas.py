class Matematica:
    def __init__(self, lista):
        self.lista = lista

    def isPrimo(self):
        for i in self.lista:
            if (self.__isPrimo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def convertGrados(self,origen,destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son',
                   self.__convertGrados(i, origen, destino),'grados',destino)
    
    def __isPrimo(self,numero):
        es_primo= True
        for i in range(2,numero):
            if(numero % i == 0):
                es_primo = False
                break
            return es_primo
        
    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))

    def valorModal(self, lista = []):
        dic_mas_repetido = {}
        for numero in lista:
            if(numero in dic_mas_repetido):
                dic_mas_repetido[numero] += 1
            else:
                dic_mas_repetido[numero] = 1
        num_mas_repetido = max(dic_mas_repetido,key=dic_mas_repetido.get)
        cantidad_repetido = dic_mas_repetido[num_mas_repetido]
        return num_mas_repetido,cantidad_repetido
    
    def __convertGrados(self,valor,origen,destino):
        valor_destino = None
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino
    
    def __factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.factorial(numero - 1)
        return numero