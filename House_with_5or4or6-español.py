
#mapa libreta
mapa = [
    ("cine", 5, 7, None, 2, "el cine está lleno de gente:: 200 obreros expertos en concreto, acabados por el trabajo & sus niños comiendo palomitas:: reunidos para ver caricaturas:: una serie que trata de un duo cómico:: un aristócrata alto y gordo que chilla en una voz aguda con acento extraño:: un tipo musculoso con el pelo lleno de gel que contesta en un tono muy bajo:: quienes están trabajando en una construcción imposible que nunca van a cumplir:: para que contraten 200 obreros expertos en concreto, acabados por el trabajo & sus niños comiendo palomitas:: reunidos para ver caricaturas"),
    ("entradapozas", None, 4, None, None, "Cae la noche & el camino sin asfaltar & sin luz:: nada mas visible que sombras, aunque, cuando alcanzas la clima del cerro te sacude una sensación profética:: te das cuenta que has encontrado el lugar que buscabas:: pocos metros adelante ves a una figura andando, envuelto de la cabeza a los pies en papel higiénico"),
    ("arco", 6, 3, 0, None, "un arco:: hecho de serpientes, hechas de concreto:: representando los siete pecados capitales de CEMEX"),
    ("ballena", 2, None, 7, 9, "¿como se llama este lugar? preguntas a la persona al lado de ti. es la casa con el techo en forma de ballena, te contesta en una voz aguda:: ¿como esto pretende ser una ballena? estas a punto de decir con escepticismo:: pero justo a tiempo espías el tragaluz, situado como respiradero:: que conduce al tejado a travez de el techo:: Sube las escaleras al tejado"),
    ("sendero", 1, None, 5, 6, "un camino, iluminado por faros altos y delgados:: una vista que te parece surreal:: ya que ningún pueblo en kilómetros tiene un generador"),
    ("jaulas", 4, 0, None, 4, "Las jaulas de las bestias están vacías:: sus ocupantes han sido liberados al bosque a perecer:: o a procrear con la fauna local, creando nuevas especies híbridas y desconocidas"),
    ("invernadero", 4, 2, 4, None, "el invernadero está lleno de ceniza helada:: bajo la ceniza, orquídeas muertas:: cientos :: sus esqueletos, grises y rígidos petrificados por el frío"),
    ("cabana", 0, 8, None, 3, "la cama esta rodeada por una nube de mosquitos voraces:: te parece que nadie nunca durmió aquí:: en una pared letras apenas visibles y poco legibles:: en la otra pared un espejo"),
    ("plutarco", 7, None, None, None, "este es un cuarto que nunca fue construido:: en el piso un desorden de planos de arquitectura, representando miles de construcciones no realizadas:: incluyendo un plano del cuarto en el que estas ahora:: cuando te inclinas a recogerlo el piso se derrumba bajo tus pies:: & caes cinco o cuatro o seis pisos al suelo:: soltando una tira de papel higiénico"),
    ("tejado", None, None, 3, None, "sumido en el concreto del tejado hay una bañera vacía:: es el ojo de la ballena:: cuando te sientas en la bañera ves desde la perspectiva de la ballena el brillo del camino iluminado:: los contornos extraños de los edificios & la periferia obscura del espacio:: que se extiende hasta donde el bosque empieza de nuevo"),
]

#inicio
ubicacion = 1

def describeLocacion ():
    global ubicacion

    cuarto = mapa [ubicacion]
    desc = cuarto [5]

    print (desc)

def cambiarLocacion (direccion):
    global ubicacion

    cuarto = mapa [ubicacion]
    siguiente_destino = None

    if direccion=='n':
        siguiente_destino = cuarto [1]

    if direccion=='s':
        siguiente_destino = cuarto [2]

    if direccion=='e':
        siguiente_destino = cuarto [3]

    if direccion=='o':
        siguiente_destino = cuarto [4]

    if (siguiente_destino==None):
        print (".")
    else:
        ubicacion = siguiente_destino


while True:
    describeLocacion ()
    eleccion = input ("(n/s/e/o): ")
    cambiarLocacion (eleccion)
