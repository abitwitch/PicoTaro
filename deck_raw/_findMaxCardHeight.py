import math
white=0xff
width=152
maxHeight=0

deck=['C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09', 'C10', 'C11', 'C12', 'C13', 'C14', 'M00', 'M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08', 'P09', 'P10', 'P11', 'P12', 'P13', 'P14', 'S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08', 'S09', 'S10', 'S11', 'S12', 'S13', 'S14', 'W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W08', 'W09', 'W10', 'W11', 'W12', 'W13', 'W14']

for cardModule in deck:
  card=__import__(f"{cardModule}", None, None, [None])
  reverseImg=card.img
  reverseImg.reverse()
  c=0
  for val in reverseImg:
    if val!=white:
      height=math.ceil((len(card.img)-c)/(width/8))
      break
    c+=1
  maxHeight=max(maxHeight,height)
  print(f"{card.name} Height: {height}")

print(f"Max Height: {maxHeight}")
  
  