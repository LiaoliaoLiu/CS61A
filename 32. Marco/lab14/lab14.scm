(define (split-at lst n)
  (cond 
    ((null? (cdr lst))
     (cons (list (car lst)) nil))
    ((= n 0)
     (cons nil lst))
    (else
     (let ((rest (split-at (cdr lst) (- n 1))))
       (cons (cons (car lst) (car rest)) (cdr rest))))))

(define (compose-all funcs)
  (define (helper x f) (if (null? f) x (helper ((car f) x) (cdr f))))
  (lambda (x) (helper x funcs)))