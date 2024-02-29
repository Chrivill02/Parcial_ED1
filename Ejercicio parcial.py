class Nodo:
    def __init__(self, dato):
        # instanciar
        self.dato = dato
        self.nodo_siguiente = None

class Termino:
    def __init__(self, coeficiente, str_termino):
        self.coeficiente = coeficiente
        self.str_termino = str_termino


class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cola = None
        self.tamannio = 0

    def search_data_retposition(self, user_data):
        current = self.head
        old = self.head
        counter = 0
        while current is not None:
            if current.dato == user_data:
                return counter
            current = current.nodo_siguiente
            counter += 1

    # Metodo insertar al inicio
    def insertar_inicio(self, dato):
        new_nodo = Nodo(dato)
        # si
        if (self.head is None):
            self.head = new_nodo
            return
        new_nodo.nodo_siguiente = self.head
        self.head = new_nodo


    # Metodo insertar al final
    def insertar_final(self, dato):
        new_nodo = Nodo(dato)
        if (self.head == None):
            self.head = new_nodo
            return
        actual = self.head
        while (actual.nodo_siguiente):
            actual = actual.nodo_siguiente

        actual.nodo_siguiente = new_nodo
    def insertar_at_beginning(self,element) :
        if self.head is None:
            new_node = Nodo(element)

            self.head = new_node
        else:
            new_node = Nodo(element)
            new_node.nodo_siguiente = self.head
            self.head = new_node

    def imprimir_listaC(self):
        actual = self.head

        while actual:
            print(actual.dato, end= " ")
            actual = actual.nodo_siguiente
    def imprimir_lista(self):
        actual = self.head

        while actual:
            print(actual.dato.str_termino, end= " ")
            actual = actual.nodo_siguiente



    def insert_at_end(self, element):
        if self.head is None:
            new_node = Nodo(element)
            self.head = new_node
        else:
            current = self.head
            while current.nodo_siguiente is not None:
                current = current.nodo_siguiente
            new_node = Nodo(element)
            current.nodo_siguiente = new_node

    def insert_at_position(self, element, position):
        counter = 1
        current = self.head
        while counter < position - 1 and current is not None:
            counter += 1
            current = current.nodo_siguiente
        if position == 1:
            new_node = Nodo(element)
            new_node.nodo_siguiente = current
            self.head = new_node
        else:
            new_node = Nodo(element)
            new_node.nodo_siguiente = current.nodo_siguiente
            current.nodo_siguiente = new_node
    def delete_from_beginning(self):
        if self.head is None:
            print("La lista está vacía, no se puede eliminar nada")
        else:
            node = self.head
            self.head = self.head.nodo_siguiente
            del node

    def delete_from_last(self):
        if self.head is None:
            print("La lista está vacía, no hay elementos para eliminar")
        else:
            current = self.head
            previous = None
            while current.nodo_siguiente is not None:
                previous = current
                current = current.nodo_siguiente
            previous.nodo_siguiente = None
            del current
    def delete_at_position(self, position):
        if self.head is None:
            print("La lista está vacia, no hay elementos para eliminar")
        else:
            current = self.head
            previous = None
            count = 1
            while current.nodo_siguiente is not None and count < position:
                previous = current
                current = current.nodo_siguiente
                count += 1
            if current == self.head:
                self.head = current.nodo_siguiente
                del current
            else:
                previous.nodo_siguiente = current.nodo_siguiente
                del current
    def count_elements(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.nodo_siguiente
        return count
    def replace_element(self, old_element, new_element):
        current = self.head
        while current is not None:
            if current.dato == old_element:
                current.dato = new_element
                break
            current = current.nodo_siguiente

    def updateAtPosition(self, new_element, position):
        if self.head is None and position != 1:
            print("No element to update in the linked list.")
            return
        elif self.head is None and position == 1:
            newNode = Nodo(new_element)
            self.head = newNode
            return
        count = 1
        current = self.head
        while current.nodo_siguiente is not None and count < position:
            count += 1
            current = current.nodo_siguiente
        if count == position:
            current.dato = new_element
        elif current.next is None:
            print("Not enough elements in the linked list.")


    def insertar_polinomio1(self, coeficiente):
        coeficiente_numerico = coeficiente
        posicion = polinomio1.count_elements()
        if tiene_menos(str(coeficiente)) == "-":
            coeficiente = str(coeficiente)
        else:
            coeficiente = "+" + str(coeficiente)
        if posicion == 0:
            polinomio1.insertar_final(Termino(coeficiente_numerico, coeficiente))
        else:
            coeficiente = str(coeficiente) + "x^" + str(posicion)
            polinomio1.insertar_final(Termino(coeficiente_numerico, coeficiente))

    def insertar_polinomio2(self, coeficiente):
        coeficiente_numerico = coeficiente
        posicion = polinomio2.count_elements()
        if tiene_menos(str(coeficiente)) == "-":
            coeficiente = str(coeficiente)
        else:
            coeficiente = "+" + str(coeficiente)
        if posicion == 0:
            polinomio2.insertar_final(Termino(coeficiente_numerico, coeficiente))
        else:
            coeficiente = str(coeficiente) + "x^" + str(posicion)
            polinomio2.insertar_final(Termino(coeficiente_numerico, coeficiente))
    def sumar(self, polinomio1, polinomio2):

        actual1 = polinomio1.head
        actual2 = polinomio2.head
        for i in range(polinomio1.count_elements()):

            resultado = actual1.dato.coeficiente + actual2.dato.coeficiente
            resultado_numerico = resultado
            if tiene_menos(str(resultado_numerico)) == "-":
                resultado = str(resultado_numerico)
            else:
                resultado = "+" + str(resultado_numerico)
            if i == 0:
                self.insertar_final(Termino(resultado_numerico, resultado))
            else:
                resultado = resultado + "x^" + str(i)
                self.insertar_final(Termino(resultado_numerico, resultado))

            actual1 = actual1.nodo_siguiente
            actual2 = actual2.nodo_siguiente



def tiene_menos(coeficiente):
    for i in coeficiente:
        if i == "-":
            return "-"
        else:
            return "+"
polinomio1 = ListaEnlazada()
polinomio2 = ListaEnlazada()

polinomio1.insertar_polinomio1(-4)
polinomio1.insertar_polinomio1(12)
polinomio1.insertar_polinomio1(30)

polinomio2.insertar_polinomio2(7)
polinomio2.insertar_polinomio2(10)
polinomio2.insertar_polinomio2(20)

polinomioC = ListaEnlazada()
print("Polinomio a:")
polinomio1.imprimir_lista()
print("\nPolinomio b:")
polinomio2.imprimir_lista()
opcion = "1"
while opcion != "0":
    print("\n1. Ingresar componentes al polinomio")
    print("2. Adición y sustracción")
    print("3. Evaluar polinomios")
    print("4. Mostrar polinomios")
    print("0. Salir")
    opcion = input("")
    if opcion == "1":
        print("1. Polinomio a")
        print("2. Polinomio b")
        opcion2 = input("Ingrese el polinomio a ingresar un coeficiente: ")
        if opcion2 == "1":
            coeficiente = int(input("Ingrese un coeficiente: "))
            polinomio1.insertar_polinomio1(coeficiente)
        else:
            coeficiente = int(input("Ingrese un coeficiente: "))
            polinomio2.insertar_polinomio2(coeficiente)
    elif opcion == "2":
        print("1. Suma")
        print("2. Resta")
        opcion2 = input("Ingrese una opción: ")
        if opcion2 == "1":
            polinomioC.sumar(polinomio1, polinomio2)
            polinomioC.imprimir_lista()

    elif opcion == "3":
        print("1. Polinomio a")
        print("2. Polinomio b")
        opcion2 = input("")
        polinomioC.insertar_final(Termino())
    elif opcion == "4":
        print("Polinomio a")
        polinomio1.imprimir_lista()
        print("\nPolinomio b")
        polinomio2.imprimir_lista()
    else:
        print("Opcion incorrecta")
