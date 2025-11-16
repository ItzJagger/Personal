import tkinter as tk
from tkinter import ttk

pricing = {
    "summer":{
        "weekday":{
            "before10":{
                "public": 110.00,
                "VIP": 90.00,
                "Associate": 100.00,
                "Junior": 110.00,
                "practice": 90.00,
                "Full": 0,
                "cart": 25.00,
                "cartmember": 22.12,
                "pushcart": 15.00
            },
            "10-1":{
                "public": 110.00,
                "VIP": 90.00,
                "Associate": 100.00,
                "Junior": 50.00,
                "practice": 90.00,
                "Full": 0,
                "cart": 25.00,
                "cartmember": 22.12,
                "pushcart": 15.00
            },
            "1-3":{
                "public": 100.00,
                "VIP": 80.00,
                "Associate": 90.00,
                "Junior": 50.00,
                "practice": 80.00,
                "Full": 0,
                "cart": 25.00,
                "cartmember": 22.12,
                "pushcart": 15.00
            },
            "3-4":{
                "public": 100.00,
                "VIP": 80.00,
                "Associate": 90.00,
                "Junior": 50.00,
                "practice": 80.00,
                "Full": 0,
                "cart": 15.00,
                "cartmember": 13.27,
                "pushcart": 7.50
            },
            "4-5":{
                "public": 75.00,
                "VIP": 55.00,
                "Associate": 65.00,
                "Junior": 50.00,
                "practice": 55.00,
                "Full": 0,
                "cart": 15.00,
                "cartmember": 13.27,
                "pushcart": 7.50
            },
            "5-close":{
                "public": 75.00,
                "VIP": 55.00,
                "Associate": 65.00,
                "Junior": 50.00,
                "Juniorwithadult": 0,
                "practice": 0,
                "Full": 0,
                "cart": 15.00,
                "cartmember": 13.27,
                "pushcart": 7.50
            }      
        },
        "friday":{
            "before10":{
                "public": 120.00,
                "VIP": 100.00,
                "Associate":110.00,
                "Junior":120.00,
                "Juniormember": 100.00,
                "practice": 100.00,
                "Full": 0,
                "cart":25.00,
                "cartmember":22.12,
                "pushcart":15.00
            },
            "10-11":{
                "public": 120.00,
                "VIP": 100.00,
                "Associate":110.00,
                "Junior":50.00,
                "Juniormember": 50.00,
                "practice": 100.00,
                "Full": 0,
                "cart":25.00,
                "cartmember":22.12,
                "pushcart":15.00 
            },
            "11-3":{
                "public": 110.00,
                "VIP": 90.00,
                "Associate":100.00,
                "Junior":50.00,
                "Juniormember": 0,
                "practice": 90.00,
                "Full": 0,
                "cart":25.00,
                "cartmember":22.12,
                "pushcart":15.00 
            },
            "3-4":{
                "public": 110.00,
                "VIP": 90.00,
                "Associate":100.00,
                "Junior":50.00,
                "Juniormember": 0,
                "practice": 90.00,
                "Full": 0,
                "cart":15.00,
                "cartmember":13.27,
                "pushcart": 7.50 
            },
            "4-5":{
                "public": 75.00,
                "VIP": 55.00,
                "Associate":65.00,
                "Junior":50.00,
                "Juniormember": 0,
                "practice": 55.00,
                "Full": 0,
                "cart":15.00,
                "cartmember":13.27,
                "pushcart": 7.50 
            },
            "5-close":{
                "public": 75.00,
                "VIP": 55.00,
                "Associate":65.00,
                "Junior":50.00,
                "Juniorwithadult":0,
                "Juniormember": 0,
                "practice": 0,
                "Full": 0,
                "cart":15.00,
                "cartmember":13.27,
                "pushcart": 7.50 
            }
        },
        "weekend/holiday":{
            "before10":{
                "public": 120.00,
                "VIP": 100.00,
                "Associate": 110.00,
                "Junior": 120.00,
                "Juniormember": 100.00,
                "Intermediate": 100.00,
                "Weekday": 100.00,
                "practice": 100.00,
                "Full": 0,
                "cart": 25.00,
                "cartmember": 22.12,
                "pushcart": 15.00
            },
            "10-11":{
                "public": 120.00,
                "VIP": 100.00,
                "Associate": 110.00,
                "Junior": 50.00,
                "Juniormember": 100.00,
                "Intermediate": 100.00,
                "Weekday": 100.00,
                "practice": 100.00,
                "Full": 0,
                "cart": 25.00,
                "cartmember": 22.12,
                "pushcart": 15.00
            },
            "11-3":{
                "public": 110.00,
                "VIP": 90.00,
                "Associate": 100.00,
                "Junior": 50.00,
                "Juniormember": 0.00,
                "Intermediate": 0.00,
                "Weekday": 90.00,
                "practice": 90.00,
                "Full": 0,
                "cart": 25.00,
                "cartmember": 22.12,
                "pushcart": 15.00
            },
            "3-4":{
                "public": 110.00,
                "VIP": 90.00,
                "Associate": 100.00,
                "Junior": 50.00,
                "Juniormember": 0.00,
                "Intermediate": 0.00,
                "Weekday": 90.00,
                "practice": 90.00,
                "Full": 0,
                "cart": 15.00,
                "cartmember": 13.27,
                "pushcart": 7.50
            },
            "4-5":{
                "public": 75.00,
                "VIP": 55.00,
                "Associate": 65.00,
                "Junior": 50.00,
                "Juniormember": 0.00,
                "Intermediate": 0.00,
                "Weekday": 55.00,
                "practice": 55.00,
                "Full": 0,
                "cart": 15.00,
                "cartmember": 13.27,
                "pushcart": 7.50
            },
            "5-close":{
                "public": 75.00,
                "VIP": 55.00,
                "Associate": 65.00,
                "Junior": 50.00,
                "Juniorwithadult":0,
                "Juniormember": 0.00,
                "Intermediate": 0.00,
                "Weekday": 55.00,
                "practice": 0.00,
                "Full": 0,
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
                "Associate": 89.00,
                "Junior": 99.00,
                "Practice": 79.00,
                "Full": 0,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "10-1":{
                "public": 99.00,
                "VIP": 79.00,
                "Associate": 89.00,
                "Junior": 50.00,
                "Practice": 79.00,
                "Full": 0,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "1-2":{
                "public": 99.00,
                "VIP": 79.00,
                "Associate": 89.00,
                "Junior": 50.00,
                "Practice": 79.00,
                "Full": 0,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50,
            },
            "2-3":{
               "public": 65.00,
                "VIP": 45.00,
                "Associate": 55.00,
                "Junior": 50.00,
                "Practice": 45.00,
                "Full": 0,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50, 
            },
            "3-close":{
                "public": 65.00,
                "VIP": 45.00,
                "Associate": 55.00,
                "Junior": 50.00,
                "Juniorwithadult": 0,
                "Practice": 0.00,
                "Full": 0,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50, 
            }
        },
        "friday":{
            "before10":{
                "public": 99.00,
                "VIP": 79.00,
                "Associate": 89.00,
                "Junior": 99.00,
                "Juniormember": 79.00,
                "Practice": 79.00,
                "Full": 0,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "10-11":{
                "public": 99.00,
                "VIP": 79.00,
                "Associate": 89.00,
                "Junior": 50.00,
                "Juniormember": 50.00,
                "Practice": 79.00,
                "Full": 0,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "11-1":{
                "public": 99.00,
                "VIP": 79.00,
                "Associate": 89.00,
                "Junior": 50.00,
                "Juniormember": 0.00,
                "Practice": 79.00,
                "Full": 0,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "1-2":{
                "public": 99.00,
                "VIP": 79.00,
                "Associate": 89.00,
                "Junior": 50.00,
                "Juniormember": 0.00,
                "Practice": 79.00,
                "Full": 0,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50,
            },
            "2-3":{
                "public": 65.00,
                "VIP": 45.00,
                "Associate": 55.00,
                "Junior": 50.00,
                "Juniormember": 0,
                "Practice": 45.00,
                "Full": 0,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50, 
            },
            "3-close":{
                "public": 65.00,
                "VIP": 45.00,
                "Associate": 55.00,
                "Junior": 50.00,
                "Juniorwithadult": 0,
                "Juniormember": 0,
                "Practice": 0.00,
                "Full": 0,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50, 
            }
        },
        "weekend/holiday":{
            "before10":{
                "public": 99.00,
                "VIP": 79.00,
                "Associate": 89.00,
                "Junior": 99.00,
                "Juniormember": 79.00,
                "intermediate": 79.00,
                "Practice": 79.00,
                "Full": 0,
                "weekday": 79.00,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "10-11":{
                "public": 99.00,
                "VIP": 79.00,
                "Associate": 89.00,
                "Junior": 50.00,
                "Juniormember": 79.00,
                "intermediate": 79.00,
                "Practice": 79.00,
                "Full": 0,
                "weekday": 79.00,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "11-1":{
                "public": 99.00,
                "VIP": 79.00,
                "Associate": 89.00,
                "Junior": 50.00,
                "Juniormember": 0.00,
                "intermediate": 0.00,
                "Practice": 79.00,
                "Full": 0,
                "weekday": 79.00,
                "cart": 20.00,
                "cartmember":17.70,
                "pushcart": 15.00,
            },
            "1-2":{
                "public": 99.00,
                "VIP": 79.00,
                "Associate": 89.00,
                "Junior": 50.00,
                "Juniormember": 0.00,
                "intermediate": 0.00,
                "Practice": 79.00,
                "Full": 0,
                "weekday": 79.00,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50,
            },
            "2-3":{
                "public": 65.00,
                "VIP": 45.00,
                "Associate": 55.00,
                "Junior": 50.00,
                "Juniormember": 0,
                "intermediate": 0,
                "Practice": 45.00,
                "Full": 0,
                "weekday": 45.00,
                "cart": 10.00,
                "cartmember":8.85,
                "pushcart": 7.50, 
            },
            "3-close":{
                "public": 65.00,
                "VIP": 45.00,
                "Associate": 55.00,
                "Junior": 50.00,
                "Juniormember": 0,
                "Juniorwithadult":0,
                "intermediate": 0,
                "Practice": 0.00,
                "Full": 0,
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
            before10button = tk.Button(mainframe, text="Before 10 AM", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("before10"))
            before10button.pack(pady=20)

            tento1button = tk.Button(mainframe, text="10AM - 12:50PM", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("10-1"))
            tento1button.pack(pady=20)

            oneto3button = tk.Button(mainframe, text="1PM - 2:50PM", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("1-3"))
            oneto3button.pack(pady=20)

            threeto4button = tk.Button(mainframe, text="3PM - 3:50PM", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("3-4"))
            threeto4button.pack(pady=20)

            fourto5button = tk.Button(mainframe, text="4PM - 4:50PM", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("4-5"))
            fourto5button.pack(pady=20)

            fivetoclosebutton = tk.Button(mainframe, text="After 5PM", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("5-close"))
            fivetoclosebutton.pack(pady=20)
        elif appstate["whatday"] == "friday":
            before10button = tk.Button(mainframe, text="Before 10 AM", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("before10"))
            before10button.pack(pady=20)

            tento11button = tk.Button(mainframe, text="10AM - 10:50AM", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("10-11"))
            tento11button.pack(pady=20)

            elevento3button = tk.Button(mainframe, text="11AM - 2:50PM", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("11-3"))
            elevento3button.pack(pady=20)

            threeto4button = tk.Button(mainframe, text="3PM - 3:50PM", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("3-4"))
            threeto4button.pack(pady=20)

            fourto5button = tk.Button(mainframe, text="4PM - 4:50PM", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("4-5"))
            fourto5button.pack(pady=20)

            fivetoclosebutton = tk.Button(mainframe, text="After 5PM", font=("Arial", 20), height=2, width=20, command=lambda: dayselect("5-close"))
            fivetoclosebutton.pack(pady=20)
        else:
            pass
    else:
        if appstate["whatday"] == "weekday":
            pass
        elif appstate["whatday"] == "friday":
            pass
        else:
            pass


seasonsection()
root.mainloop()