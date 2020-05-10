from django.apps import AppConfig


class MillionConfig(AppConfig):
    name = 'million'
class AccountsConfig(AppConfig):
	name='million'

	def ready(self):
		import million.signals