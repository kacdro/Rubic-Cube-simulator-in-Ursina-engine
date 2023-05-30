from ursina import *
from itertools import product


def parent_kid_inherit(axle, layer):
    for c in cube:
        c.position, c.rotation = round(c.world_position, 1), c.world_rotation
        c.parent = scene

    centrum.rotation = 0

    for c in cube:
        if eval(f'c.position.{axle}') == layer:
            c.parent = centrum


def input(key):
    if key not in rot_direction: return
    axle, layer, degree = rot_direction[key]
    parent_kid_inherit(axle, layer)
    shift = held_keys['shift']
    eval(f'centrum.animate_rotation_{axle} ({-degree if shift else degree}, duration = 0.2)')


app = Ursina()
window.borderless = False
window.size = (1000, 800)
window.position = (800, 200)


EditorCamera()

centrum = Entity()

rot_direction = {'q': ['y', 1, -90], 'w': ['y', 0, -90], 'e': ['y', -1, -90],
            'a': ['x', -1, -90], 's': ['x', 0, -90], 'd': ['x', 1, -90],
            'z': ['z', -1, 90], 'x': ['z', 0, 90], 'c': ['z', 1, 90]}

cube = []
for pos in product((-1, 0, 1), repeat=3):
    cube.append(Entity(model='Model.obj', texture='ModelKostki.png', position=pos, scale=0.5))


app.run()