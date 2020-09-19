alien_o = {'color': 'green', 'points': 5}
print(alien_o['color'])
print(alien_o['points'])

alien_o['x_position'] = 0
alien_o['y_position'] = 25
print(alien_o)

alien_o = {'color': 'green'}
print(f"The alien is {alien_o['color']}.")

alien_o['color'] = 'yellow'
print(f"The alien is now {alien_o['color']}")

alien_o = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

if alien_o == 'slow':
    x_increment = 1

elif alien_o['speed'] == 'medium':
    x_increment = 2

else:
    x_increment = 3


alien_o['x_position'] = alien_o['x_position'] + x_increment
print(f"La position de  x est {alien_o['x_position']}")

del alien_o['speed']
print(alien_o)


