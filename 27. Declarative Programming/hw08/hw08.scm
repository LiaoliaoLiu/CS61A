(define (cadr s) (car (cdr s)))
(define (caddr s) (car (cdr (cdr s))))

(+ 2 4 6 8)
; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (first-operand s) (cadr s))
(define (second-operand s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
; You can access the operands from the expressions with
; first-operand and second-operand
(define (first-operand p) (cadr p))
(define (second-operand p) (caddr p))

(define (derive-sum expr var)
  (define derived (map (lambda (expr) (derive expr var)) (cdr expr)))
  (reduce make-sum derived)
)

(define (derive-product expr var)
  (define (helper f g)
      (define derived_f (derive f var))
      (define derived_g (derive g var))
      (make-sum (make-product derived_f g) (make-product derived_g f)))
  (reduce helper (cdr expr))
)

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  (cond ((= exponent 0) 1)
        ((= exponent 1) base)
        ((and (number? base) (number? exponent)) (expt base exponent))
        (else (list '^ base exponent)))
)

(define (exp? exp)
  (and (list? exp) (eq? (car exp) '^) (null? (cdr (cdr (cdr exp)))) (> (second-operand exp) 0))
)

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

(define (derive-exp exp var)
    (define f (first-operand exp))
    (define g (second-operand exp))
  (make-product g (make-exp f (make-sum g -1)))
)