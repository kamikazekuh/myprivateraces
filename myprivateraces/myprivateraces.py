from commands.say import SayCommand
from commands.client import ClientCommand
from menus import PagedMenu
from menus import PagedOption
from players.entity import Player
import wcs
from wcs import admin

@ClientCommand('mpr')
@SayCommand('mpr')
@ClientCommand('myprivateraces')
@SayCommand('myprivateraces')
def mpr_command(command,index,team=None):
	if has_private(index) == 1:
		mpr_menu.send(index)
	else:
		wcs.wcs.tell(Player(index).userid,'\x04[WCS] \x05You do not have any private races!')
	




def mpr_menu_select(menu,index,choice):
	userid = Player(index).userid
	player = wcs.wcs.getPlayer(userid)
	player.changeRace(choice.value)


def mpr_menu_build(menu,index):
	menu.clear()
	races = wcs.wcs.racedb.getAll()
	player_entity = Player(index)
	userid = player_entity.userid
	allraces = races.keys()
	counter = 0
	for number, race in enumerate(allraces):
		player = wcs.wcs.getPlayer(userid)
		level = wcs.wcs._getRace(player.player.UserID, race, userid).level
		raceinfo = wcs.wcs.racedb.getRace(race)
		allowonly = str(raceinfo['allowonly'])
		if allowonly == player_entity.steamid:
			nol = int(raceinfo['numberoflevels'])
			nos = int(raceinfo['numberofskills'])
			max_level = nol * nos
			level_buffer = level
			if level_buffer > max_level:
				level_buffer = max_level
			if wcs.wcs.showracelevel:
				level = wcs.wcs._getRace(player.player.UserID, race, userid).level
			if level > 0:
				option = PagedOption('%s - [%s/%s]' % (str(race), str(level_buffer),str(max_level)), race)
				menu.append(option)
				counter += 1
			else:
				option = PagedOption('%s' % str(race), race)
				menu.append(option)
				counter += 1
		if 'ADMINS' in allowonly:
			if admin.is_admin(player_entity.userid):
				nol = int(raceinfo['numberoflevels'])
				nos = int(raceinfo['numberofskills'])
				max_level = nol * nos
				level_buffer = level
				if level_buffer > max_level:
					level_buffer = max_level
				if wcs.wcs.showracelevel:
					level = wcs.wcs._getRace(player.player.UserID, race, userid).level
				if level > 0:
					option = PagedOption('%s - [%s/%s]' % (str(race), str(level_buffer),str(max_level)), race)
					menu.append(option)
					counter += 1
				else:
					option = PagedOption('%s' % str(race), race)
					menu.append(option)	
					counter += 1

		
mpr_menu = PagedMenu(title='My Private Races', build_callback=mpr_menu_build, select_callback=mpr_menu_select,fill=False)

def has_private(index):
	races = wcs.wcs.racedb.getAll()
	player_entity = Player(index)
	userid = player_entity.userid
	allraces = races.keys()
	counter = 0
	for number, race in enumerate(allraces):
		player = wcs.wcs.getPlayer(userid)
		level = wcs.wcs._getRace(player.player.UserID, race, userid).level
		raceinfo = wcs.wcs.racedb.getRace(race)
		allowonly = str(raceinfo['allowonly'])
		if allowonly == player_entity.steamid:
			nol = int(raceinfo['numberoflevels'])
			nos = int(raceinfo['numberofskills'])
			max_level = nol * nos
			level_buffer = level
			if level_buffer > max_level:
				level_buffer = max_level
			if wcs.wcs.showracelevel:
				level = wcs.wcs._getRace(player.player.UserID, race, userid).level
			if level > 0:
				counter += 1
			else:
				counter += 1
		if 'ADMINS' in allowonly:
			if admin.is_admin(player_entity.userid):
				nol = int(raceinfo['numberoflevels'])
				nos = int(raceinfo['numberofskills'])
				max_level = nol * nos
				level_buffer = level
				if level_buffer > max_level:
					level_buffer = max_level
				if wcs.wcs.showracelevel:
					level = wcs.wcs._getRace(player.player.UserID, race, userid).level
				if level > 0:
					counter += 1
				else:
					counter += 1
	if counter == 0:
		return 0
	if counter > 0:
		return 1
