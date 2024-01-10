#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        best_student = None
        for key, value in a_dictionary.items():
            if value is not None:
                best_student = max(a_dictionary, key=a_dictionary.get)
        return best_student
