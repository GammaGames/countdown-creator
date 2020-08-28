# Countdown Creator

A simple python script to create simple timeanddate.com countdown urls. Configure events via the `config.yaml` file.

## Setup

Clone repository and install dependencies:

```sh
git clone https://github.com/GammaGames/countdown-creator.git
cd countdown-creator
pip3 install -r requirements.txt
```

## Use

Run command with python, event name is the only argument. Event name is not case sensitive.

```sh
python3 countdown.py SEUS
```
Output: https://www.timeanddate.com/countdown/to?msg=SEUS%20Deadline&p0=250&ud=1&year=2020&month=8&day=29&hour=23&min=59&sec=00
```sh
python3 countdown.py tt
```
Output: https://www.timeanddate.com/countdown/generic?msg=TT%20Deadline&p0=250&ud=1&year=2020&month=9&day=2&hour=18&min=59&sec=59

## Notes

The `timezone` config is taken from existing urls (`p0` parameter), I have no idea how they translate.
