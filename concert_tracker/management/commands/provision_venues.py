from django.core.management.base import BaseCommand, CommandError
import pandas as pd


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file", type=str)

    def handle(self, *args, **options):
        input_file = options['file']
        input_df = pd.read_csv(input_file)
        input_df['Previous Name(s)'] = input_df['Previous Name(s)'].fillna('')
        print(input_df)

        # for poll_id in options["poll_ids"]:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()

