from MultiColorComponent import MultiColorComponent
from MyModelFinger import MyModelFinger
from Point import Point
from Shapes import Cube, Sphere
import ColorType as Ct


# defined macros for dimension
uAxis = 0
vAxis = 1
wAxis = 2


class MyModelHand(MultiColorComponent):
    """
    Hand part
    - [ ] Palm

    """

    def __init__(self, parent, position, shaderProg, display_obj=None,
                 scale: float = 1.0, left_handed: bool = True):
        super().__init__(position, display_obj)
        self.contextParent = parent

        joint_color = Ct.ColorType(0.4, 0.4, 0.4)
        color_medium_gray = Ct.ColorType(80 / 255, 62 / 255, 89 / 255)

        joint_radius = 0.12 * scale
        joint_length = joint_radius * 2
        joint_part = Sphere(Point((0, 0, 0)), shaderProg, [0.1, 0.1, 0.1], joint_color)
        self.addChild(joint_part)
        self.componentList.append(joint_part)
        self.componentDict['joint'] = joint_part
        self.joint = joint_part

        palm_length = 1 * scale
        palm_width = 1 * scale
        palm_thickness = 2.2 * joint_radius
        palm_part = Cube(Point((
            0, 0, joint_length)), shaderProg, [
            palm_length, palm_thickness, palm_width], color_medium_gray)

        joint_part.addChild(palm_part)
        self.componentList.append(palm_part)
        self.componentDict['palm'] = palm_part
        self.palm = palm_part

        finger_radius = palm_thickness / 2
        finger_length = 1.5 * palm_thickness

        joint_part.setRotateExtent(joint_part.uAxis, -45, 15)
        palm_part.setRotateExtent(joint_part.uAxis, -45, 15)
        palm_part.setRotateExtent(joint_part.wAxis, 0, 0)

        if not left_handed:
            joint_part.setRotateExtent(joint_part.vAxis, -5, 15)
            joint_part.setRotateExtent(joint_part.wAxis, -90, 45)

            palm_part.setRotateExtent(joint_part.vAxis, -5, 15)

            thumb_finger_part = MyModelFinger(self.contextParent, Point((
                -palm_length / 2, 0, palm_length / 4)), shaderProg,
                                              finger_radius=finger_radius, finger_height=finger_length, finger_nums=2)
            thumb_finger_part.setDefaultAngle(-45, thumb_finger_part.vAxis)
            palm_part.addChild(thumb_finger_part)
            self.componentList.extend(thumb_finger_part.componentList)
            for k, v in thumb_finger_part.componentDict.items():
                self.componentDict[f'thumb_{k}'] = v

            index_finger_part = MyModelFinger(self.contextParent, Point((
                -palm_length / 2 + finger_radius, 0, palm_length / 2)), shaderProg,
                                         finger_radius=finger_radius, finger_height=0.9 * finger_length, finger_nums=3)
            palm_part.addChild(index_finger_part)
            self.componentList.extend(index_finger_part.componentList)
            for k, v in index_finger_part.componentDict.items():
                self.componentDict[f'index_{k}'] = v

            middle_finger_part = MyModelFinger(self.contextParent, Point((
                finger_radius / 3 - palm_length / 6, 0, palm_length / 2)), shaderProg,
                                          finger_radius=finger_radius, finger_height=finger_length, finger_nums=3)
            palm_part.addChild(middle_finger_part)
            self.componentList.extend(middle_finger_part.componentList)
            for k, v in middle_finger_part.componentDict.items():
                self.componentDict[f'middle_{k}'] = v

            ring_finger_part = MyModelFinger(self.contextParent, Point((
                palm_length / 6 - finger_radius / 3, 0, palm_length / 2)), shaderProg,
                                        finger_radius=finger_radius, finger_height=0.9 * finger_length, finger_nums=3)
            palm_part.addChild(ring_finger_part)
            self.componentList.extend(ring_finger_part.componentList)
            for k, v in ring_finger_part.componentDict.items():
                self.componentDict[f'ring_{k}'] = v

            little_finger_part = MyModelFinger(self.contextParent, Point((
                palm_length / 2 - finger_radius, 0, palm_length / 2)), shaderProg,
                                          finger_radius=finger_radius, finger_height=0.8 * finger_length, finger_nums=3)
            palm_part.addChild(little_finger_part)
            self.componentList.extend(little_finger_part.componentList)
            for k, v in little_finger_part.componentDict.items():
                self.componentDict[f'little_{k}'] = v

            # thumb finger rotation limit
            thumb_finger_part.setPartRotateExtent(0, 0, -90, 0)
            thumb_finger_part.setPartRotateExtent(0, vAxis, -30, 30)
            thumb_finger_part.setPartRotateExtent(0, wAxis, 0, 0)

            thumb_finger_part.setPartRotateExtent(1, 0, 0, 0)
            thumb_finger_part.setPartRotateExtent(1, vAxis, 0, 90)
            thumb_finger_part.setPartRotateExtent(1, wAxis, 0, 0)

        # left handed
        else:
            joint_part.setRotateExtent(joint_part.vAxis, -15, 5)
            joint_part.setRotateExtent(joint_part.wAxis, -45, 90)

            palm_part.setRotateExtent(joint_part.vAxis, -15, 5)

            thumb_finger_part = MyModelFinger(self.contextParent, Point((
                palm_length / 2, 0, palm_length / 4)), shaderProg,
                                              finger_radius=finger_radius, finger_height=finger_length, finger_nums=2)
            thumb_finger_part.setDefaultAngle(45, thumb_finger_part.vAxis)
            palm_part.addChild(thumb_finger_part)
            self.componentList.extend(thumb_finger_part.componentList)
            for k, v in thumb_finger_part.componentDict.items():
                self.componentDict[f'thumb_{k}'] = v

            index_finger_part = MyModelFinger(self.contextParent, Point((
                palm_length / 2 - finger_radius, 0, palm_length / 2)), shaderProg,
                                              finger_radius=finger_radius, finger_height=0.9 * finger_length, finger_nums=3)
            palm_part.addChild(index_finger_part)
            self.componentList.extend(index_finger_part.componentList)
            for k, v in index_finger_part.componentDict.items():
                self.componentDict[f'index_{k}'] = v

            middle_finger_part = MyModelFinger(self.contextParent, Point((
                palm_length / 6 - finger_radius / 3, 0, palm_length / 2)), shaderProg,
                                          finger_radius=finger_radius, finger_height=finger_length, finger_nums=3)
            palm_part.addChild(middle_finger_part)
            self.componentList.extend(middle_finger_part.componentList)
            for k, v in middle_finger_part.componentDict.items():
                self.componentDict[f'middle_{k}'] = v

            ring_finger_part = MyModelFinger(self.contextParent, Point((
                finger_radius / 3 - palm_length / 6, 0, palm_length / 2)), shaderProg,
                                        finger_radius=finger_radius, finger_height=0.9 * finger_length, finger_nums=3)
            palm_part.addChild(ring_finger_part)
            self.componentList.extend(ring_finger_part.componentList)
            for k, v in ring_finger_part.componentDict.items():
                self.componentDict[f'ring_{k}'] = v

            little_finger_part = MyModelFinger(self.contextParent, Point((
                -palm_length / 2 + finger_radius, 0, palm_length / 2)), shaderProg,
                                          finger_radius=finger_radius, finger_height=0.8 * finger_length, finger_nums=3)
            palm_part.addChild(little_finger_part)
            self.componentList.extend(little_finger_part.componentList)
            for k, v in little_finger_part.componentDict.items():
                self.componentDict[f'little_{k}'] = v

            # thumb finger rotation limit
            thumb_finger_part.setPartRotateExtent(0, uAxis, -90, 0)
            thumb_finger_part.setPartRotateExtent(0, vAxis, -30, 30)
            thumb_finger_part.setPartRotateExtent(0, wAxis, 0, 0)

            thumb_finger_part.setPartRotateExtent(1, uAxis, 0, 0)
            thumb_finger_part.setPartRotateExtent(1, vAxis, -90, 0)
            thumb_finger_part.setPartRotateExtent(1, wAxis, 0, 0)

        self.thumb_finger = thumb_finger_part
        self.Index_finger = index_finger_part
        self.middle_finger = middle_finger_part
        self.ring_finger = ring_finger_part
        self.little_finger = little_finger_part

        # index finger rotation limit
        index_finger_part.setPartRotateExtent(0, uAxis, -90, 0)
        index_finger_part.setPartRotateExtent(0, vAxis, -5, 5)
        index_finger_part.setPartRotateExtent(0, wAxis, 0, 0)

        index_finger_part.setPartRotateExtent(1, uAxis, -90, 0)
        index_finger_part.setPartRotateExtent(1, vAxis, 0, 0)
        index_finger_part.setPartRotateExtent(1, wAxis, 0, 0)

        index_finger_part.setPartRotateExtent(2, uAxis, -90, 0)
        index_finger_part.setPartRotateExtent(2, vAxis, 0, 0)
        index_finger_part.setPartRotateExtent(2, wAxis, 0, 0)

        # middle finger rotation limit
        middle_finger_part.setPartRotateExtent(0, uAxis, -90, 0)
        middle_finger_part.setPartRotateExtent(0, vAxis, -5, 5)
        middle_finger_part.setPartRotateExtent(0, wAxis, 0, 0)

        middle_finger_part.setPartRotateExtent(1, uAxis, -90, 0)
        middle_finger_part.setPartRotateExtent(1, vAxis, 0, 0)
        middle_finger_part.setPartRotateExtent(1, wAxis, 0, 0)

        middle_finger_part.setPartRotateExtent(2, uAxis, -90, 0)
        middle_finger_part.setPartRotateExtent(2, vAxis, 0, 0)
        middle_finger_part.setPartRotateExtent(2, wAxis, 0, 0)

        # ring finger rotation limit
        ring_finger_part.setPartRotateExtent(0, uAxis, -90, 0)
        ring_finger_part.setPartRotateExtent(0, vAxis, -5, 5)
        ring_finger_part.setPartRotateExtent(0, wAxis, 0, 0)

        ring_finger_part.setPartRotateExtent(1, uAxis, -90, 0)
        ring_finger_part.setPartRotateExtent(1, vAxis, 0, 0)
        ring_finger_part.setPartRotateExtent(1, wAxis, 0, 0)

        ring_finger_part.setPartRotateExtent(2, uAxis, -90, 0)
        ring_finger_part.setPartRotateExtent(2, vAxis, 0, 0)
        ring_finger_part.setPartRotateExtent(2, wAxis, 0, 0)

        # little finger rotation limit
        little_finger_part.setPartRotateExtent(0, uAxis, -90, 0)
        little_finger_part.setPartRotateExtent(0, vAxis, -5, 5)
        little_finger_part.setPartRotateExtent(0, wAxis, 0, 0)

        little_finger_part.setPartRotateExtent(1, uAxis, -90, 0)
        little_finger_part.setPartRotateExtent(1, vAxis, 0, 0)
        little_finger_part.setPartRotateExtent(1, wAxis, 0, 0)

        little_finger_part.setPartRotateExtent(2, uAxis, -90, 0)
        little_finger_part.setPartRotateExtent(2, vAxis, 0, 0)
        little_finger_part.setPartRotateExtent(2, wAxis, 0, 0)
