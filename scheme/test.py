from scheme import *

expr = read_line("(define-macro (for formal iterable body) (list 'map (list 'lambda (list formal) body) iterable))")
env = create_global_frame()
scheme_eval(expr, env)

a = scheme_eval(read_line("(for i '(1 2 3) (if (= i 1) 0 i))"), env)