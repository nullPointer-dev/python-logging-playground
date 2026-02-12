from logger_config import setup_logging
import logging
import uuid
from operations import calcs, ops

SESSION_ID = uuid.uuid4().hex[:6]
setup_logging(SESSION_ID)
logger = logging.getLogger(__name__)
print("\n-----Welcome to CLI-Based-Calculator-----")
logger.debug("Session Started")
while(True):
    print("Please Select Operation Number (1-5):")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    user_input = input()
    logger.debug(f"User Entered {user_input}")
    try:
        op = int(user_input)
        if(op > 5 or op < 1):
            logger.warning("Invalid Input Operation")
            continue
    except ValueError:
        logger.warning("Invalid Input")
        continue   
    if op == 5:
        logger.info(f"Exited Calculator")
        print("Thanks for Using")
        break
    n1 = input("Enter 1st Number: ")
    n2 = input("Enter 2nd Number: ")
    logger.debug(f"Num1 Enterred: {n1}")
    logger.debug(f"Num2 Enterred: {n2}")
    try:
        num1 = float(n1)
        num2 = float(n2)
        logger.debug(f"Parsed numbers: {num1}, {num2}")
    except ValueError:
        logger.warning("Invalid Numbers Enterred")
        continue
    else:
        logger.debug(f"Performing {ops[op]}")
        result = calcs[op](num1,num2)
    print("\n")
logger.debug("Session Ended")

