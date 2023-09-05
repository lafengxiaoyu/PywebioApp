import logging
from datetime import datetime

from pywebio.input import *
from pywebio.output import *
from pywebio import start_server

team = ''
start_time = datetime.now()


def read_answer(n):
    content = open('answer.txt').readlines()
    return content[n].strip('\n').split(' ')


def input_data(trial_number):
    return input_group("Please input 4 digits as the password. This the %d time your tried" % trial_number, [
        input('1st', name='first', required=True),
        input('2nd', name='second', required=True),
        input('3rd', name='third', required=True),
        input('4th', name='fourth', required=True),
    ])


def btn_click():
    put_text(calculate_time())


def try_input(answer, data, trial_number):
    while (answer[0] != data['first'] or answer[1] != data['second'] or answer[2] != data['third']
            or answer[3] != data['fourth']):
        put_markdown('- Your %d try: `%s-%s-%s-%s`, is not correct. Please try again.' %
                     (trial_number, data['first'], data['second'], data['third'], data['fourth']))
        trial_number += 1
        put_button("How long we have taken already?", onclick=btn_click)
        data = input_data(trial_number)


def calculate_time():
    now = datetime.now()
    diff = now - start_time
    sec = int(diff.total_seconds())
    mins = int(sec / 60)
    sec -= 60 * mins
    return "You take %dm : %ds" % (mins, sec)


def main():
    global team
    team = input('Your team name', required=True)
    put_markdown('# Hi team %s! Welcome' % team)
    with use_scope('scope1'):
        put_button("Click to start", onclick=lambda: stage1())


def stage1():
    global start_time
    start_time = datetime.now()
    logging.info("start_time: %s" % start_time)
    with use_scope('scope1', clear=True):
        put_markdown('# This is the 1st Stage, you start at %s' % start_time.strftime("%H:%M:%S"))
    trial_number = 1
    data = input_data(trial_number)
    try_input(read_answer(0), data, trial_number)
    put_markdown('## Congratulations 💐💐!!! You passed the 1st stage. %s' % calculate_time())
    stage2()


def stage2():
    put_markdown('# This is the 2nd Stage')
    trial_number = 1
    data = input_data(trial_number)
    try_input(read_answer(1), data, trial_number)
    put_markdown('## Congratulations again 🎉🎉!!! You passed the 2nd stage. %s' % calculate_time())
    stage3()


def stage3():
    put_markdown('# Welcome to the 3rd Stage')
    trial_number = 1
    data = input_data(trial_number)
    try_input(read_answer(2), data, trial_number)
    toast('Congratulations team %s 🎁🎁' % team)
    put_markdown('## Congratulations!! You passed all the stages. %s' % calculate_time())
    img = open('congrats-7.gif', 'rb').read()
    put_image(img, width='500px')


if __name__ == '__main__':
    start_server(main, port=8080, debug=True,
                 remote_access=False)
