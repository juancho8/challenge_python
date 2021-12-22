print('Bienvenido al nba roster !\n')
teamRoster = []
positions = ['Point Guard:','Shooting Guard:','Small Forward:','Power Forward:','Center:']
 
#obtenemos los inputs de los usuarios

teamRoster.append(str(input('Who is your point guard: ')).capitalize())
# quien es tu escolta
teamRoster.append(str(input('Who is your shooting guard: ')).capitalize())
#quien es tu ala
teamRoster.append(str(input('Who is your small forward: ')).capitalize())
# quien es pivot
teamRoster.append(str(input('Who is your power forward: ')).capitalize())
# quien es tu ala pivot
teamRoster.append((input('Who is your center: ')).capitalize())
#quien es tu base
print('\nYour starting 5 for the upcoming basketball season')
for i in range(len(teamRoster)):
    print(str(positions[i])+'\t'+str(teamRoster[i]))

added_player = str(input(('\nOh no, '+str(teamRoster[2])+' is injured \nYour roster only has 4 players \nWho will take '+str(teamRoster[2])+' spot: '))).capitalize()
teamRoster[2] = added_player

print('\nYour starting 5 for the upcoming basketball season')
for i in range(len(teamRoster)):
    print(str(positions[i])+'\t'+str(teamRoster[i]))
print('Good luck '+added_player+' you will do great! \nYour roster now has 5 players')