(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
   (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)


(define (sign x)
  'YOUR-CODE-HERE
  (cond 
    ((< x 0) -1)
    ((zero? x) 0)
    (else 1)
    )
)


(define (square x) (* x x))

(define (pow b n)
  (cond
    ((eq? n 0) 1)
    ((eq? n 1) b)
    ((even? n) (pow (* b b) (quotient n 2)))
    (else (* (pow (* b b) (quotient n 2)) b)
    )
))

(define (ordered? s)
  (cond
    ((null? s))
    ((null? (cdr (cdr s)))
    (if (<= (car s) (car (cdr s))) True
      False)) 
    (else (ordered? (cdr s))
    )
))


(define (nodots s)
  'YOUR-CODE-HERE
  (cond 
        ((null? s) nil)    
        ((and (not (number? (car s))) (not (null? (car s)))  (not (number? (cdr s))) (not (null? (cdr s))))  
         (cons (nodots (car s)) (nodots (cdr s))))
        ( (and (not (number? (car s))) (not (null? (car s))) (number? (cdr s)))  (cons (nodots (car s)) (cons (cdr s) nil)))
        ((and (not (number? (car s))) (not (null? (car s))) (or (number? (cdr s)) (null? (cdr s)))) (cons (nodots (car s)) nil))
        ((and (or (number? (car s)) (null? (car s))) (not (number? (cdr s))) (not (null? (cdr s))) (cons (car s) (nodots (cdr s)))))  
        ((not (and (not (number? (car s))) (not (null? (car s))) (not (number? (cdr s))) (not (null? (cdr s)))))
          (if (null? (cdr s))
                (cons (car s) nil)
                (cons (car s) (cons(cdr s) nil))
            ))
    )
)




; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ((> (car s) v) false)
          ((= (car s) v) true)
          (else (contains? (cdr s) v))
          )
    )

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((< v (car s)) (cons v s))
          ((eq? v (car s)) s)
          (else (cons (car s) (add (cdr s) v)) ; replace this line
          )))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) '())
          ((eq? (car s) (car t)) (cons (car s) (intersect (cdr s)(cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          (else (intersect s (cdr t))))) ; replace this line
; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
          ((eq? (car s) (car t)) (cons (car s)(union (cdr s) (cdr t))))
          (else (cons (car t) (union s (cdr t)))) ; replace this line
          ))

