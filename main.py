def calculate(a: int, b: int) -> int:
    result = a * b
    return result


def main() -> None:
    x = 10
    y = 20

    result = calculate(x, y)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
