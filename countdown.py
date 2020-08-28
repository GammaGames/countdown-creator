import datetime
import sys
import yaml
import time


def get_next_date(target):
    d = datetime.date.today()
    while d.weekday() != target:
        d += datetime.timedelta(1)

    return d


def format_url(event, theme, date, time):
    year, month, day = (date.year, date.month, date.day)
    hour, minute, second = [time[i: i + 2] for i in range(0, len(time), 2)]
    domain = "https://www.timeanddate.com"
    params = f"msg={event}%20Deadline&p0=250&ud=1&year={year}&month={month}&day={day}&hour={hour}&min={minute}&sec={second}"
    return f"{domain}/countdown/{theme}?{params}"


def main():
    if len(sys.argv) < 2:
        print("python3 countdown.py [event]")

    name = sys.argv[1].lower()
    event = None
    with open("config.yaml") as in_file:
        config = yaml.load(in_file.read(), Loader=yaml.SafeLoader)
        if name in config:
            event = config[name]

    print(
        format_url(
            name.upper(),
            event["theme"],
            get_next_date(time.strptime(event["day"], "%A").tm_wday),
            str(event["time"]).ljust(6, "0"),
        )
    )


if __name__ == "__main__":
    main()
