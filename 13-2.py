#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 14:38:45 2026

@author: gecpi
"""
class animal:
    pass
class aquatic(animal):
    def move(self,speed):
        print(f"the aquatic animal can swim with {speed} km/h.")
class terrestrial(animal):
    def move(self,speed):
        print(f"the terrestrial animal can swim with {speed} km/h.")
class reptile(aquatic,terrestrial):
    def move(self,speed):
        return super().move(speed)
frog=reptile()
print(f"animal-{reptile.__mro__[0].__name__}")
frog.move(6)