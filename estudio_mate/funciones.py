from random import choice

def generate_problems(total_problems, n):
        problems = []
        for q in range(n):
                s = choice(total_problems)
                while s in problems:
                        s = choice(total_problems)
                problems.append(s)
        return problems