
#mapa libreta
mapa = [
    ("cinema", 5, 7, None, 2, "the cinema is packed with people:: 200 day labourers concrete workers clocked off for the night & their palomita-eating children:: congregated to watch cartoons:: a series about a comic duo:: one tall & fat aristocrat who squeaks in a high-pitched voice:: one muscular brylcreemed beefcake who answers in an accent:: who are working to build an impossible construction that will never ever be finished:: for the purposes of which they hire 200 day labourers concrete workers clocked off for the night & their palomita-eating children:: congregated to watch cartoons"),
    ("entrancepozas", None, 4, None, None, "night is falling & the path unpaved & unlit:: nothing but shadows ahead, tho as you reach the crest of the hill you are struck by a fateful sensation:: you know that you have found the place you have been looking for:: shaken, you look down at yourself & see that you are wrapped head to toe in toilet paper"),
    ("arch", 6, 3, 0, None, "an archway:: made of snakes made of concrete:: depicting the seven deadly sins of CEMEX"),
    ("whale", 2, None, 7, 9, "what is this place called? you ask the person next to you. it’s the house with the roof like a whale, they reply in a low baritone. how is this meant to be a whale? you are about to ask skeptically:: but just in time you spy the skylight, positioned like a blowhole:: leading through the ceiling to the roof"),
    ("lightedwalkway", 1, None, 5, 6, "a walkway, illuminated by tall spindly electric lampposts:: a sight which strikes you as surreal:: since no town has a generator for miles"),
    ("enclosures", 4, 0, None, 4, "the animal enclosures are empty:: their occupants have been released into the forest to perish:: or to interbreed with local fauna creating strange new hybrid species"),
    ("hothouse", 4, 2, 4, None, "the hothouse is filled with freezing ash:: beneath the ash, dead orchids:: hundreds of them:: their stiff grey skeletons petrified with cold"),
    ("cabana", 0, 8, None, 3, "the bed is surrounded by a cloud of ravenous mosquitoes:: you get the impression no-one ever slept here:: on one wall faint letters still almost legible:: on the other wall a mirror"),
    ("plutarco", 7, None, None, None, "this is a room that was never built:: on the floor a mess of architectural drawings depicting one thousand unrealised edifices:: including a plan of the room you are in now:: as you bend to pick it up the floor  gives way beneath you:: & you fall five or four or six stories to the ground below:: trailing toilet paper in your wake"),
    ("tejado", None, None, 3, None, "sunk into the concrete of the roof is an empty bathtub:: it is the eye of the whale:: when you sit down in it you see from the whale’s perspective the glow from the LIGHTED WALKWAY:: the peculiar outlines of the buildings & the dark periphery of the space:: which extends to where the forest re begins"),
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
