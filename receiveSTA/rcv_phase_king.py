# process local states
local = range(34)
# L states
L = {"x0" : [0, 16], "x1" : [1, 17], "k0" : [22], "k1" : [23], "kb" : [30], "m0" : [4, 5, 20, 21], "m1" : [3, 5, 19, 21]}
# receive variables 
rcv_vars = ["nr0", "nr1", "nrm0", "nrm1", "nrk0", "nrk1"]
# initial states
initial = [0, 1, 16, 17, 26, 27]

# rules
rules = []
rules.append({'idx': 0, 'from': 0, 'to': 2, 'guard': "(and (< nr0 (- n t)) (< nr1 (- n t)))"})
rules.append({'idx': 1, 'from': 0, 'to': 3, 'guard': "(and (< nr0 (- n t)) (>= nr1 (- n t)))"})
rules.append({'idx': 2, 'from': 0, 'to': 4, 'guard': "(and (>= nr0 (- n t)) (< nr1 (- n t)))"})
rules.append({'idx': 3, 'from': 0, 'to': 5, 'guard': "(and (>= nr0 (- n t)) (>= nr1 (- n t)))"})

rules.append({'idx': 4, 'from': 1, 'to': 2, 'guard': "(and (< nr0 (- n t)) (< nr1 (- n t)))"})
rules.append({'idx': 5, 'from': 1, 'to': 3, 'guard': "(and (< nr0 (- n t)) (>= nr1 (- n t)))"})
rules.append({'idx': 6, 'from': 1, 'to': 4, 'guard': "(and (>= nr0 (- n t)) (< nr1 (- n t)))"})
rules.append({'idx': 7, 'from': 1, 'to': 5, 'guard': "(and (>= nr0 (- n t)) (>= nr1 (- n t)))"})

rules.append({'idx': 8, 'from': 2, 'to': 6, 'guard': "(and (<= nrm1 t) (< nrm0 (- n t)))"})
rules.append({'idx': 9, 'from': 2, 'to': 7, 'guard': "(and (<= nrm1 t) (>= nrm0 (- n t)))"})
rules.append({'idx': 10, 'from': 2, 'to': 8, 'guard': "(and (> nrm1 t) (< nrm1 (- n t)))"})
rules.append({'idx': 11, 'from': 2, 'to': 9, 'guard': "(and (> nrm1 t) (>= nrm1 (- n t)))"})

rules.append({'idx': 12, 'from': 3, 'to': 6, 'guard': "(and (<= nrm1 t) (< nrm0 (- n t)))"})
rules.append({'idx': 13, 'from': 3, 'to': 7, 'guard': "(and (<= nrm1 t) (>= nrm0 (- n t)))"})
rules.append({'idx': 14, 'from': 3, 'to': 8, 'guard': "(and (> nrm1 t) (< nrm1 (- n t)))"})
rules.append({'idx': 15, 'from': 3, 'to': 9, 'guard': "(and (> nrm1 t) (>= nrm1 (- n t)))"})

rules.append({'idx': 16, 'from': 4, 'to': 6, 'guard': "(and (<= nrm1 t) (< nrm0 (- n t)))"})
rules.append({'idx': 17, 'from': 4, 'to': 7, 'guard': "(and (<= nrm1 t) (>= nrm0 (- n t)))"})
rules.append({'idx': 18, 'from': 4, 'to': 8, 'guard': "(and (> nrm1 t) (< nrm1 (- n t)))"})
rules.append({'idx': 19, 'from': 4, 'to': 9, 'guard': "(and (> nrm1 t) (>= nrm1 (- n t)))"})

