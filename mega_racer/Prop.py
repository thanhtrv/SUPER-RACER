from OpenGL.GL import *
import glfw
import numpy as np
import math
from PIL import Image
import imgui

import random
from enum import IntEnum

import lab_utils as lu
from lab_utils import vec3, vec2
from terrain import TerrainInfo
from ObjModel import ObjModel


class PropType(IntEnum):
    NONE = 0
    PALMTREE = 1
    GUMTREE = 2
    BIRCHTREE = 3
    TREEONE = 4
    ROCKONE = 5
    ROCKTWO = 6
    ROCKTHREE = 7
    ROCKFOUR = 8
    ROCKFIVE = 9

class Prop:
    position = vec3(0,0,0) # start at 0,0,0 to make x-axis world rot easier
    facing =  vec3(1,0,0) #world space "heading"
    rotAmount = 0.0 #how much to rotate by
    model = None #model to use
    terrain = None
    propType = 0 # propType will be used for prop specific scaling/etc
    zOffset = 3.0
    def render(self, view, renderingSystem):
        #put switch statement here for each type of prop if ann where appropriate

        modelToWorldTransform = lu.make_mat4_from_zAxis(self.position, self.facing, vec3(0,0,1))
        rotationByRandAmount = lu.make_rotation_z(self.rotAmount)
        renderingSystem.drawObjModel(self.model,rotationByRandAmount * modelToWorldTransform, view)
    def load(self, model, terrain, renderingSytem):
        self.model = model[0]
        self.propType = model[1]
        self.rotAmount = random.uniform(0.001, 6.28319) # ~0 to ~360
        self.terrain = terrain
        #info = self.terrain.getInfoAt(position)
        # need to set position height to terrain height
        # self.position = position
    # def update(self):
    #     info = self.terrain.getInfoAt(self.position)
    #     self.position[2] = lu.mix(self.position[2], info.height + self.zOffset, 0.1);
