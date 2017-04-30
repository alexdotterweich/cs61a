class Doge: 
	much = "wow"
	def bark(self): 
	return self.much
class Puppye(Doge): 
	very = "meow"
	def __init__(self, friend):
		self.friend = friend
		self.much = [Doge.much, friend.much]
	def bark(self):
		return "puppye" + Doge.bark(self)[1]
such = Doge()
such.much = "interesting" fido = Puppye(such)
flora = Puppye(fido)