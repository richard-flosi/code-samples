/*
Provides is_prime(x) and prime_between(x, y).
*/

function is_prime(x) {
    // Returns True if x is prime, otherwise returns False.
    if (x < -1) {
        for (var i=-2; i>x; i--) {
            if (x % i == 0) {
                return false;
            }
        }
    } else if (x == -1 || x == 0 || x == 1) {
        return false;
    } else {
        for (var i=2; i<x; i++) {
            if (x % i == 0) {
                return false;
            }            
        }
    }
    return true;
}

function prime_between(x, y) {
    // Returns all the prime numbers between x and y inclusive.
    var primes = [];
    if (x > y) {
        var orig_x = x;
        x = y;
        y = orig_x;
    }
    for (var i=x; i<=y; i++) {
        if (is_prime(i)) {
            primes.push(i);
        }        
    }
    return primes;
}