from Component import Component
from MyModelHead import MyModelHead
from Point import Point
from Shapes import Cube
import ColorType as Ct


class MyModelBody(Component):
    """
    Body Part
    - [x] Main Body
    - [ ] Connect the head
    - [x] Jetpack
    - [ ] Saber Slot
    - [ ] Sabers
    - [ ] Shoulder Part

    """

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale=1.0):
        super().__init__(position, display_obj)
        self.componentList = []
        self.componentDict = {}
        self.contextParent = parent

        # define body
        body1_length = scale * 0.8
        body1_thickness = scale * 0.6
        body1_height = scale * 0.9
        body_part_1 = Cube(Point((0, 0, 0)), shaderProg,
                           [body1_length, body1_thickness, body1_height],
                           Ct.RED)
        self.addChild(body_part_1)

        body2_length = body1_length * 1.2
        body2_thickness = body1_thickness * 1.2
        body2_height = body1_height * 0.6
        body_part_2 = Cube(Point((0, 0, body1_height / 2 - body2_height / 3)), shaderProg,
                           [body2_length, body2_thickness, body2_height],
                           Ct.BLUE)
        self.addChild(body_part_2)

        neck_platform_length = body2_length * 0.4
        neck_platform_thickness = body2_thickness * 1.1
        neck_platform_height = body2_length * 0.1
        neck_platform = Cube(Point((0, 0, body2_height / 2 - neck_platform_height * 0.48)), shaderProg,
                             [neck_platform_length, neck_platform_thickness, neck_platform_height],
                             Ct.ColorType(217 / 255, 166 / 255, 82 / 255))
        body_part_2.addChild(neck_platform)

        # Connect the neck
        head_neck_part = MyModelHead(self,
                                     Point((0, 0, neck_platform_height * 0.95)),
                                     shaderProg, scale=scale * 0.5)
        neck_platform.addChild(head_neck_part)
        self.componentList.extend(head_neck_part.componentList)
        for key, value in head_neck_part.componentDict.items():
            self.componentDict[f'head_{key}'] = value

        # Jetpack
        jetpack_length = body1_length * 0.9
        jetpack_thickness = body2_thickness * 0.4
        jetpack_height = body1_height * 0.8
        jetpack = Cube(Point((0, body1_thickness / 2 + jetpack_thickness / 2,
                              body1_height / 2 - jetpack_height * 0.48)), shaderProg,
                       [jetpack_length, jetpack_thickness, jetpack_height],
                       Ct.ColorType(80 / 255, 62 / 255, 89 / 255))
        body_part_1.addChild(jetpack)
