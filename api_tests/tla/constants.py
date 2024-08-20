class Body(int):
    """
    Константы для тела запроса.
    """

    REGION = 1
    OFS = 60  # смещение/задержка включения участка (секунды > 0)

    def __str__(self) -> int:
        return self.value
