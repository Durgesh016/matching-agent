from abc import ABC, abstractmethod

from app.models.schemas import JobPosting


class JobSource(ABC):

    @abstractmethod
    def get_jobs(
        self, role: str = "", location: str = "", page: int = 1
    ) -> list[JobPosting]:
        pass
