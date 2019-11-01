# -*- coding: UTF-8 -*- 

class WinDoor:
	""" Площадь окон и дверей """
	def __init__(self, widht_WinDoor, height_WinDoor):
		self.squale_WinDoor = widht_WinDoor * height_WinDoor

class Room:
	def __init__(self, widht_room, height_room, leight_room):
		self.squale_room = 2 * leight_room * (widht_room + height_room)
		self.wd = []
		self.new_square = self.squale_room
		self.squale_wallpapers = 0
		self.number_of_wallpapers = 0
	
	def add_square_winDoor(self, w, h):
		self.wd.append(WinDoor(w, h))
		for i in self.wd:
			self.new_square -= i.squale_WinDoor
		return self.new_square
	
	def add_square_rool(self, h, w):
		self.squale_wallpapers = h * w
		self.number_of_wallpapers = self.new_square
		self.number_of_wallpapers /= self.squale_wallpapers
		return self.number_of_wallpapers

	def show_room(self):
		print('\n' + 'Square room: %s' % self.squale_room + '\n'
			  + 'square work: %s' % self.new_square + '\n'
			  + 'Number of rolls: %s' % round(self.number_of_wallpapers))

	


def main():
	work = Room(3, 5, 2)
	work.add_square_winDoor(1.5, 2.5)
	work.add_square_rool(.75, 3)
	work.show_room()
	

if __name__ == '__main__':
	main() 