

def safe_divide(numerator, denominator):
    """Performs safe division with error handling."""
    try:
        
        num = float(numerator)
        den = float(denominator)

        
        result = num / den
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
