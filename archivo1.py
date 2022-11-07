import random
import json

class Libro:
  def __init__(self, id, titulo, genero, isbn, editorial, autor):
    self.id = id
    self.titulo = titulo
    self.genero = genero
    self.isbn = isbn
    self.editorial = editorial       
    self.autor = autor
  # Metodos para acceder a los datos
  def verId(self):
    return self.id
  def verTitulo(self):
    return self.titulo
  def verGenero(self):
    return self.genero
  def verIsbn(self):
    return self.isbn
  def verEditorial(self):
    return self.editorial
  def verAutor(self):
    return self.autor
    
  def listarLibro(self):
    print("\nID: " + str(self.verId()) + "\nTitulo: " + self.verTitulo() + "\nGenero: " + self.verGenero() + "\nISBN: " + str(self.verIsbn()) + "\nEditorial: " + self.verEditorial() + "\nAutor:" + self.verAutor())
  def libroAguardar(self):
    libro = {"id":int(self.verId()), "titulo": self.verTitulo(), "genero":self.verGenero(), "isbn":int(self.verIsbn()), "editorial": self.verEditorial(), "autor": self.verAutor()}
    return json.dumps(libro)

def cargarLibros(archivo):
  with open(archivo) as libro_texto:
    lineas = libro_texto.readlines()
  return [json.loads(linea) for linea in lineas]

def mostrarTres():
  libros = cargarLibros("libros.txt")
  random.shuffle(libros)
  for i in range(3):
    libro = libros[i]
    libro_formateado = Libro(libro["id"], libro["titulo"], libro["genero"], libro["isbn"], libro["editorial"], libro["autor"])
    libro_formateado.listarLibro()
  print("\n")

def todosLibros():
  libros = cargarLibros("libros.txt")
  for libro in libros:
    libro_formateado = Libro(libro["id"], libro["titulo"], libro["genero"], libro["isbn"], libro["editorial"], libro["autor"])
    libro_formateado.listarLibro()
  print("\n")

