#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11-03-2023 07:16 pm
# @Author  : bhaskar.uprety
# @File    : utils.py

"""utils.py File created on 11-03-2023"""
import random


def generate_random_number(length) -> int:
    """Generates a random number of the given lengths"""
    return random.randint(10 ** (length - 1), 10 ** length - 1)
