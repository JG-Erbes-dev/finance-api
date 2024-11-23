from django.core.management.base import BaseCommand
import importlib

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # updateecon = importlib.import_module('updatedata.updateecon')
        # updatevents = importlib.import_module('updatedata.updateevents')
        # updatefinancials = importlib.import_module('updatedata.updatefinancials')
        updatemarket = importlib.import_module('updatedata.updatemarket')
        # updatesearch = importlib.import_module('updatedata.updatesearch')
        # updatevaluation = importlib.import_module('updatedata.updatevaluation')
        # updateecon.execute_all()
        # updatefinancials.execute_all()
        # updatevents.execute_all()
        updatemarket.execute_all()
        # updatesearch.execute_all()
        # updatevaluation.execute_all()
        self.stdout.write(self.style.SUCCESS('Dados coletados e salvos no banco de dados.'))
