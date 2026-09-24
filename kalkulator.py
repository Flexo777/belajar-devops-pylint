"""Modul kalkulator sederhana untuk demonstrasi Pylint quality gate."""


def hitung_luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang.

    Args:
        panjang: Panjang sisi persegi panjang.
        lebar: Lebar sisi persegi panjang.

    Returns:
        Hasil perkalian panjang dan lebar.

    Raises:
        ValueError: Jika panjang atau lebar bernilai negatif.
    """
    if panjang < 0 or lebar < 0:
        raise ValueError("Panjang dan lebar tidak boleh bernilai negatif.")

    return panjang * lebar


def main() -> None:
    """Fungsi utama program."""
    hasil = hitung_luas_persegi_panjang(5, 3)
    print(f"Luas persegi panjang: {hasil}")


if __name__ == "__main__":
    main()
