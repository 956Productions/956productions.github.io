import csv,re 

find_urls = r'https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)'

output = {}
#generate all entries for tournaments
with open('games.csv','r', encoding="utf8") as file:
    read = csv.DictReader(file)
    for row in read:
        g = {
            "Event" : row['Tournament'],
            "Region" : row['Abbr-Regions List'].replace("SA/",""),
            "Game" : row['Game Name'],
            "Bracket": "",
            "Phase": "",
            "VOD" : "",
            "1" : "",
            "2" : "",
            "3" : "",
            "4" : "",
            "Count" : 1
        }
        if row['Alt Reg URL'] != "":
            g["Bracket"] = row['Alt Reg URL']
        else:
            g["Bracket"] = row['Smash URL']
        output[g["Event"]] = g
#format VOD info into markdown
with open('vod.csv','r', encoding="utf8") as file:
    read = csv.DictReader(file)
    for row in read:
        if row['Tournament'] in output:
            g = output[row['Tournament']]
            g['Phase'] = row['Phase']
            links = re.findall(find_urls,row['Final VOD URL'])
            if len(links) > 1:
                c = 0
                for i in links:
                    g['VOD'] += "<a href='%s'>VOD %s</a>, " % (links[c],g['Count'])
                    g['Count'] += 1
                    c += 1
            elif len(links) == 1:
                if g['Count'] > 1:
                    if g['VOD'][-2:] != ", ":
                        g['VOD'] += ", "
                    g['VOD'] += "<a href='%s'>VOD %s</a>, " % (links[0],g['Count'])
                    g['Count'] += 1
                else:
                    g['VOD'] += "<a href='%s'>VOD</a>" % links[0]
                    g['Count'] += 1
#fill out names of players
with open('results.csv','r', encoding="utf8") as file:
    read = csv.DictReader(file)
    for row in read:
        if row['Tournaments'] in output:
            g = output[row['Tournaments']]
            placements = ["1","2","3","4"]
            types = ["-Organization","-Tag","-Twitter/Mastodon"]
            for i in placements:
                if i in row['Placing'] and "5" not in row['Placing'] and "7" not in row['Placing']:
                    p = ""
                    if row['Player-Organization'] != '':
                        p += "<b>" + row['Player-Organization'] + "</b> | "
                    p += row['Player-Tag']
                    if row['Player-Twitter/Mastodon'] != '':
                        p += " (%s)" % row['Player-Twitter/Mastodon']
                    if g[i] != '':
                        g[i] += ", " + p
                    else:
                        g[i] = p
                    break

#make sure to account for teams
fields = ['Event',"Region","Game","VOD","Bracket","Phase","1","2","3","4"]
with open('output.csv', 'w', encoding="utf8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields, lineterminator = '\n')
    writer.writeheader()
    for i in output:
        del output[i]['Count']
        output[i]['VOD'] = output[i]['VOD'].rstrip(', ')
        writer.writerow(output[i])