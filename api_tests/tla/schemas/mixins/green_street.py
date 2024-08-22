class GuidExtractionMixin:
    """Миксин для извлечения GUID из различных объектов."""

    def get_guids(self) -> list[str]:
        """
        Возвращает список GUID из всех объектов
        GreenPartResponse.

        Returns:
            List[str]: Список GUID.
        """
        return [part.guid for part in self.info]

    def get_guids_from_parts(self) -> list[str]:
        """
        Возвращает список GUID из всех участков.

        Returns:
            List[str]: Список GUID.
        """
        return [part.guid for part in self.info[0].green_part]

    def get_guids_from_routes(self) -> list[str]:
        """
        Возвращает список GUID из маршрутов.

        Returns:
            List[str]: Список GUID.
        """
        return [part.guid for part in self.info[0].green_route]
