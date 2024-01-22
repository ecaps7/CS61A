;;; Non-empty subsets of integer list s that have an even sum
;;;
;;; scm> (even-subsets '(3 4 5 7))
;;; ((5 7) (4 5 7) (4) (3 7) (3 5) (3 4 7) (3 4 5))
; (define (even-subsets s)
;     (if (null? s) nil
;         (append (even-subsets (cdr s))
;                 (subset-helper even? s))))
;;; Non-empty subsets of integer list s that have an odd sum        
; (define (odd-subsets s)
;     (if (null? s) nil
;         (append (odd-subsets (cdr s))
;                 (subset-helper odd? s))))

; (define (subset-helper f s)
;     (append
;         (map (lambda (t) (cons (car s) t))
;              (if (f (car s))
;                  (even-subsets (cdr s))
;                  (odd-subsets (cdr s))))
;         (if (f (car s)) (list (list (car s))) nil)))

;;; an alternative solution
;;;
;;; Non-empty subsets of s
(define (nonempty-subsets s)
    (if (null? s)
        nil
        (let ((rest (nonempty-subsets (cdr s))))
             (append rest
                     (map (lambda (t) (cons (car s) t)) rest)
                     (list (list (car s)))))))
;;; Non-empty subsets of integer list s that have an even sum
(define (even-subsets s)
    (filter (lambda (s) (even? (apply + s)))(nonempty-subsets s)))