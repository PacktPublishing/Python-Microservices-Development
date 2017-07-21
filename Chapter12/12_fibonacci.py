class Fibo:
	def __init__(self, max=10):
		self.a, self.b = 0, 1
		self.max = max
		self.count = 0
		
	def __iter__(self):
		return self

	def next(self):
		try:
			return self.a
		finally:
			if self.count == self.max:
				raise StopIteration()
			self.a, self.b = self.b, self.a + self.b
			self.count += 1