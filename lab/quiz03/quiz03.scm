; Load this file into an interactive session with:
; python3 scheme -load quiz03.scm

; Filter (from lab) takes a predicate procedure f and a list s. It returns a
; new list containing only elements x in s for which (f x) is a true value.
(define (filter f s)
    (cond ((null? s) '())
          ((f (car s)) (cons (car s) (filter f (cdr s))))
          (else (filter f (cdr s))))
)

; All takes a predicate procedure f and a list s. It returns whether (f x) is
; a true value for every element x in s.
(define (all f s)
  (cond 
    ((null? s) True)
    ( (not (f (car s)))   False)
    (else (all f (cdr s)))
    )
)

; Every takes a two-argument predicate g and a list s. It returns a new list
; containing only elements x in s for which (g x y) is true for every y in s.
(define (every g s)
  (define (helper g x y)
    (define (f n)
      (g (car x) n)
      )
    (cond 
      ((null? x) '())
      ((all f y) (cons (car x) (helper g (cdr x) y)))
      (else  (helper g (cdr x) y))
      ) 
      )
  (helper g s s)  
)


; Return a minimum card.
(define (min hand) (car (every <= hand)))

; Fimp returns the card played under the fimping strategy in Cucumber.
(define (fimp hand highest)
  (define (greater x)
    (if (>= x highest)
     True
     False )
    )
  (define lis (filter greater hand))
    (if (null? lis) 
      (min hand)
      (min lis)
)
)

; Legal returns pairs of (card . control) for all legal plays in Cucumber.
(define (legal hand highest)
  (define least (min hand))
  (define (result hand)
    (if (null? hand) nil 
      (begin
        (define card (car hand))
        (cond 
            ((>= card highest) (cons (cons card True) (result (cdr hand))))
            ((= card least)  (cons (cons card False) (result (cdr hand))))
            (else (result (cdr hand)))
        )
        )))
  (result hand))


