import csv, json

def csvParse(csvfile):
    # Open the CSV
    f = open( csvfile, 'rU' )
    reader = csv.DictReader( f, fieldnames = ( "name","type","description", "prerequisites", "benefit", "source"))
    featnames = []
    store = []
    # Store feat names in a list
    for row in reader:
        feat= {"name": row["name"],
        "segments":[]}
        if row["name"] not in featnames:
            featnames.append(row["name"])
            store.append(feat)

    # Create Objects for Feat
    segment = {"segmentName":""}
    for feat in store:
        f = open( csvfile, 'rU' )
        reader = csv.DictReader( f, fieldnames = ( "name","type","description", "prerequisites", "benefit", "source"))
        for row in reader:
            if feat["name"] == row["name"]:
                contents = {
                          "rule1 |": 1,
                          "subtitle |": row["type"],
                          "property | prerequisites |": row["prerequisites"],
                          "rule2 |": 1,
                          "fill1 |": 1,
                          "text1 | ": row["description"],
                          "fill2 |": 1,
                          "text2 | ": row["benefit"],
                          "fill |": 1,
                           }
                segment = {
                        "count": 1,
                        "color": "Maroon",
                        "title": row["name"],
                        "icon": "enlightenment",
                        "icon_back": "enlightenment",
                        "contents": [],
                        "tags": [
                           row["source"]
                                ]
                       }
        feat["segments"].append(segment)
        segment["contents"].append(contents)

    # Parse the CSV into JSON
    out = json.dumps(store, indent=2)
    # Save the JSON
    f = open( 'FeatPFRPG-UCamp.json', 'w')
    f.write(out)

csvParse('PFRPG-UCamp- Updated 22Nov2018.csv')
