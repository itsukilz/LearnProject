;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname I-3-2) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp") (lib "universe.rkt" "teachpack" "2htdp") (lib "batch-io.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp") (lib "universe.rkt" "teachpack" "2htdp") (lib "batch-io.rkt" "teachpack" "2htdp")) #f)))
;e34
;String -> 1String
;extracts the first character from a non-empty string
;given: "hello" back: "h"
;given: "test me once more" back:"t"
(define (string-first s)
  (string-ith s 0))

;e35
;String -> 1String
;extracts the last character from a non-empty string
;given:"hello" back:"o"
;given:"test me once more" back:"e"
(define (string-last s)
  (string-ith s (- (string-length s) 1)))

;e36
;Image -> Number
;compute the number of pixels of the given image
;given: (circle 9 "solid" "red") back: 324
;given: (rectangle 3 4 "outline" "blue")  back: 12
(define (area-of-image image)
  (* (image-width image) (image-height image)))

;e37
;String -> String
;move the first character and return the rest of string
;given: "hello" back:"ello"
;given: "test me once more" back:"est me once more"
(define (string-rest s)
  (substring s 1 (string-length s) ))

;e38
;String -> String
;move the last character and return the rest of string
;given: "hello" back:"hell"
;given: "test me once more" back:"test me once mor"
(define (string-remove-last s)
  (substring s 0 (- (string-length s) 1)))