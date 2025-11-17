import tkinter as tk
from tkinter import ttk

pricing = {
    "summer":{
        "weekday":{
            "before10":{
                "public": 110.00,
                "VIP": 90.00,
                "associate": 100.00,
                "junior": 110.00,
                "practice": 90.00,
                "full": 0,
                "cart": 25.00,
                "cartmember": 22.12,
                "pushcart": 15.00
            },
            "10-1":{
                "public": 110.00,
                "VIP": 90.00,
                "associate": 100.00,
                "junior": 50.00,
                "practice": 90.00,
                "full": 0,
                "cart": 25.00,
                "cartmember": 22.12,
                "pushcart": 15.00
            },
            "1-3":{
                "public": 100.00,
                "VIP": 80.00,
                "associate": 90.00,
                "junior": 50.00,
                "practice": 80.00,
                "full": 0,
                "cart": 25.00,
                "cartmember": 22.12,
                "pushcart": 15.00
            },
            "3-4":{
                "public": 100.00,
                "VIP": 80.00,
                "associate": 90.00,
                "junior": 50.00,
                "practice": 80.00,
                "full": 0,
                "cart": 15.00,
                "cartmember": 13.27,
                "pushcart": 7.50
            },
            "4-5":{
                "public": 75.00,
                "VIP": 55.00,
                "associate": 65.00,
                "junior": 50.00,
                "practice": 55.00,
                "full": 0,
                "cart": 15.00,
                "cartmember": 13.27,
                "pushcart": 7.50
            },
            "5-close":{
                "public": 75.00,
                "VIP": 55.00,
                "associate": 65.00,
                "junior": 50.00,
                "juniorwithadult": 0,
                "practice": 0,
                "full": 0,
                "cart": 15.00,
                "cartmember": 13.27,
                "pushcart": 7.50
            }      
        },
        "friday":{
            "before10":{
                "public": 120.00,
                "VIP": 100.00,
                "associate":110.00,
                "junior":120.00,
                "juniormember": 100.00,
                "practice": 100.00,
                "full": 0,
                "cart":25.00,
                "cartmember":22.12,
                "pushcart":15.00
            },
            "10-11":{
                "public": 120.00,
                "VIP": 100.00,
                "associate":110.00,
                "junior":50.00,
                "juniormember": 50.00,
                "practice": 100.00,
                "full": 0,
                "cart":25.00,
                "cartmember":22.12,
                "pushcart":15.00 
            },
            "11-3":{
                "public": 110.00,
                "VIP": 90.00,
                "associate":100.00,
                "junior":50.00,
                "juniormember": 0,
                "practice": 90.00,
                "full": 0,
                "cart":25.00,
                "cartmember":22.12,
                "pushcart":15.00 
            },
            "3-4":{
                "public": 110.00,
                "VIP": 90.00,
                "associate":100.00,
                "junior":50.00,
                "juniormember": 0,
                "practice": 90.00,
                "full": 0,
                "cart":15.00,
                "cartmember":13.27,
                "pushcart": 7.50 
            },
            "4-5":{
                "public": 75.00,
                "VIP": 55.00,
                "associate":65.00,
                "junior":50.00,
                "juniormember": 0,
                "practice": 55.00,
                "full": 0,
                "cart":15.00,
                "cartmember":13.27,
                "pushcart": 7.50 
            },
            "5-close":{
                "public": 75.00,
                "VIP": 55.00,
                "associate":65.00,
                "junior":50.00,
                "juniorwithadult":0,
                "juniormember": 0,
                "practice": 0,
                "full": 0,
                "cart":15.00,
                "cartmember":13.27,
                "pushcart": 7.50 
            }
        },
        "weekend/holiday":{
            "before10":{
                "public": 120.00,
                "VIP": 100.00,
                "associate": 110.00,
                "junior": 120.00,
                "juniormember": 100.00,
                "intermediate": 100.00,
                "weekday": 100.00,
                "practice": 100.00,
                "full": 0,
                "cart": 25.00,
                "cartmember": 22.12,
                "pushcart": 15.00
            },
            "10-11":{
                "public": 120.00,
                "VIP": 100.00,
                "associate": 110.00,
                "junior": 50.00,
                "juniormember": 100.00,
                "intermediate": 100.00,
                "weekday": 100.00,
                "practice": 100.00,
                "full": 0,
                "cart": 25.00,
                "cartmember": 22.12,
                "pushcart": 15.00
            },
            "11-3":{
                "public": 110.00,
                "VIP": 90.00,
                "associate": 100.00,
                "junior": 50.00,
                "juniormember": 0.00,
                "intermediate": 0.00,
                "weekday": 90.00,
                "practice": 90.00,
                "full": 0,
                "cart": 25.00,
                "cartmember": 22.12,
                "pushcart": 15.00
            },
            "3-4":{
                "public": 110.00,
                "VIP": 90.00,
                "associate": 100.00,
                "junior": 50.00,
                "juniormember": 0.00,
                "intermediate": 0.00,
                "weekday": 90.00,
                "practice": 90.00,
                "full": 0,
                "cart": 15.00,
                "cartmember": 13.27,
                "pushcart": 7.50
            },
            "4-5":{
                "public": 75.00,
                "VIP": 55.00,
                "associate": 65.00,
                "junior": 50.00,
                "juniormember": 0.00,
                "intermediate": 0.00,
                "weekday": 55.00,
                "practice": 55.00,
                "full": 0,
                "cart": 15.00,
                "cartmember": 13.27,
                "pushcart": 7.50
            },
            "5-close":{
                "public": 75.00,
                "VIP": 55.00,
                "associate": 65.00,
                "junior": 50.00,
                "juniorwithadult":0,
                "juniormember": 0.00,
                "intermediate": 0.00,
                "weekday": 55.00,
                "practice": 0.00,
                "full": 0,
                "cart": 15.00,
                "cartmember": 13.27,
                "pushcart": 7.50
            }
        }
    },
    "spring/fall":{
        "weekday":{
            "before10":{
                "public": 99.00,
                "VIP": 79.00,
                "associate": 89.00,
                "junior": 99.00,
                "practice": 79.00,
                "full": 0,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "10-1":{
                "public": 99.00,
                "VIP": 79.00,
                "associate": 89.00,
                "junior": 50.00,
                "practice": 79.00,
                "full": 0,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "1-2":{
                "public": 99.00,
                "VIP": 79.00,
                "associate": 89.00,
                "junior": 50.00,
                "practice": 79.00,
                "full": 0,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50,
            },
            "2-3":{
                "public": 65.00,
                "VIP": 45.00,
                "associate": 55.00,
                "junior": 50.00,
                "practice": 45.00,
                "full": 0,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50, 
            },
            "3-close":{
                "public": 65.00,
                "VIP": 45.00,
                "associate": 55.00,
                "junior": 50.00,
                "juniorwithadult": 0,
                "practice": 0.00,
                "full": 0,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50, 
            }
        },
        "friday":{
            "before10":{
                "public": 99.00,
                "VIP": 79.00,
                "associate": 89.00,
                "junior": 99.00,
                "juniormember": 79.00,
                "practice": 79.00,
                "full": 0,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "10-11":{
                "public": 99.00,
                "VIP": 79.00,
                "associate": 89.00,
                "junior": 50.00,
                "juniormember": 50.00,
                "practice": 79.00,
                "full": 0,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "11-1":{
                "public": 99.00,
                "VIP": 79.00,
                "associate": 89.00,
                "junior": 50.00,
                "juniormember": 0.00,
                "practice": 79.00,
                "full": 0,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "1-2":{
                "public": 99.00,
                "VIP": 79.00,
                "associate": 89.00,
                "junior": 50.00,
                "juniormember": 0.00,
                "practice": 79.00,
                "full": 0,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50,
            },
            "2-3":{
                "public": 65.00,
                "VIP": 45.00,
                "associate": 55.00,
                "junior": 50.00,
                "juniormember": 0,
                "practice": 45.00,
                "full": 0,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50, 
            },
            "3-close":{
                "public": 65.00,
                "VIP": 45.00,
                "associate": 55.00,
                "junior": 50.00,
                "juniorwithadult": 0,
                "juniormember": 0,
                "practice": 0.00,
                "full": 0,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50, 
            }
        },
        "weekend/holiday":{
            "before10":{
                "public": 99.00,
                "VIP": 79.00,
                "associate": 89.00,
                "junior": 99.00,
                "juniormember": 79.00,
                "intermediate": 79.00,
                "practice": 79.00,
                "full": 0,
                "weekday": 79.00,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "10-11":{
                "public": 99.00,
                "VIP": 79.00,
                "associate": 89.00,
                "junior": 50.00,
                "juniormember": 79.00,
                "intermediate": 79.00,
                "practice": 79.00,
                "full": 0,
                "weekday": 79.00,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "11-1":{
                "public": 99.00,
                "VIP": 79.00,
                "associate": 89.00,
                "junior": 50.00,
                "juniormember": 0.00,
                "intermediate": 0.00,
                "practice": 79.00,
                "full": 0,
                "weekday": 79.00,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "1-2":{
                "public": 99.00,
                "VIP": 79.00,
                "associate": 89.00,
                "junior": 50.00,
                "juniormember": 0.00,
                "intermediate": 0.00,
                "practice": 79.00,
                "full": 0,
                "weekday": 79.00,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50,
            },
            "2-3":{
                "public": 65.00,
                "VIP": 45.00,
                "associate": 55.00,
                "junior": 50.00,
                "juniormember": 0,
                "intermediate": 0,
                "practice": 45.00,
                "full": 0,
                "weekday": 45.00,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50, 
            },
            "3-close":{
                "public": 65.00,
                "VIP": 45.00,
                "associate": 55.00,
                "junior": 50.00,
                "juniormember": 0,
                "juniorwithadult":0,
                "intermediate": 0,
                "practice": 0.00,
                "full": 0,
                "weekday": 45.00,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50, 
            }
        }
    }
}


appstate = {
    "season": None,
    "whatday": None,
    "Timeframe": None,
    "totalplayers": 0,
    "players" : [],
    "holesplayed": None,
    "currentplayer": 0 
}

def seasonselect(season):
    appstate["season"] = season
    daysection()

def dayselect(whatday):
    appstate["whatday"] = whatday
    timeframesection()

def timeframeselect(timeframe):
    appstate["Timeframe"] = timeframe
    numberofplayerssection()

def numberofplayersselect(totalplayers):
    appstate["totalplayers"] = totalplayers
    appstate["players"] = [{"membership": None, "holesplayed": None, "walkride": None,} for _ in range(totalplayers)]
    appstate["currentplayer"] = 0
    membershipsection()

def membershipselect(membership):
    temp = appstate["currentplayer"]
    appstate["players"][temp]["membership"] = membership
    holesection()

def holeselect(holesplayed):
    temp = appstate["currentplayer"]
    appstate["players"][temp]["holesplayed"] = holesplayed
    methodsection()

def methodselect(method):
    pass

root = tk.Tk()
root.title("Royal Ashburn Rain Check Calculator by Jackson Blellock")
root.geometry("2800x2600")
mainframe = tk.Frame(root)
mainframe.pack(fill="both", expand=True)

#Season Select
def seasonsection():
    for widget in mainframe.winfo_children():
        widget.destroy()

    title = tk.Label(mainframe, text="Select Season", font=("Arial", 20))
    title.pack(pady=40)

    summerbutton = tk.Button(mainframe, text="Summer", font=("Arial", 20), height=2, width=20, command=lambda: seasonselect("summer"))
    summerbutton.pack(pady=20)

    springfallbutton = tk.Button(mainframe, text="Spring/Fall", font=("Arial", 20), height=2, width=20, command=lambda: seasonselect("spring/fall"))
    springfallbutton.pack(pady=20)

def daysection():
    for widget in mainframe.winfo_children():
        widget.destroy()

    title = tk.Label(mainframe, text="Select Day", font=("Arial", 20))
    title.pack(pady=40)

    weekdaybutton = tk.Button(mainframe, text="Weekday", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("weekday"))
    weekdaybutton.pack(pady=20)

    fridaybutton = tk.Button(mainframe, text="Friday", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("friday"))
    fridaybutton.pack(pady=20)

    weekendholidaybutton = tk.Button(mainframe, text="Weekend/Holiday", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("weekend/holiday"))
    weekendholidaybutton.pack(pady=20)

def timeframesection():
    for widget in mainframe.winfo_children():
        widget.destroy()

    title = tk.Label(mainframe, text="Select time of Tee Time", font=("Arial", 20))
    title.pack(pady=40)

    if appstate["season"] == "summer":
        if appstate["whatday"] == "weekday":
            before10button = tk.Button(mainframe, text="Before 10 AM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("before10"))
            before10button.pack(pady=20)

            tento1button = tk.Button(mainframe, text="10AM - 12:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("10-1"))
            tento1button.pack(pady=20)

            oneto3button = tk.Button(mainframe, text="1PM - 2:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("1-3"))
            oneto3button.pack(pady=20)

            threeto4button = tk.Button(mainframe, text="3PM - 3:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("3-4"))
            threeto4button.pack(pady=20)

            fourto5button = tk.Button(mainframe, text="4PM - 4:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("4-5"))
            fourto5button.pack(pady=20)

            fivetoclosebutton = tk.Button(mainframe, text="After 5PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("5-close"))
            fivetoclosebutton.pack(pady=20)
        elif appstate["whatday"] == "friday":
            before10button = tk.Button(mainframe, text="Before 10 AM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("before10"))
            before10button.pack(pady=20)

            tento11button = tk.Button(mainframe, text="10AM - 10:50AM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("10-11"))
            tento11button.pack(pady=20)

            elevento3button = tk.Button(mainframe, text="11AM - 2:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("11-3"))
            elevento3button.pack(pady=20)

            threeto4button = tk.Button(mainframe, text="3PM - 3:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("3-4"))
            threeto4button.pack(pady=20)

            fourto5button = tk.Button(mainframe, text="4PM - 4:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("4-5"))
            fourto5button.pack(pady=20)

            fivetoclosebutton = tk.Button(mainframe, text="After 5PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("5-close"))
            fivetoclosebutton.pack(pady=20)

        elif appstate["whatday"] =="weekend/holiday":
            before10button = tk.Button(mainframe, text="Before 10 AM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("before10"))
            before10button.pack(pady=20)

            tento11button = tk.Button(mainframe, text="10AM - 10:50AM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("10-11"))
            tento11button.pack(pady=20)

            elevento3button = tk.Button(mainframe, text="11AM - 2:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("11-3"))
            elevento3button.pack(pady=20)

            threeto4button = tk.Button(mainframe, text="3PM - 3:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("3-4"))
            threeto4button.pack(pady=20)

            fourto5button = tk.Button(mainframe, text="4PM - 4:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("4-5"))
            fourto5button.pack(pady=20)

            fivetoclosebutton = tk.Button(mainframe, text="After 5PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("5-close"))
            fivetoclosebutton.pack(pady=20)

    else:
        if appstate["whatday"] == "weekday":
            before10button = tk.Button(mainframe, text="Before 10 AM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("before10"))
            before10button.pack(pady=20)

            tento1button = tk.Button(mainframe, text="10AM - 12:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("10-1"))
            tento1button.pack(pady=20)

            oneto2button = tk.Button(mainframe, text="1PM - 1:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("1-2"))
            oneto2button.pack(pady=20)

            twoto3button = tk.Button(mainframe, text="2PM - 2:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("2-3"))
            twoto3button.pack(pady=20)

            threetoclosebutton = tk.Button(mainframe, text="After 3PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("3-close"))
            threetoclosebutton.pack(pady=20)


        elif appstate["whatday"] == "friday":
            before10button = tk.Button(mainframe, text="Before 10 AM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("before10"))
            before10button.pack(pady=20)

            tento11button = tk.Button(mainframe, text="10AM - 10:50AM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("10-11"))
            tento11button.pack(pady=20)

            elevento1button = tk.Button(mainframe, text="11AM - 12:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("11-1"))
            elevento1button.pack(pady=20)

            oneto2button = tk.Button(mainframe, text="1PM - 1:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("1-2"))
            oneto2button.pack(pady=20)

            twoto3button = tk.Button(mainframe, text="2PM - 2:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("2-3"))
            twoto3button.pack(pady=20)

            threetoclosebutton = tk.Button(mainframe, text="After 3PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("3-close"))
            threetoclosebutton.pack(pady=20)

        elif appstate["whatday"] =="weekend/holiday":
            before10button = tk.Button(mainframe, text="Before 10 AM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("before10"))
            before10button.pack(pady=20)

            tento11button = tk.Button(mainframe, text="10AM - 10:50AM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("10-11"))
            tento11button.pack(pady=20)

            elevento1button = tk.Button(mainframe, text="11AM - 12:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("11-1"))
            elevento1button.pack(pady=20)

            oneto2button = tk.Button(mainframe, text="1PM - 1:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("1-2"))
            oneto2button.pack(pady=20)

            twoto3button = tk.Button(mainframe, text="2PM - 2:50PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("2-3"))
            twoto3button.pack(pady=20)

            threetoclosebutton = tk.Button(mainframe, text="After 3PM", font=("Arial", 20), height=2, width=20, command=lambda: timeframeselect("3-close"))
            threetoclosebutton.pack(pady=20)

def numberofplayerssection():
    for widget in mainframe.winfo_children():
        widget.destroy()

    title = tk.Label(mainframe, text="How Many People in the Group are Getting Rain Checks", font=("Arial", 20))
    title.pack(pady=40)

    oneplayerbutton = tk.Button(mainframe, text="1", font=("Arial", 20), height=2, width=20, command=lambda: numberofplayersselect(1))
    oneplayerbutton.pack(pady=20)

    twoplayersbutton = tk.Button(mainframe, text="2", font=("Arial", 20), height=2, width=20, command=lambda: numberofplayersselect(2))
    twoplayersbutton.pack(pady=20)

    threeplayersbutton = tk.Button(mainframe, text="3", font=("Arial", 20), height=2, width=20, command=lambda: numberofplayersselect(3))
    threeplayersbutton.pack(pady=20)

    fourplayersbutton = tk.Button(mainframe, text="4", font=("Arial", 20), height=2, width=20, command=lambda: numberofplayersselect(4))
    fourplayersbutton.pack(pady=20)

def membershipsection():
    for widget in mainframe.winfo_children():
        widget.destroy()

    title = tk.Label(mainframe, text="Membership Selection for Player", font=("Arial", 20))
    title.pack(pady=40)

    if appstate["whatday"] == "weekday" or appstate["whatday"] == "friday":
        if appstate["Timeframe"] == "5-close" or appstate["Timeframe"] == "3-close":
            publicbutton = tk.Button(mainframe, text="Public Player", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("public"))
            publicbutton.pack(pady=20)

            vipbutton = tk.Button(mainframe, text="VIP", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("VIP"))
            vipbutton.pack(pady=20)

            associatebutton = tk.Button(mainframe, text="Associate", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("associate"))
            associatebutton.pack(pady=20)

            juniorbutton = tk.Button(mainframe, text="Junior", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("junior"))
            juniorbutton.pack(pady=20)

            juniorwithadultbutton = tk.Button(mainframe, text="Junior with paying Adult", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("juniorwithadult"))
            juniorwithadultbutton.pack(pady=20)

            practicebutton = tk.Button(mainframe, text="Practice Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("practice"))
            practicebutton.pack(pady=20)

            fullbutton = tk.Button(mainframe, text="Full/Weekday/Intermediate/Junior Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("full"))
            fullbutton.pack(pady=20)
        else:
            publicbutton = tk.Button(mainframe, text="Public Player", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("public"))
            publicbutton.pack(pady=20)

            vipbutton = tk.Button(mainframe, text="VIP", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("VIP"))
            vipbutton.pack(pady=20)

            associatebutton = tk.Button(mainframe, text="Associate", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("associate"))
            associatebutton.pack(pady=20)

            juniorbutton = tk.Button(mainframe, text="Junior", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("junior"))
            juniorbutton.pack(pady=20)

            practicebutton = tk.Button(mainframe, text="Practice Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("practice"))
            practicebutton.pack(pady=20)

            fullbutton = tk.Button(mainframe, text="Full/Weekday/Intermediate/Junior Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("full"))
            fullbutton.pack(pady=20)
    else:
        if appstate["Timeframe"] == "5-close" or appstate["Timeframe"] == "3-close":
            publicbutton = tk.Button(mainframe, text="Public Player", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("public"))
            publicbutton.pack(pady=20)

            vipbutton = tk.Button(mainframe, text="VIP", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("VIP"))
            vipbutton.pack(pady=20)

            associatebutton = tk.Button(mainframe, text="Associate", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("associate"))
            associatebutton.pack(pady=20)

            juniorbutton = tk.Button(mainframe, text="Junior", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("junior"))
            juniorbutton.pack(pady=20)

            juniorwithadultbutton = tk.Button(mainframe, text="Junior with paying Adult", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("juniorwithadult"))
            juniorwithadultbutton.pack(pady=20)

            practicebutton = tk.Button(mainframe, text="Practice Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("practice"))
            practicebutton.pack(pady=20)

            fullbutton = tk.Button(mainframe, text="Full Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("full"))
            fullbutton.pack(pady=20)

            weekdaybutton = tk.Button(mainframe, text="Weekday Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("weekday"))
            weekdaybutton.pack(pady=20)

            juniormemberbutton = tk.Button(mainframe, text="Junior Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("juniormember"))
            juniormemberbutton.pack(pady=20)

            intermediatebutton = tk.Button(mainframe, text="Intermediate Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("intermediate"))
            intermediatebutton.pack(pady=20)
        else:
            publicbutton = tk.Button(mainframe, text="Public Player", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("public"))
            publicbutton.pack(pady=20)

            vipbutton = tk.Button(mainframe, text="VIP", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("VIP"))
            vipbutton.pack(pady=20)

            associatebutton = tk.Button(mainframe, text="Associate", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("associate"))
            associatebutton.pack(pady=20)

            juniorbutton = tk.Button(mainframe, text="Junior", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("junior"))
            juniorbutton.pack(pady=20)

            practicebutton = tk.Button(mainframe, text="Practice Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("practice"))
            practicebutton.pack(pady=20)

            fullbutton = tk.Button(mainframe, text="Full Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("full"))
            fullbutton.pack(pady=20)

            weekdaybutton = tk.Button(mainframe, text="Weekday Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("weekday"))
            weekdaybutton.pack(pady=20)

            juniormemberbutton = tk.Button(mainframe, text="Junior Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("juniormember"))
            juniormemberbutton.pack(pady=20)

            intermediatebutton = tk.Button(mainframe, text="Intermediate Member", font=("Arial", 20), height=2, width=20, command=lambda: membershipselect("intermediate"))
            intermediatebutton.pack(pady=20)

def holesection():
    for widget in mainframe.winfo_children():
        widget.destroy()

    title = tk.Label(mainframe, text="Number of Holes Remaining", font=("Arial", 20))
    title.pack(pady=40)

    buttonframe = tk.Frame(mainframe)
    buttonframe.pack(pady=20)

    onebutton = tk.Button(buttonframe, text="1", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(1))
    onebutton.grid(row=0, column=0, padx=10, pady=10)

    twobutton = tk.Button(buttonframe, text="2", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(2))
    twobutton.grid(row=0, column=1, padx=10, pady=10)

    threebutton = tk.Button(buttonframe, text="3", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(3))
    threebutton.grid(row=0, column=2, padx=10, pady=10)

    fourbutton = tk.Button(buttonframe, text="4", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(4))
    fourbutton.grid(row=1, column=0, padx=10, pady=10)

    fivebutton = tk.Button(buttonframe, text="5", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(5))
    fivebutton.grid(row=1, column=1, padx=10, pady=10)

    sixbutton = tk.Button(buttonframe, text="6", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(6))
    sixbutton.grid(row=1, column=2, padx=10, pady=10)

    sevenbutton = tk.Button(buttonframe, text="7", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(7))
    sevenbutton.grid(row=2, column=0, padx=10, pady=10)

    eightbutton = tk.Button(buttonframe, text="8", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(8))
    eightbutton.grid(row=2, column=1, padx=10, pady=10)

    ninebutton = tk.Button(buttonframe, text="9", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(9))
    ninebutton.grid(row=2, column=2, padx=10, pady=10)

    tenbutton = tk.Button(buttonframe, text="10", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(10))
    tenbutton.grid(row=3, column=0, padx=10, pady=10)

    elevenbutton = tk.Button(buttonframe, text="11", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(11))
    elevenbutton.grid(row=3, column=1, padx=10, pady=10)

    twelvebutton = tk.Button(buttonframe, text="12", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(12))
    twelvebutton.grid(row=3, column=2, padx=10, pady=10)

    thirteenbutton = tk.Button(buttonframe, text="13", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(13))
    thirteenbutton.grid(row=4, column=0, padx=10, pady=10)

    fourteenbutton = tk.Button(buttonframe, text="14", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(14))
    fourteenbutton.grid(row=4, column=1, padx=10, pady=10)

    fifteenbutton = tk.Button(buttonframe, text="15", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(15))
    fifteenbutton.grid(row=4, column=2, padx=10, pady=10)

    sixteenbutton = tk.Button(buttonframe, text="16", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(16))
    sixteenbutton.grid(row=5, column=0, padx=10, pady=10)

    seventeenbutton = tk.Button(buttonframe, text="17", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(17))
    seventeenbutton.grid(row=5, column=1, padx=10, pady=10)

    eightteenbutton = tk.Button(buttonframe, text="18", font=("Arial", 20), height=2, width=20, command=lambda: holeselect(18))
    eightteenbutton.grid(row=5, column=2, padx=10, pady=10)

def methodsection():
    for widget in mainframe.winfo_children():
        widget.destroy()

    title = tk.Label(mainframe, text="Did they Walk/Ride/Pushcart", font=("Arial", 20))
    title.pack(pady=40)

seasonsection()
root.mainloop()