"""
App change role schema
"""

from dataclasses import dataclass


@dataclass
class ChangeRoleResponseSchema:
    role_name: str
    status_code: int
