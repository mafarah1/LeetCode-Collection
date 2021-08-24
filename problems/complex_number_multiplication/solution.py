class Solution:
    def complexNumberMultiply(self, a, b):

        # Split numbers to real and imagine parts without "i".
        ra, ia = a[:-1].split("+") #Python trick where you can give two variables values using a split stop parameter
        rb, ib = b[:-1].split("+")
        
        # Convert all parts to integer.
        ra, rb = int(ra), int(rb)
        ia, ib = int(ia), int(ib)

        # Return result with formula of multiply for complex numbers.
        return "{}+{}i".format((ra*rb)-(ia*ib),(ra*ib)+(ia*rb)) # Format replaces the "{}" in the string with the desired values