from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from poetry.core.packages.dependency import Dependency


MAIN_GROUP = "main"


class DependencyGroup:
    def __init__(self, name: str, optional: bool = False) -> None:
        self._name: str = name
        self._optional: bool = optional
        self._dependencies: list[Dependency] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def dependencies(self) -> list[Dependency]:
        return self._dependencies

    def is_optional(self) -> bool:
        return self._optional

    def add_dependency(self, dependency: Dependency) -> None:
        self._dependencies.append(dependency)

    def remove_dependency(self, name: str) -> None:
        from poetry.core.utils.helpers import canonicalize_name

        name = canonicalize_name(name)

        dependencies = [
            dependency for dependency in self.dependencies if dependency.name != name
        ]

        self._dependencies = dependencies

    def __eq__(self, other: object) -> bool:
        return (
            self._name == other.name
            and set(self._dependencies) == set(other.dependencies)
            if isinstance(other, DependencyGroup)
            else NotImplemented
        )

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"{cls}({self._name}, optional={self._optional})"