rules.append({'idx': 20, 'from': 5, 'to': 6, 'guard': "(and (<= nrm1 t) (< nrm0 (- n t)))"})
rules.append({'idx': 21, 'from': 5, 'to': 7, 'guard': "(and (<= nrm1 t) (>= nrm0 (- n t)))"})
rules.append({'idx': 22, 'from': 5, 'to': 8, 'guard': "(and (> nrm1 t) (< nrm1 (- n t)))"})
rules.append({'idx': 23, 'from': 5, 'to': 9, 'guard': "(and (> nrm1 t) (>= nrm1 (- n t)))"})

rules.append({'idx': 24, 'from': 6, 'to': 10, 'guard': "(> nrk0 0)"})
rules.append({'idx': 25, 'from': 6, 'to': 11, 'guard': "(> nrk1 0)"})

rules.append({'idx': 26, 'from': 7, 'to': 12, 'guard': "true"})

rules.append({'idx': 27, 'from': 8, 'to': 13, 'guard': "(> nrk0 0)"})
rules.append({'idx': 28, 'from': 8, 'to': 14, 'guard': "(> nrk1 0)"})

rules.append({'idx': 29, 'from': 9, 'to': 15, 'guard': "true"})

# going back to the beginning of the round
rules.append({'idx': 30, 'from': 10, 'to': 0, 'guard': "true"})
rules.append({'idx': 31, 'from': 12, 'to': 0, 'guard': "true"})
rules.append({'idx': 32, 'from': 13, 'to': 0, 'guard': "true"})

rules.append({'idx': 33, 'from': 11, 'to': 1, 'guard': "true"})
rules.append({'idx': 34, 'from': 14, 'to': 1, 'guard': "true"})
rules.append({'idx': 35, 'from': 15, 'to': 1, 'guard': "true"})

rules.append({'idx': 36, 'from': 10, 'to': 16, 'guard': "true"})
rules.append({'idx': 37, 'from': 12, 'to': 16, 'guard': "true"})
rules.append({'idx': 38, 'from': 13, 'to': 16, 'guard': "true"})

rules.append({'idx': 39, 'from': 11, 'to': 17, 'guard': "true"})
rules.append({'idx': 40, 'from': 14, 'to': 17, 'guard': "true"})
rules.append({'idx': 41, 'from': 15, 'to': 17, 'guard': "true"})

# king transitions
rules.append({'idx': 42, 'from': 16, 'to': 18, 'guard': "(and (< nr0 (- n t)) (< nr1 (- n t)))"})
rules.append({'idx': 43, 'from': 16, 'to': 19, 'guard': "(and (< nr0 (- n t)) (>= nr1 (- n t)))"})
rules.append({'idx': 44, 'from': 16, 'to': 20, 'guard': "(and (>= nr0 (- n t)) (< nr1 (- n t)))"})
rules.append({'idx': 45, 'from': 16, 'to': 21, 'guard': "(and (>= nr0 (- n t)) (>= nr1 (- n t)))"})

rules.append({'idx': 46, 'from': 17, 'to': 18, 'guard': "(and (< nr0 (- n t)) (< nr1 (- n t)))"})
rules.append({'idx': 47, 'from': 17, 'to': 19, 'guard': "(and (< nr0 (- n t)) (>= nr1 (- n t)))"})
rules.append({'idx': 48, 'from': 17, 'to': 20, 'guard': "(and (>= nr0 (- n t)) (< nr1 (- n t)))"})
rules.append({'idx': 49, 'from': 17, 'to': 21, 'guard': "(and (>= nr0 (- n t)) (>= nr1 (- n t)))"})

rules.append({'idx': 50, 'from': 18, 'to': 22, 'guard': "(<= nrm1 t)"})
rules.append({'idx': 51, 'from': 18, 'to': 23, 'guard': "(> nrm1 t)"})

rules.append({'idx': 52, 'from': 19, 'to': 22, 'guard': "(<= nrm1 t)"})
rules.append({'idx': 53, 'from': 19, 'to': 23, 'guard': "(> nrm1 t)"})

