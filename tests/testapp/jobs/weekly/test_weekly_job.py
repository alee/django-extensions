import mock

from django_extensions.management.jobs import WeeklyJob


WEEKLY_JOB_MOCK = mock.MagicMock()


class Job(WeeklyJob):
    help = "My sample weekly job."

    def execute(self):
        WEEKLY_JOB_MOCK()
