from playwright.sync_api import Page

class HomePage:
	def __init__(self, page: Page, base_url: str):
		self.page = page
		self.base_url = base_url

	def open(self):
		self.page.goto(self.base_url)
		return self

	def header(self):
		# Stub para el header, se puede expandir según necesidades del test
		class Header:
			def go_to_register(self_inner):
				pass
			def go_to_login(self_inner):
				pass
		return Header()
