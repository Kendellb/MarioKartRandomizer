import numpy as np
import random

        

mushroomCup = np.array(["Mario Kart Stadium","Water Park","Sweet Sweet Canyon"
,"Thwomp Ruins"])


flowerCup = np.array(["Mario Circuit","Toad Harbour","Twisted Mansion"
,"Shy Guy Falls"])

starCup = np.array(["Sunshine Airport","Dolphin Shoals","Electrodome"
,"Mount Wario"])

specialCup = np.array(["Cloudtop Cruise","Bone Dry Dunes","Bowser’s Castle"
,"Rainbow Road"])

shellCup = np.array(["Moo Moo Meadows (Wii)","Mario Circuit (GBA)",
"Cheep Cheep Beach (DS)", "Toad’s Turnpike (N64)"])

bananaCup = np.array(["Dry Dry Desert (GCN)","Donut Plains 3 (SNES)",
"Royal Raceway (N64)","DK Jungle (3DS)"])

leafCup = np.array(["Wario Stadium (DS)","Sherbet Land (GCN)","Melody Motorway (3DS)"
,"Yoshi Valley (N64)"])

lightningCup = np.array(["Tick-Tock Clock (DS)","Piranha Plant Pipeway (3DS)",
"Grumble Volcano (Wii)","Rainbow Road (N64)"])

eggCup = np.array(["Yoshi Circuit(GCN)","Excitebike Arena","Dragon Driftway"
,"Mute City"])

triforceCup = np.array(["Wario's Gold Mine(Wii)","Rainbow Road(SNES)","Ice Ice Outpost"
,"Hyrule Circuit"])

crossingCup = np.array(["Baby Park(GCN)","Cheese Land(GBA)","Wild Woods"
,"Animal Crossing"])

bellCup = np.array(["Neo Bowser City(3DS)","Ribbon Road(GBA)","Super Bell Subway"
,"Big Blue"])

goldenDashCup = np.array(["Paris Promenade(Tour)","Toad Circuit(3DS)","Choco Mountain(N64)"
,"Coconut Mall(Wii)"])

luckyCatCup = np.array(["Tokyo Blur(Tour)","Shroom Ridge(DS)","Sky Garden(GBA)"
,"Ninja Hideaway"])

turnipCup = np.array(["New York Minute(Tour)","Mario Circuit 3(SNES)","Kalimari Desert(N64)"
,"Waluigi Pinball(DS)"])

propellerCup = np.array(["Sydney Sprint(Tour)","Snow Land(GBA)","Mushroom Gorge(Wii)"
,"Sky-High Sundae"])

rockCup = np.array(["London Loop(Tour)","Boo Lake(GBA)","Rock Rock Mountain(3DS)"
,"Maple Treeway(Wii)"])

moonCup = np.array(["Berlin Byways(Tour)","Peach Gardens(DS)","Merry Mountain"
,"Rainbow Road(3DS)"])

fruitCup = np.array(["Amsterdam Drift(Tour)","Riverside Park(GBA)","DK Summit(Wii)"
,"Yoshi's Island"])

boomerangCup = np.array(["Bangkok Rush(Tour)","Mario Circuit(DS)","Waluigi Stadium(GCN)"
,"Singapore Speedway(Tour)"])

featherCup = np.array(["Athens Dash(Tour)","Daisy Cruiser(GCN)","Moonview Highway(Wii)"
,"Squeaky Clean Sprint"])

cherryCup = np.array(["Los Angeles Laps(Tour)","Sunset Wilds(GBA)","Koopa Cape(Wii)"
,"Vancouver Velocity(Tour)"])

#acornCup = np.array("","","","")

#spinyCup = np.array("","","","")

all_arrays = np.array([mushroomCup,flowerCup,starCup,specialCup,shellCup,
bananaCup,leafCup,lightningCup,eggCup,triforceCup,crossingCup,
bellCup,goldenDashCup,luckyCatCup,turnipCup,propellerCup,rockCup,
moonCup,fruitCup,boomerangCup,featherCup,cherryCup])

arrayNames = ["Mushroom Cup","Flower Cup","Star Cup","Special Cup","Shell Cup",
"Banana Cup","Leaf Cup","Lightning Cup","Egg Cup","Triforce Cup","Crossing Cup",
"Bell Cup","Golden Dash Cup","Lucky Cat Cup","Turnip Cup","Propeller Cup","Rock Cup",
"MoonCup","Fruit Cup","Boomerang Cup","Feather Cup","Cherry Cup"]

while(True):
    # 22 cups 4 tracks
    # 24 after all released
    
   
    cup = random.randint(0,21)
    track = random.randint(0,3)

    print(arrayNames[cup])
    print(all_arrays[cup,track],"\n")
   
    input("Press Enter For another Track...\n")


