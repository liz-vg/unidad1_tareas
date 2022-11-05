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
    print("\nid: " + str(self.verId()) + "\nTitulo: " + self.verTitulo() + "\ngenero: " + self.verGenero() + "\nisbn: " + str(self.verIsbn()) + "\neditorial: " + self.verEditorial() + "\nautor:" + self.verAutor())
    
def mostrarTres():
  libros = []
  with open("libros.txt") as libro_texto:
    lineas = libro_texto.readlines()
    random.shuffle(lineas)
    for linea in lineas:
      libros.append(json.loads(linea))
  for i in range(3):
    libro = libros[i]
    libro_formateado = Libro(libro["id"], libro["titulo"], libro["genero"], libro["isbn"], libro["editorial"], libro["autor"])
    libro_formateado.listarLibro()
  print("\n")

print ("Bienvenidos a la librería Silabuz")
menu = {}
menu['1']="Mostrar tres libros al azar" 
menu['2']="Listar libros"
menu['3']=" Agregar libro"
menu['4']="Eliminar libro"
menu['5']="Buscar libro por ISBN o título"
menu['6']="Ordenar libros por título"
menu['7']="Buscar libro por autor, editorial o género"
menu['8']="Buscar libros por número de autores"
menu['9']="Editar o actualizar datos"
menu['10']="Guardar libros"
while True: 
  opciones=list(menu.keys())
  for opcion in opciones: 
    print (opcion+")", menu[opcion])

  seleccion=input("Por favor seleccione una opción: ") 
  if seleccion =='1':
    mostrarTres()
  elif seleccion == '2':
    break
  elif seleccion == '3':
    break
  elif seleccion == '4':
    break
  elif seleccion == '5':
    break
  elif seleccion == '6':
    break
  elif seleccion == '7':
    break
  elif seleccion == '8':
    break
  elif seleccion == '9':
    break
  elif seleccion == '10':
    break
  else: 
    print ("\n¡Opción incorrecta!\n")