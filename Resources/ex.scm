(define (sum-while initial-x condition add-to-total  update-x)
    `(begin
        (define (f x total)
            (if ,condition
                (f ,update-x (+ total ,add-to-total))
                total))
        (f ,initial-x 0)))
(begin
    (define (f x total)
        (if (< x 10)
            (f (+ x 2) (+ total (* x x)))
            total))
    (f 1 0))