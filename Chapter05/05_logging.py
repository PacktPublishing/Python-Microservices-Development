import logging
from logging.handlers import SMTPHandler

host = "smtp.free.fr", 25
handler = SMTPHandler(mailhost=host, fromaddr="tarek@ziade.org", toaddrs=["tarek@ziade.org"], subject="Service Exception")

logger = logging.getLogger('theapp')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def email_errors(func):
	def _email_errors(*args, **kw):
		try:
			return func(*args, **kw)
		except Exception:
			logger.exception('A problem has occured')
			raise
		return _email_errors

@email_errors
def function_that_raises():
	print(i_dont_exist)

function_that_raises()