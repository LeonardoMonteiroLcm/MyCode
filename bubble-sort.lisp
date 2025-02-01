;;Bubble Sort in Lisp

(defun bubble-sort (lst)
  "Ordena uma lista de números usando o algoritmo Bubble Sort."
  (let ((swapped t))
    (loop while swapped do
      (setf swapped nil)
      (setf lst (loop for (a b . rest) on lst
                      when (and b (> a b))
                        do (setf swapped t)
                           (return (cons b (cons a rest)))
                      collect a into new-list
                      finally (return (append new-list (list b))))))
    lst))

;; Exemplo de uso:
(print (bubble-sort '(5 3 8 4 2)))

;; Saída esperada: (2 3 4 5 8)
