#https://www.geeksforgeeks.org/plotting-world-map-using-pygal-in-python/


# import pygal
import pygal

# import Style class from pygal.style
from pygal.style import Style

# create a Style object
custom_style = Style(colors=('#FF0000', '#0000FF',
                             '#00FF00', '#000000',
                             '#FFD700'))

# create a world map,
# Style class is used for using
# the custom colours in the map,
worldmap = pygal.maps.world.World(style
                                  =custom_style)

# set the title of the map
worldmap.title = 'Some Countries Starting from Specific Letters'

# hex code of colours are used
# for every .add() called
worldmap.add('"E" Countries',
             ['ec', 'ee', 'eg', 'eh',
              'er', 'es', 'et'])

worldmap.add('"F" Countries',
             ['fr', 'fi'])

worldmap.add('"P" Countries',
             ['pa', 'pe', 'pg', 'ph', 'pk',
              'pl', 'pr', 'ps', 'pt', 'py'])

worldmap.add('"Z" Countries',
             ['zm', 'zw'])

worldmap.add('"A" Countries',
             ['ad', 'ae', 'af', 'al', 'am', 'ao',
              'aq', 'ar', 'at', 'au', 'az'],
             color='black')

# save into the file
worldmap.render_to_file('abc.svg')

print("Success")

# import pygal library
import pygal

# create a world map
worldmap = pygal.maps.world.SupranationalWorld()

# set the title of map
worldmap.title = 'Continents'

# adding the continents
worldmap.add('Africa', [('africa')])
worldmap.add('North america', [('north_america')])
worldmap.add('Oceania', [('oceania')])
worldmap.add('South america', [('south_america')])
worldmap.add('Asia', [('asia')])
worldmap.add('Europe', [('europe')])
worldmap.add('Antartica', [('antartica')])

# save into the file
worldmap.render_to_file('continent.svg')

print("Success")