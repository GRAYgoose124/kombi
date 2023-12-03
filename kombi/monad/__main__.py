from . import get_line, to_uppercase

if __name__ == "__main__":
    composed_action = get_line >> to_uppercase
    final_result = composed_action()

    print("Transformed input:", final_result)
