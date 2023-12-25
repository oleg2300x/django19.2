# import json
# import logging
#
# from apscheduler.schedulers.blocking import BlockingScheduler
# from django.conf import settings
# from django.core.management import BaseCommand
# from django_apscheduler.jobstores import DjangoJobStore
#
# from catalog.models import Category, Product
# from apscheduler.triggers.cron import CronTrigger
#
#
# logger = logging.getLogger(__name__)
#
# def print_hello():
#   print('Hello world!!!')
#
#
# class Command(BaseCommand):
#   help = "Runs APScheduler."
#
#   def handle(self, *args, **options):
#     scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
#     scheduler.add_jobstore(DjangoJobStore(), "default")
#
#     scheduler.add_job(
#       print_hello(),
#       trigger=CronTrigger(second="*/10"),  # Every 10 seconds
#       id="my_job",  # The `id` assigned to each job MUST be unique
#       max_instances=1,
#       replace_existing=True,
#     )
#     logger.info("Added job 'my_job'.")
#
#     # scheduler.add_job(
#     #   delete_old_job_executions,
#     #   trigger=CronTrigger(
#     #     day_of_week="mon", hour="00", minute="00"
#     #   ),  # Midnight on Monday, before start of the next work week.
#     #   id="delete_old_job_executions",
#     #   max_instances=1,
#     #   replace_existing=True,
#     # )
#     # logger.info(
#     #   "Added weekly job: 'delete_old_job_executions'."
#     # )
#
#     try:
#       logger.info("Starting scheduler...")
#       scheduler.start()
#     except KeyboardInterrupt:
#       logger.info("Stopping scheduler...")
#       scheduler.shutdown()
#       logger.info("Scheduler shut down successfully!")