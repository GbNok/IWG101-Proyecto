from random import choice

def generate_problems(total_problems, n):
        if n > len(total_problems):
            n = len(total_problems)
        problems = []
        for q in range(n):
                s = choice(total_problems)
                while s in problems:
                        s = choice(total_problems)
                problems.append(s)
        return problems


#este es un comentario
#hello world