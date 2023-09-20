"""
Билдер наиболее приятно реализуется через цепочку вызовов, когда сложная json`ка строится
ProductBuilder(). - тут инициализируется базовые поля запроса из полей-значений по-умолчанию у датаклассов
.category(name="Phone") - тут можем поправить одно из полей, если отличается от умолчания
.description(link="https://qwe.ru") - тут можем добавить дополнительные секции в json не из списка дефолтных

И шагом теста будет выглядеть ProductBuilder().category(name="Phone").description(link="https://qwe.ru")
"""
import dataclasses
from typing import Self

from data.schemas.phases_schemas import PhaseRequestSchema
from .authorize_request import AuthorizeRequest
from .phase_request import PhaseRequest
from data.schemas.authorize_schema import AuthorizeRequestSchema


class AuthorizeBuilder:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._prepared_request = AuthorizeRequest()

    @property
    def prepared_request(self):
        prepared_request = self._prepared_request
        self.reset()
        return prepared_request

    def login(self, **kwargs) -> Self:
        self._prepared_request.add({"login": AuthorizeRequestSchema(**kwargs).login})
        return self

    def password(self, **kwargs) -> Self:
        self._prepared_request.add({"password": AuthorizeRequestSchema(**kwargs).password})
        return self

    def additional(self, **kwargs) -> Self:
        self._prepared_request.add(dataclasses.asdict(AuthorizeRequestSchema(**kwargs)))
        return self


class PhaseBuilder:
    def __init__(self, token) -> None:
        self._token = token
        self.reset()

    def reset(self) -> None:
        self._prepared_request = PhaseRequest(self._token)

    @property
    def prepared_request(self):
        prepared_request = self._prepared_request
        self.reset()
        return prepared_request

    def add_phase(self, **kwargs) -> Self:
        self._prepared_request.add({"templateIds": PhaseRequestSchema(**kwargs).templateIds})
        self._prepared_request.add({"customNames": PhaseRequestSchema(**kwargs).customNames})
        return self
