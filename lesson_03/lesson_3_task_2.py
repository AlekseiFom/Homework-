from smartphone import Smartphone

catalog = [
    Smartphone(
        "iphone",
        "17",
        "+79123456789"
    ),
    Smartphone(
        "Samsung",
        "A15",
        "+79234567899"
    ),
    Smartphone(
        "Redmi",
        "11Light",
        "+79876543211"
    ),
    Smartphone(
        "Xaomi",
        "Note 05",
        "-79856942255"
    ),
    Smartphone(
        "Nokia",
        "3210",
        "+79224790827"
    )
]

for item in catalog:
    print(f"{item.mark} - {item.model}. {item.phone}")
