#  -*-coding:utf-8-*-
import math


class Point:
    def __init__(self, X=0, Y=0, Z=0):
        self.x = X
        self.y = Y
        self.z = Z

    def cal_dist(self, obj):
        dx = abs(self.x - obj.x)
        dy = abs(self.y - obj.y)
        dz = abs(self.z - obj.z)
        return math.sqrt(dx*dx + dy*dy + dz*dz)

    def cal_vector(self, obj):
        dx = self.x - obj.x
        dy = self.y - obj.y
        dz = self.z - obj.z
        return Vector(dx, dy, dz)


class Vector:

    def __init__(self, X=0, Y=0, Z=0):
        self.x = X
        self.y = Y
        self.z = Z

    def cross(self,vector_b):
        x1 = self.x
        y1 = self.y
        z1 = self.z
        x2 = vector_b.x
        y2 = vector_b.y
        z2 = vector_b.z
        X = y1 * z2 - y2 * z1
        Y = -(x1 * z2 - x2 * z1)
        Z = x1 * y2 - x2 * y1
        return Vector(X, Y, Z)

    def abs(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def sqr(self):
        return self.x*self.x + self.y*self.y + self.z*self.z


class Line:
    def __init__(self, point_a, point_b):
        self.p = point_a
        self.v = point_b.cal_vector(point_a)

    def get_point(self,delta):
        dx = self.p.x + delta*self.v.x
        dy = self.p.y + delta*self.v.y
        dz = self.p.z + delta*self.v.z
        return Point(dx, dy, dz)



