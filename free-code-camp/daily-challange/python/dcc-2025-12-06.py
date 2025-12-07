def format_date(date_string):
    months_to_numbers= {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

    date_string = date_string.split(" ")
    date_string[1]=date_string[1][:-1]
    y=date_string[-1]
    m=months_to_numbers[date_string[0]]
    d=date_string[1]
    if len(d)==1:
        d = "0"+d
    res_date = f"{y}-{m}-{d}" 
    print(res_date)
    return res_date


format_date("December 6, 2025")