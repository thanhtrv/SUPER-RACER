from OpenGL.GL import *
import glfw
import numpy as np
import math
from PIL import Image
import imgui

import lab_utils as lu
from lab_utils import vec3, vec2
from terrain import TerrainInfo
from ObjModel import ObjModel

class Prop:
    position = vec3(0,0,0)
    velocity = vec3(0,0,0)
    heading = vec3(1,0,0)
    speed = 0.0

    maxSpeedRoad = 50.0
    maxSpeedRough = 15.0
    zOffset = 3.0
    angvel = 2.0

    terrain = None
    model = None

    def render(self, view, renderingSystem):
        # TODO 1.3: This is a good place to draw the racer model instead of the sphere
        modelToWorldTransform = lu.make_mat4_from_zAxis(self.position, self.heading, vec3(0,0,1))
        renderingSystem.drawObjModel(self.model, modelToWorldTransform, view)
        #lu.drawSphere(self.position, 1.5, [1,0,0,1], view)

    def load(self, objModelName, terrain, renderingSystem):
        self.terrain = terrain
        self.position = terrain.startLocations[0]
        # TODO 1.3: This is a good place create and load the racer model
        self.model = ObjModel(objModelName)