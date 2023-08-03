import json
from typing import Dict

from pandas import DataFrame, read_csv


class Database:
    _db: DataFrame = None

    def __init__(self) -> None:
        self._db = read_csv("Mobile_Food_Facility_Permit.csv")

    # Internal query helpers

    def _query(self, field_name: str, value):
        return json.loads(self._db.query(f"{field_name} == '{value}'").to_json(orient="records"))

    def _query_multi(self, query_params: Dict[str, str]):
        query_string = " & ".join([f"{field} == '{value}'" for field, value in query_params.items()])
        return json.loads(self._db.query(query_string).to_json(orient="records"))

    def _query_partial_str(self, field_name: str, value):
        return json.loads(
            self._db.query(
                f"{field_name}.str.contains('{value}', regex=False)",
                engine="python",
            ).to_json(orient="records")
        )

    # External query methods

    def query_applicant(self, applicant: str, status: str = None):
        if status:
            return self._query_multi(
                {
                    "Applicant": applicant,
                    "Status": status,
                }
            )
        else:
            return self._query(field_name="Applicant", value=applicant)

    def query_street(self, street: str):
        return self._query_partial_str(field_name="Address", value=street)

    def query_near(self, lat: float, long: float, allow_non_approved: bool):
        if allow_non_approved:
            pass
        else:
            pass


# Initialize db object
database = Database()
