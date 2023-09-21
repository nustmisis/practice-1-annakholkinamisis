# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""
weight = float(input("Input your weight: "))
height = float(input("Input your height: "))


def compute_bmi(weight: float, height: float):
    return (weight / height) ** 2


print(compute_bmi(weight, height))
