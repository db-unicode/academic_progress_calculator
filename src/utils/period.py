class Period:
    @staticmethod
    def get_year(period: str) -> int:
        """
        Extracts the year from the period string in YYYYXZ format.
        
        :param period: A string representing the period (e.g., "202120").
        :return: An integer representing the year.
        """
        return int(period[:4])

    @staticmethod
    def get_semester(period: str) -> int:
        """
        Extracts the semester from the period string in YYYYXZ format.
        
        :param period: A single digit in period string representing the semester (1 or 2).
        :return: An integer representing the semester.
        """
        return int(period[4])

    @staticmethod
    def is_before_period(record_period: str, limit_period: str) -> bool:
        """
        Determines if a period is before a given limit period.
        
        :param record_period: The period to check (e.g., "202120").
        :param limit_period: The exclusive upper limit period (e.g., "202220").
        :return: True if record_period is before limit_period, otherwise False.
        """
        record_year = Period.get_year(record_period)
        record_semester = Period.get_semester(record_period)
        limit_year = Period.get_year(limit_period)
        limit_semester = Period.get_semester(limit_period)
        
        return record_year < limit_year or (record_year == limit_year and record_semester < limit_semester)
