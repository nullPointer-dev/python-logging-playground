import logging
logger = logging.getLogger(__name__)
ops = {
    1 : "Addition",
    2 : "Subtraction",
    3 : "Multiplication",
    4 : "Division",
}

def add(n1, n2):
    result = n1 + n2
    logger.info(f"Operation = {ops[1]}, Num1 = {n1}, Num2 = {n2}, Result = {result}")
    return result

def sub(n1, n2):
    result = n1 - n2
    logger.info(f"Operation = {ops[2]}, Num1 = {n1}, Num2 = {n2}, Result = {result}")
    return result

def mul(n1, n2):
    result = n1 * n2
    logger.info(f"Operation = {ops[3]}, Num1 = {n1}, Num2 = {n2}, Result = {result}")
    return result

def div(n1, n2):
    try:
        result = n1 / n2
    except ZeroDivisionError:
        logger.error("Division By ZERO")
    else:
        logger.info(f"Operation = {ops[4]}, Num1 = {n1}, Num2 = {n2}, Result = {result}") 
        return result

calcs = {
    1 : add,
    2 : sub,
    3 : mul,
    4 : div,
}      