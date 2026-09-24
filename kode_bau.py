"""Contoh kode Python yang aman dan mengikuti standar Pylint."""


def calculate_result(
    condition_a: bool,
    condition_b: bool,
    condition_c: object,
    values: list[int],
    value_f: int,
    offset: int = 1,
    extra: int = 0,
) -> int | None:
    """Menghitung hasil berdasarkan beberapa kondisi.

    Args:
        condition_a: Kondisi pertama.
        condition_b: Kondisi kedua.
        condition_c: Nilai yang harus bernilai None.
        values: Daftar angka yang menyediakan nilai pertama.
        value_f: Angka tambahan.
        offset: Nilai offset perhitungan.
        extra: Nilai tambahan perhitungan.

    Returns:
        Hasil perhitungan atau None jika kondisi tidak terpenuhi.

    Raises:
        ValueError: Jika daftar values kosong.
    """
    if not condition_a or condition_b or condition_c is not None:
        return None

    if not values:
        raise ValueError("values tidak boleh kosong.")

    # Jangan gunakan eval(). Operasi dilakukan secara langsung dan aman.
    return values[0] + value_f + offset + extra


def main() -> None:
    """Menjalankan contoh penggunaan fungsi."""
    result = calculate_result(
        condition_a=True,
        condition_b=False,
        condition_c=None,
        values=[2],
        value_f=3,
    )

    print(f"Hasil perhitungan: {result}")


if __name__ == "__main__":
    main()