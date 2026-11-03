world = [[], []]

def add_object(o, depth=0):
    world[depth].append(o)

def remove_object(o, depth=0):
    world[depth].remove(o)


def update():
    for layer in world:
        for o in layer:
            o.update()
def render():
    for layer in world:
        for o in layer:
            o.draw()
