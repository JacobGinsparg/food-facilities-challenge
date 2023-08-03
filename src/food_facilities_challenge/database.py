from pandas import DataFrame, read_csv


class Database:
    _db: DataFrame = None

    def __init__(self) -> None:
        self._db = read_csv("Mobile_Food_Facility_Permit.csv")
