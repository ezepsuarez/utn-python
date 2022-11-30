import bpy
import random

def CrearMaterial(nombre, diffuse, specular):
    mat = bpy.data.materials.new(nombre)
    
 
    mat.use_nodes = True
    mat_nodes = mat.node_tree.nodes["Principled BSDF"]

    mat_nodes.inputs[0].default_value = diffuse

    return mat

def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)

def run(origin):
    rojo = random.randint(0,1)
    verde = random.randint(0,1)
    azul = random.randint(0,1)
    matcolor = CrearMaterial('Red', (rojo,verde,azul,1), (1,1,1))


    bpy.ops.mesh.primitive_cube_add(location=origin)
    setMaterial(bpy.context.object, matcolor)


if __name__ == "__main__":
    for i in range(0,4):
        for j in range(0,4):
            run((i*2,0,j*2))