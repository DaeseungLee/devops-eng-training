# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 테스트 케이스 작성
import sys, os
from functions import plus, sub, multiplication, divide
import pytest


def test_plus():
    assert plus(3,4) == 7
    assert plus(132,145) == 277

def test_sub():
    assert sub(3,4) == -1
    assert sub(120, 120) == 0

def test_multiplication():
    assert multiplication(3,4) == 12
    assert multiplication(-4, -5) == 20

def test_divide():
    assert divide(3, 4) == 0.75
    assert divide(1, 3) == 0.33
    assert divide(4, 0) == None
