Title: Fighting an N-headed monster with recursion
Date: 2012-10-07 3:36
tags: programming, scheme, recursion

A while back, I came upon this problem:

> "You need to kill an N-headed monster. To do that, you have two swords. The first sword(A) cuts `cutA` heads, however, in case the monster doesn't die(ie `no. of heads > 0`), it will grow `growA` heads. The second sword works the same way, except that it'll cut `cutB` heads and in case the monster is still alive, it'll grow `growB` heads. If a sword is used to result in the no. of monster heads being less than 0, you die."

> The problem is to find the shortest combination of swords that can be used to kill the monster(without killing yourself).

This is a paraphrase of the original question(so the question might have sounded a bit awkward). Here's my solution to it, in Scheme(Racket):

    ::Scheme
    (define cutA 7)
    (define growA 3)
    (define cutB 5)
    (define growB 2)

    (define (attack-monster heads)
      (use-sword heads 0 '()))

    (define (use-sword n grow s)
      (cond ((< n 0) '())
        ((= n 0)
         (list s))
        (else
         (append
          (use-sword (- (+ n grow) cutA) growA (append s (list 'a)))
          (use-sword (- (+ n grow) cutB) growB (append s (list 'b)))))))

    (define (shortest-way heads)
      (first (sort (attack-monster heads) (lambda (x y) (< (length x) (length y))))))

Here's how to use it:

    ::Scheme
    > (shortest-way 23)
    '(a a a a a)

Thanks to [skeeto][skeeto] on [Reddit][reddit_disc] for helping me out with this, and more importantly for **not** showing me his code :)

Also, I'd love to see how you guys do this in a more efficient and more elegant ways.

[skeeto]: http://www.reddit.com/user/skeeto
[reddit_disc]: http://www.reddit.com/r/scheme/comments/10zc9x/finding_shortest_link_from_within_a_recursive/
