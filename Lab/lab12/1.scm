(define-macro (trace expr)
  (define operator (car expr))
`(begin
    (define original ,operator)
    (define ,operator (lambda (n)
                         (print (list (quote ,operator) n))
                         (original n)))
    (define result ,expr)
    (define ,operator original)
    result))

(define fact (lambda (n)
  (if (zero? n) 1 (* n (fact (- n 1))))))

(fact 5)
(trace (fact 5))
