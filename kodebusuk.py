"""Contoh fungsi penjumlahan sederhana."""


def add_numbers(first_number: int, second_number: int) -> int:
    """Menjumlahkan dua bilangan."""
    return first_number + second_number


def main() -> None:
    """Menjalankan contoh penjumlahan."""
    result = add_numbers(1, 2)
    print(result)


if __name__ == "__main__":
    main()
