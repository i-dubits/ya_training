#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def origin_distance(point):
    return euclidean_distance(point, (0, 0))


def angle_between_points_2(point1, point2):

    angle_1 = math.atan2(point1[1], point1[0])
    angle_2 = math.atan2(point2[1], point2[0])

    
    angle = abs(angle_1 - angle_2)
    #print(f'angle: {angle}')
    return min(angle, 2 * math.pi - angle)

def arc_length(radius, angle):
    return radius * angle

def shortest_path_A_to_B(pointA, pointB):
    distance_OA = origin_distance(pointA)
    distance_OB = origin_distance(pointB)
    
    direct_path = distance_OA + distance_OB
    if distance_OA < 1e-6 or distance_OB < 1e-6:
        return direct_path
    
    if distance_OA > distance_OB:
        radius = distance_OB
        factor = distance_OB / distance_OA
        tangent_point_T = (pointA[0] * factor, pointA[1] * factor)
        
        angle = angle_between_points_2(tangent_point_T, pointB)
        arc_l = arc_length(radius, angle)
    else:
        radius = distance_OA
        factor = distance_OA / distance_OB
        tangent_point_T = (pointB[0] * factor, pointB[1] * factor)
        
        angle = angle_between_points_2(tangent_point_T, pointA)
        arc_l = arc_length(radius, angle)
     
    circle_path = arc_l + abs(distance_OA - distance_OB)
    
    #print(f'direct_path {direct_path}')
    #print(f'arc_l {arc_l}')
    #print(f'distance_OA {distance_OA}')
    #print(f'distance_OB {distance_OB}')
    #print(f'abs(distance_OA - distance_OB) {abs(distance_OA - distance_OB)}')
    #print(f'factor {factor}')
    #print(f'circle_path {circle_path}')
    return min(direct_path, circle_path)

with open('input.txt', 'r') as f:
    x_1, y_1, x_2, y_2 = list(map(int, f.readline().strip().split()))

res = shortest_path_A_to_B((x_1, y_1), (x_2, y_2))
print(res)