print ("Bienvenidos a la librería Silabuz")
menu = {}
menu['1']="Mostrar tres libros al azar" 
menu['2']="Listar libros"
menu['3']="Agregar libro"
menu['4']="Eliminar libro"
menu['5']="Buscar libro por ISBN o título"
menu['6']="Ordenar libros por título"
menu['7']="Buscar libro por autor, editorial o género"
menu['8']="Buscar libros por número de autores"
menu['9']="Editar o actualizar datos"
menu['10']="Guardar libros en nuevo archivo"
while True:
  opciones=list(menu.keys())
  for opcion in opciones: 
    print (opcion+")", menu[opcion])
  seleccion=input("Por favor seleccione una opción: ") 
  if seleccion =='1':
    mostrarTres()
  elif seleccion == '2':
    todosLibros()
    break
  elif seleccion == '3':
    id = input("Ingrese ID del libro: ")
    titulo = input("Ingrese el título del libro: ")
    genero = input("Ingrese el genero del libro: ")
    isbn = input("Ingrese el isbn del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    autor = input("Ingrese el autor del libro: ")
    libro_nuevo = Libro(id, titulo, genero, isbn, editorial, autor)
    with open("libros.txt", "a") as libro_texto:
      libro_texto.write("\n"+str(libro_nuevo.libroAguardar()))
    print("\nSe guardó existosamente.")
    libro_nuevo.listarLibro()
    break
  elif seleccion == '4':
    todosLibros()
    eliminar = int(input("Introduzca el ID del libro a eliminar: "))
    libros = cargarLibros("libros.txt")
    for libro in libros:
      indice = libros.index(libro)
      if libro.get("id") == eliminar:
        del libros[indice]
    for libro in libros:
      nuevaLineaTexto = Libro(libro["id"], libro["titulo"], libro["genero"], libro["isbn"], libro["editorial"], libro["autor"])
      if libro == libros[0]:
        with open("libros.txt", "w") as libro_texto:
          libro_texto.write(str(nuevaLineaTexto.libroAguardar()))
      else:
        with open("libros.txt", "a") as libro_texto:
          libro_texto.write("\n"+str(nuevaLineaTexto.libroAguardar()))
        
    print("\nSe eliminó existosamente.")
    todosLibros()
    break
  elif seleccion == '5':
    continuar = "si"
    while continuar == "si":
      buscar = str(input("Introduzca el Título o ISBN del libro a buscar: "))
      libros = cargarLibros("libros.txt")
      existencia = 0
      for libro in libros:
        if str(libro.get("isbn")) == buscar or libro.get("titulo") == buscar :
          existencia = libro
      if existencia:
        print("Libro encontrado:\n ISBN: "+str(existencia.get("isbn"))+", Título: "+existencia.get("titulo")+", Autor: "+existencia.get("autor"))
        continuar = input("Desea volver a consultar? Si/No: ").lower()
      else:
        print("¡Libro no encontrado!\n")
        continuar = input("Desea continuar? Si/No: ").lower()        
    break
  elif seleccion == '6':
    print("\nTítulos ordenados de forma alfabética:")
    libros = cargarLibros("libros.txt")
    ordenado = []
    for libro in libros:
      ordenado.append(libro.get("titulo"))
    ordenado.sort()
    for titulo in ordenado:
      print (titulo)
    break
  elif seleccion == '7':
    opciones = f"""{'#'*22}
Realizar búsqueda por:
a) autor.
b) editorial.
c) género.
{'#'*22}"""
    continuar = "si"
    while continuar == "si":
      print(opciones)
      tipoBusqueda = input("Ingrese su opción: ").lower()
      while tipoBusqueda not in {"a", "b", "c"}:
        tipoBusqueda = input("Opción incorrecta, Vuelva a intentarlo: ").lower()
      if tipoBusqueda == "a":
        tipoBusqueda = "autor"
      elif tipoBusqueda == "b":
        tipoBusqueda = "editorial"
      elif tipoBusqueda == "c":
        tipoBusqueda = "genero"
      buscar = input(f"Ingrese {tipoBusqueda} del libro a buscar: ")
      libros = cargarLibros("libros.txt")
      existencia = 0
      for libro in libros:
        if str(libro.get(tipoBusqueda)) == buscar:
          existencia = libro
      if existencia:
        print("Libro encontrado:\n ISBN: "+str(existencia.get("isbn"))+", Título: "+existencia.get("titulo")+", Autor: "+existencia.get("autor"))
      else:
        print("¡Libro no encontrado!\n")
      continuar = input("Desea volver a consultar? Si/No: ").lower()
    break
  elif seleccion == '8':
    libros = cargarLibros("libros.txt")
    for libro in libros:
      libro["numeroAutores"] = len(libro.get("autor").split(','))
    cantidadConsulta = int(input("\nIngrese el número de autores: "))
    for libro in libros:
      if libro.get("numeroAutores") == cantidadConsulta:
        print("Libro encontrado:\n ISBN: "+str(libro.get("isbn"))+", Título: "+libro.get("titulo")+", Autor: "+libro.get("autor"))    
    break
  elif seleccion == '9':
    todosLibros()
    editar = int(input("Introduzca el ID del libro a editar: "))
    mensaje = f"""{'#'*30}
¿Qué dato desea modificar?:
a) ID.
b) Título.
c) Género.
d) ISBN.
e) Editorial.
f) Autor.
{'#'*30}
Escriba su opción y presione enter: """
    valorOpcion = {"a":"id", "b": "titulo", "c":"genero", "d":"isbn", "e": "editorial", "f": "autor"}
    opcion = input(mensaje)
    while opcion not in valorOpcion:
      print("¡Valor incorrecto!\n vuelva a intentar: ")
      opcion = input(mensaje)
    editarValor = valorOpcion[opcion]
    nuevoValor = input("Ingrese nuevo valor: ")
    libros = cargarLibros("libros.txt")
    for libro in libros:
      if libro.get("id") == editar:
        libro[editarValor] = nuevoValor
      nuevaLineaTexto = Libro(libro["id"], libro["titulo"], libro["genero"], libro["isbn"], libro["editorial"], libro["autor"])
      libroEditado = nuevaLineaTexto
      if libro == libros[0]:
        with open("libros.txt", "w") as libro_texto:
          libro_texto.write(str(nuevaLineaTexto.libroAguardar()))
      else:
        with open("libros.txt", "a") as libro_texto:
          libro_texto.write("\n"+str(nuevaLineaTexto.libroAguardar()))
        
    print("\nSe editó existosamente.")
    libroEditado.listarLibro()
    break
  elif seleccion == '10':
    archivo = str(input("Ingrese un nombre de archivo con su extensión: "))
    libros = cargarLibros("libros.txt")
    for libro in libros:
      nuevaLineaTexto = Libro(libro["id"], libro["titulo"], libro["genero"], libro["isbn"], libro["editorial"], libro["autor"])
      if libro == libros[0]:
        with open(archivo, "w") as libro_texto:
          libro_texto.write(str(nuevaLineaTexto.libroAguardar()))
      else:
        with open(archivo, "a") as libro_texto:
          libro_texto.write("\n"+str(nuevaLineaTexto.libroAguardar()))
    todosLibros()
    print(f"\nSe guardaron los libros en el archivo {archivo}.")
    break
  else: 
    print ("\n¡Opción incorrecta!\n")