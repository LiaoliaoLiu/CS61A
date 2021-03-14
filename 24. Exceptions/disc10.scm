;; 5.1 Write a function which takes two lists and concatenates them.
(define (my-append a b) 
    (if (null? a)
        b
        (cons (car a) (my-append (cdr a) b)))
)

;; Write an expression that selects the value 3 from the list below.
(define s '(5 4 (1 2) 3 7))
((lambda (s) ((lambda (f) (f s f)) (lambda (s f) (if (eq? (car s) 3) (car s) (f (cdr s) f))))) s)

;; Write a Scheme function that, when given a list, such as (1 2 3 4)
(define s '(1 2 3 4))
(define (duplicate lst)
        (if (null? lst)
            nil
            (cons (car lst)
                  (cons (car lst) (duplicate (cdr lst)))
            )
        )
)


;; Write a Scheme function that, when given an element, a list, and an index, inserts the element into the list at that index.
(define (insert element lst index)
        (cond ((null? lst) 'index out of range)
              ((= index 0) (cons element lst))
              (else (cons (car lst) (insert element (cdr lst) (- index 1))))
        )
)