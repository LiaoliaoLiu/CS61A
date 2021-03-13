(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)


(define (sign num)
  (cond ((= num 0) 0)
        ((< num 0) -1)
        (else +1))
)


(define (square x) (* x x))

(define (pow x y)
  (if (= y 0)
      1
      (if (= (remainder y 2) 1)
          (* x (pow x (- y 1)))
          (square (pow x (/ y 2))))
      )
)

