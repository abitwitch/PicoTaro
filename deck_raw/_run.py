
names={
"C01": "Ace of Cups",
"C02": "Two of Cups",
"C03": "Three of Cups",
"C04": "Four of Cups",
"C05": "Five of Cups",
"C06": "Six of Cups",
"C07": "Seven of Cups",
"C08": "Eight of Cups",
"C09": "Nine of Cups",
"C10": "Ten of Cups",
"C11": "Page of Cups",
"C12": "Knight of Cups",
"C13": "Queen of Cups",
"C14": "Kings of Cups",
"M00": "The Fool",
"M01": "The Magician",
"M02": "The High Priestess",
"M03": "The Empress",
"M04": "The Emperor",
"M05": "The Hierophant",
"M06": "The Lovers",
"M07": "The Chariot",
"M08": "Strength",
"M09": "The Hermit",
"M10": "Wheel of Fortune",
"M11": "Justice",
"M12": "The Hanged Man",
"M13": "Death",
"M14": "Temperance",
"M15": "The Devil",
"M16": "The Tower",
"M17": "The Star",
"M18": "The Moon",
"M19": "The Sun",
"M20": "Judgement",
"M21": "The World",
"P01": "Ace of Pentacles",
"P02": "Two of Pentacles",
"P03": "Three of Pentacles",
"P04": "Four of Pentacles",
"P05": "Five of Pentacles",
"P06": "Six of Pentacles",
"P07": "Seven of Pentacles",
"P08": "Eight of Pentacles",
"P09": "Nine of Pentacles",
"P10": "Ten of Pentacles",
"P11": "Page of Pentacles",
"P12": "Knight of Pentacles",
"P13": "Queen of Pentacles",
"P14": "King of Pentacles",
"S01": "Ace of Swords",
"S02": "Two of Swords",
"S03": "Three of Swords",
"S04": "Four of Swords",
"S05": "Five of Swords",
"S06": "Six of Swords",
"S07": "Seven of Swords",
"S08": "Eight of Swords",
"S09": "Nine of Swords",
"S10": "Ten of Swords",
"S11": "Page of Swords",
"S12": "Knight of Swords",
"S13": "Queen of Swords",
"S14": "King of Swords",
"W01": "Ace of Wands",
"W02": "Two of Wands",
"W03": "Three of Wands",
"W04": "Four of Wands",
"W05": "Five of Wands",
"W06": "Six of Wands",
"W07": "Seven of Wands",
"W08": "Eight of Wands",
"W09": "Nine of Wands",
"W10": "Ten of Wands",
"W11": "Page of Wands",
"W12": "Knight of Wands",
"W13": "Queen of Wands",
"W14": "King of Wands",
}


targetfile="_W.py"

with open(targetfile,"r") as f:
  content=f.read()

d={}
for line in content.split("\n"):
  if line.startswith("//"):
    f=line[4:7]
    d[f]=f'name="{names[f]}"\n'
    d[f]+='img=[\n'
  else:
    d[f]+=line+"\n"
 
for key in d.keys():
  d[key]+="]"
  with open(key+".py","w") as f:
    f.write(d[key])



