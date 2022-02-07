room = {
    'CS101':'3004',
    'CS102':'4501',
    'CS103':'6755',
    'NT110':'1244',
    'CM241':'1411'
}
instructor = {
    'CS101':'Haynes',
    'CS102':'Alvarado',
    'CS103':'Rich',
    'NT110':'Burke',
    'CM241':'Lee'
}
time = {
    'CS101':'8:00a.m.',
    'CS102':'9:00a.m.',
    'CS103':'10:00a.m.',
    'NT110':'11:00a.m.',
    'CM241':'1:00p.m.'
}

course_number = 'CS102'

def info():
    print(room[course_number]),
    print(instructor[course_number]),
    print(time[course_number])

info()