rules.append({'idx': 54, 'from': 20, 'to': 22, 'guard': "(<= nrm1 t)"})
rules.append({'idx': 55, 'from': 20, 'to': 23, 'guard': "(> nrm1 t)"})

rules.append({'idx': 56, 'from': 21, 'to': 22, 'guard': "(<= nrm1 t)"})
rules.append({'idx': 57, 'from': 21, 'to': 23, 'guard': "(> nrm1 t)"})

rules.append({'idx': 58, 'from': 22, 'to': 24, 'guard': "true"})
rules.append({'idx': 59, 'from': 23, 'to': 25, 'guard': "true"})

# going back to the beginning of the round
rules.append({'idx': 60, 'from': 24, 'to': 0, 'guard': "true"})
rules.append({'idx': 61, 'from': 25, 'to': 1, 'guard': "true"})

# faulty king transitions
rules.append({'idx': 62, 'from': 26, 'to': 28, 'guard': "true"})
rules.append({'idx': 63, 'from': 28, 'to': 30, 'guard': "true"})
rules.append({'idx': 64, 'from': 30, 'to': 32, 'guard': "true"})
rules.append({'idx': 65, 'from': 32, 'to': 26, 'guard': "true"})
rules.append({'idx': 66, 'from': 32, 'to': 27, 'guard': "true"})

rules.append({'idx': 67, 'from': 27, 'to': 29, 'guard': "true"})
rules.append({'idx': 68, 'from': 29, 'to': 31, 'guard': "true"})
rules.append({'idx': 69, 'from': 31, 'to': 33, 'guard': "true"})
rules.append({'idx': 70, 'from': 33, 'to': 26, 'guard': "true"})
rules.append({'idx': 71, 'from': 33, 'to': 27, 'guard': "true"})


# parameters, resilience condition
params = ["n", "t", "f"]
active = "(- n (- f 1))"
rc = ["(> n 0)", "(> t 0)", "(> f 0)", "(>= t f)", "(> n (* 3 t))"]

# faults
faults = "byzantine"
faulty = [26, 27, 28, 29, 30, 31, 32, 33]
max_faulty = "1"


king = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 30, 32]
faulty_king = [26, 28, 30, 32]
phase = 4

# configuration/transition constraints
constraints = []
constraints.append({'type': 'configuration', 'sum': 'eq', 'object': local, 'result': active})
constraints.append({'type': 'configuration', 'sum': 'eq', 'object': faulty, 'result': max_faulty})
constraints.append({'type': 'configuration', 'sum': 'eq', 'object': king, 'result': 1})
constraints.append({'type': 'transition', 'sum': 'eq', 'object': range(len(rules)), 'result': active})
constraints.append({'type': 'round_config', 'sum': 'eq', 'object': faulty_king, 'result': 0})

# receive environment constraints
environment = []
environment.append('(>= nr0 x0)')
environment.append('(<= nr0 (+ x0 f))')
environment.append('(>= nr1 x1)')
environment.append('(<= nr1 (+ x1 f))')

environment.append('(>= nrm0 m0)')
environment.append('(<= nrm0 (+ m0 f))')
environment.append('(>= nrm1 m1)')
environment.append('(<= nrm1 (+ m1 f))')

environment.append('(>= nrk0 k0)')
environment.append('(<= nrk0 (+ k0 kb))')
environment.append('(>= nrk1 k1)')
environment.append('(<= nrk1 (+ k1 kb))')

# properties
properties = []
properties.append({'name':'validity0', 'spec':'safety', 'initial':'(= x0 (- n f))', 'qf':'some', 'reachable':'(not (= x1 0))'})
properties.append({'name':'validity1', 'spec':'safety', 'initial':'(= x1 (- n f))', 'qf':'some', 'reachable':'(not (= x0 0))'})
properties.append({'name':'agreement', 'spec':'safety', 'initial':'true', 'qf':'last', 'reachable':'(and (not (= x0 0)) (not (= x1 0)))'})
