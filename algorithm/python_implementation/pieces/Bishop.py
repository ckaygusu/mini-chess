def bishop_ray1():
    for i in range(1, 6):
        yield i, i

def bishop_ray2():
    for i in range(1, 6):
        yield -i, i

def bishop_ray3():
    for i in range(1, 6):
        yield i, -i
        
def bishop_ray4():
    for i in range(1, 6):
        yield -i, -i
        
rays = [bishop_ray1, bishop_ray2, bishop_ray3, bishop_ray4]