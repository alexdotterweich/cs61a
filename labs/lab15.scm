;; function tester -- Used in doctests
;; DO NOT EDIT THE FOLLOWING CODE
(define (assert-equal test-num func-name actual-result expected-result)
  (display (string-append "Testing case " (number->string test-num) " for " func-name ": "))
  (if (not (equal? expected-result actual-result))
      (begin
	(display "Failed.") (newline)
	(display "Expected: ")
	(display expected-result)
	(display " Got: ")
	(display actual-result)
	(newline)
	(newline))
      (begin (display "Passed!") (newline))))

(define (reverse lst)
  'YOUR-CODE-HERE)

(define (reverse-iter lst)
  'YOUR-CODE-HERE)

