from ursina import *
from itertools import product
import time


def parent_kid_inherit(axle, layer):
    for c in cube:
        c.position, c.rotation = round(c.world_position, 1), c.world_rotation
        c.parent = scene

    centrum.rotation = 0

    for c in cube:
        if eval(f'c.position.{axle}') == layer:
            c.parent = centrum


counter = 0
trigger = False
move_history = []
animation_time = 0.15
was_shift_on = []
overwiew = False


def input(key):
    global trigger
    global animation_time
    global move_history
    global counter
    if key == 'p':
        reset_camera()
    if key == 'o':
        replay_moves()
    if key == 'i':
        reverse()
    if trigger:
        return
    if key not in rot_direction:
        return
    if not overwiew:
        trigger = True
        counter = 0
        axle, layer, degree = rot_direction[key]
        parent_kid_inherit(axle, layer)
        shift = held_keys['shift']
        mouse3 = held_keys['right mouse']
        if not mouse3:
            eval(f'centrum.animate_rotation_{axle} ({-degree if shift else degree}, duration = animation_time)')
            move_history.append(key)
            was_shift_on.append(True if shift else False)
        invoke(change_trigger, delay=animation_time + 0.02)


def replay_moves():
    global trigger
    global move_history
    global counter
    global overwiew
    global was_shift_on
    x = len(move_history)
    overwiew = True
    is_overwiew()
    if counter == 0 and move_history:
        reset_cube()
    if move_history and counter < x:
        if trigger:
            return
        trigger = True
        c = move_history[counter]
        s = was_shift_on[counter]
        axle, layer, degree = rot_direction[c]
        parent_kid_inherit(axle, layer)
        if not s:
            eval(f'centrum.animate_rotation_{axle} ({degree}, duration = animation_time)')
        else:
            eval(f'centrum.animate_rotation_{axle} ({-degree}, duration = animation_time)')
        counter += 1
        invoke(change_trigger, delay=animation_time+0.05)
    if counter == x:
        overwiew = False
        is_overwiew()
    if not move_history:
        counter = 0


def is_overwiew():
    global overwiew
    global txt2

    if overwiew:
        txt2.text = "overwiew mode on - cant reverse and add moves"
    else:
        txt2.text = "overwiew mode off"


def reverse():
    global trigger
    global move_history
    global was_shift_on
    global counter
    if not overwiew:
        if move_history:
            if trigger:
                return
            trigger = True
            move_to_reverse = move_history.pop()
            s = was_shift_on.pop()
            axle, layer, degree = rot_direction[move_to_reverse]
            parent_kid_inherit(axle, layer)
            if not s:
                eval(f'centrum.animate_rotation_{axle} ({- degree}, duration = animation_time)')
            else:
                eval(f'centrum.animate_rotation_{axle} ({ degree}, duration = animation_time)')
            invoke(change_trigger, delay=animation_time + 0.05)


def change_trigger():
    global trigger
    trigger = False


def reset_cube():
    global cube
    global move_history
    for ent in cube:
        destroy(ent)
    cube = []
    for pos in product((-1, 0, 1), repeat=3):
        cube.append(Entity(model='Model.obj', texture='ModelKostki.png', position=pos, scale=0.5))
    time.sleep(0.1)


app = Ursina()
window.borderless = False
window.size = (1000, 800)
window.position = (800, 200)
txt = Text(text="Instrukcja obsługi programu:", x=-0.6, y=0.48, scale=0.9, font="font.otf")
txt1 = Text(text="Kostką możesz poruszać za pomocą klawiszy w, s, x, d, f, g, h, b, u.",
            x=-0.6, y=0.44, scale=0.9, font="font.otf")
txt5 = Text(text="Przytrzymaj prawy przycisk myszy, aby obracać kostką.", x=-0.6, y=0.4, scale=0.9, font="font.otf")
txt3 = Text(text="Aby wykonywać ruchy w drugą stronę,"
                 " naciśnij 'shift'+ klawisz ", x=-0.6, y=0.36, scale=0.9, font="font.otf")
txt4 = Text(text="Naciśnij 'i', aby cofnąć ruch."
                 " Naciśnij 'o', aby przeglądać rozgrywkę.", x=-0.6, y=0.32, scale=0.9, font="font.otf")
txt2 = Text(text="overwiew mode off ", x=-0.6, y=0.3, scale=0.9, font="font.otf")

camera = EditorCamera()

start_position = camera.position


def reset_camera():
    camera.position = start_position  # Przywracamy kamerę do początkowej pozycji


centrum = Entity()

rot_direction = {'w': ['y', 1, -90], 's': ['y', 0, -90], 'x': ['y', -1, -90],
                 'd': ['x', -1, -90], 'f': ['x', 0, -90], 'g': ['x', 1, -90],
                 'u': ['z', -1, 90], 'h': ['z', 0, 90], 'b': ['z', 1, 90],
                 }

cube = []
for pos in product((-1, 0, 1), repeat=3):
    cube.append(Entity(model='Model.obj', texture='ModelKostki.png', position=pos, scale=0.5))


app.run()
