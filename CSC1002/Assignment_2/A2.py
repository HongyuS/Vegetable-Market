from bokeh.io import show, curdoc
from bokeh.models import widgets as wd, ColumnDataSource
from bokeh.layouts import widgetbox as wb, layout
from bokeh.core.properties import value
from bokeh.plotting import figure
from functools import partial
import string
import pymssql

sqlConn = None

def connectSQLServer():    # function to connect SQL server

    attr = dict(
        server = '10.20.213.10',
        database = 'csc1002',
        user = 'csc1002',
        password = 'csc1002',
        port = 1433,
        as_dict = True
    )

    try:
        return pymssql.connect(**attr)
    except Exception as e:
        print(e)
        quit()

sqlConn = connectSQLServer()

'''
def select():
    title = title_input.value
    tsql = "select * from lgu.course where title like %s"
    with sqlConn.cursor(as_dict=True) as cursor:
        cursor.execute(tsql, title)
        rows = cursor.fetchall()
        data = {}
        for row in rows:
            data['id'] = [row['course_id']]
            data['title'] = [row['title']]
            data['dept'] = [row['dept_name']]
            data['credit'] = [row['credits']]
            data['instructor'] = [row['instructor']]
    table.source.data = data

def selectDept(year, gpa):
    tsql = "select gpa, count(*) from lgu.student \
            where dept_name = \'English\' and year = {} and gpa = {}\
            group by gpa \
            order by gpa".format(year, gpa)
    with sqlConn.cursor(as_dict=True) as cursor:
        cursor.execute(tsql)
        rows = cursor.fetchall()
        data = {}
        for row in rows:
            print(row)
    # source = ColumnDataSource(data=data)

def onClick(idx):
    pass
'''

def dept_list():
    tsql = "select dept_name from lgu.student order by dept_name"
    with sqlConn.cursor(as_dict=True) as cursor:
        cursor.execute(tsql)
        rows = cursor.fetchall()
        l = []
        for row in rows:
            l.append(row['dept_name'])
        l = list(set(l))
    l.sort()
    return l

# Course Info
columns = [
    wd.TableColumn(field='id', title='Course ID'),
    wd.TableColumn(field='title', title='Title'),
    wd.TableColumn(field='dept', title='Department'),
    wd.TableColumn(field='credit', title='Credit'),
    wd.TableColumn(field='instructor', title='Instructor')
]
table = wd.DataTable(
    source = ColumnDataSource(),
    columns = columns,
    width = 800
)

paragraph = wd.Paragraph(text='option')
optionGroup = wd.RadioGroup(labels=['and', 'or'], active=0, width=100, inline=True)
btnGroupLetters = wd.RadioButtonGroup(labels=list(string.ascii_uppercase), active=-1)
title_input = wd.TextInput(title='Title:', value='', placeholder='contains....')
dept_input = wd.TextInput(title='Department:', value='', placeholder='contains....')
refresh = wd.Button(label='Refresh')
btnGroupTitle = wd.RadioButtonGroup(name='title',
    labels=['begins with...', '...contains...', '...ends with'], active=1)
btnGroupDept = wd.RadioButtonGroup(name='dept',
    labels=['begins with...', '...contains...', '...ends with'], active=1)

page_info = layout(
    [
        [wb(btnGroupLetters, width=1000)],
        [wb(btnGroupTitle), wb(btnGroupDept)],
        [wb(title_input), wb(paragraph, optionGroup, width=100), wb(dept_input)],
        [wb(refresh, width=100)],
        [wb(table)]
    ]
)

# Statistics
select_list = wd.Select(title='Department:', value='', options=dept_list())

colors = ['#c9d9d3', '#718dbf', '#e84d60']

gpa = ['A+', 'A', 'B+', 'B', 'C+', 'C','D+', 'D','F']
years = ['2015', '2016', '2017']

data = {}
data['gpa'] = gpa
data['2015'] = [2,8,4,3,6,2,8,4,9]
data['2016'] = [2,2,0,4,6,8,4,6,7]
data['2017'] = [6,7,4,7,8,5,8,9,0]

source = ColumnDataSource(data=data)

p = figure(x_range=gpa, plot_height=500, title='GPA Counts by Year',
    toolbar_location=None, tools='')
p.vbar_stack(years, x='gpa', width=0.9, color=colors, source=source,
    legend=[value(x) for x in years])

p.y_range.start = 0
p.y_range.end = 30
p.legend.location = 'top_right'

page_sta = layout([[wb(select_list), p]])

page1 = wd.Panel(child=page_info, title='Course Info')
page2 = wd.Panel(child=page_sta, title='Statistics')
tabs = wd.Tabs(tabs=[page1, page2])

# show(tabs)
curdoc().add_root(tabs)
