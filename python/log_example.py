import logging
import random

logging.basicConfig(filename='app.log', filemode='a')
log = logging.getLogger()
log.setLevel(logging.DEBUG)

log.debug("Output: ")
log.info("Starting program.")
log.warn("Something doesn't look right.")
log.error("Something went wrong.")

def get_guess():
    guess = input("Enter guess. ")
    log.info("Getting user's guess.")
    log.debug(f"Guess: {guess}")
    return guess


def get_secret():
    secret = random.randint(1, 101)
    log.info("Getting random secret.")
    log.debug(f"Secret: {secret}")
    return secret


def run_game(secret):
    log.info("Running game")
    while 1:
        try:
            guess = get_guess()

            if int(guess) < secret:
                print("Too low!")
            elif int(guess) > secret:
                print("Too high!")
            elif int(guess) == secret:
                print("You got it!")
                break
            else:
                log.warn("Impossible action. Something went wrong.")
        except Exception as e:
            log.error("Something went wrong.")
            log.error(e)
            raise e



def main():
    log.info("Running the main stuff")
    print("Welcome to higher or lower!")
    secret = get_secret()
    run_game(secret)
    print("Game over.")
    log.info("Exiting program.")


if __name__ == "__main__":
    main()
