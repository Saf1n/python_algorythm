__author__ = 'Сафин Ильшат'

# coding: utf-8

# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

# Ссылка для блок-схем:
# https://drive.google.com/file/d/1HdOXn5QLdtpqXqcnslDd7CYutivQozwz/view?usp=sharing

while True:
    print('Пожалуйста, введите знак операции и два числа')
    znak = input('Введите знак операции (0, +, -, *, /): ')
    if znak == '0':
        break
    if znak in ('+','-','*','/'):
        x = int(input('Введите первое число: '))
        y = int(input('Введите второе число: '))
        if znak == '+':
            print('Операция сложения:', x + y)
        elif znak == '-':
            print('Операция вычитания:', x - y)
        elif znak == '*':
            print('Операция умножения:', x * y)
        elif znak == '/':
            if y != 0:
                print('Операция деления:', x / y)
            else:
                print('Делить на ноль нельзя!')
        else:           
            print('Неверный знак операции!')
