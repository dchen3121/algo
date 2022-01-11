# QUESTION:
# Given an array of people's height comparisons, give 'yes' 'no' or 'unknown' to compare two people's heights

from typing import List

class Solution:
    def taller(height_comparisons, person1, person2):
        di = {}
        for p_taller, p_shorter in height_comparisons:
            if p_taller in di: