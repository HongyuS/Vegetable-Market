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

def select(tsql="select * from lgu.course order by dept_name"):
    global table
    data = {}
    with sqlConn.cursor(as_dict=True) as cursor:
        cursor.execute(tsql)
        rows = cursor.fetchall()
        data['id'] = [row['course_id'] for row in rows]
        data['title'] = [row['title'] for row in rows]
        data['dept'] = [row['dept_name'] for row in rows]
        data['credit'] = [row['credits'] for row in rows]
        data['instructor'] = [row['instructor'] for row in rows]
    print(data)
    return data

def letterOnClick(idx):
    tsql = "select * from lgu.course \
            where title like \'{}%\' \
            order by dept_name".format(list(string.ascii_uppercase)[idx])
    table.source.data = select(tsql)

def titleOnClick(idx):
    if idx == 0:
        tsql = "select * from lgu.course \
                where title like \'{}%\' \
                order by dept_name".format(
                    title_input.value
                )
    elif idx == 1:
        tsql = "select * from lgu.course \
                where title like \'%{}%\' \
                order by dept_name".format(
                    title_input.value
                )
    else:
        tsql = "select * from lgu.course \
                where title like \'%{}\' \
                order by dept_name".format(
                    title_input.value
                )
    table.source.data = select(tsql)

def deptOnClick(idx):
    if idx == 0:
        tsql = "select * from lgu.course \
                where dept_name like \'{}%\'\
                order by dept_name".format(dept_input.value)
    elif idx == 1:
        tsql = "select * from lgu.course \
                where dept_name like \'%{}%\' \
                order by dept_name".format(dept_input.value)
    else:
        tsql = "select * from lgu.course \
                where dept_name like \'%{}\' \
                order by dept_name".format(dept_input.value)
    table.source.data = select(tsql)

def showPlot(attr, old, new):    # function to update plot when dept changes
    global gpa, data, years, p
    for year in years:
        tsql = "select gpa, count(gpa) as gpa_num from lgu.student \
                where dept_name = \'{}\' and year = {} \
                group by gpa".format(new, year)
        with sqlConn.cursor(as_dict=True) as cursor:
            cursor.execute(tsql)
            rows = cursor.fetchall()
            for d in rows:
                for i in range(len(rows)):
                    if d['gpa'] == gpa[i]:
                        data[str(year)][i] = d['gpa_num']
    source.data = data
    
def dept_list():    # function to get options of the dept selection on tab_2
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

sqlConn = connectSQLServer()

# +----------+ Course Info +----------+

columns = [
    wd.TableColumn(field='id', title='Course ID'),
    wd.TableColumn(field='title', title='Title'),
    wd.TableColumn(field='dept', title='Department'),
    wd.TableColumn(field='credit', title='Credit'),
    wd.TableColumn(field='instructor', title='Instructor')
]
table = wd.DataTable(
    source=ColumnDataSource(),
    columns=columns,
    width=800
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

# +----------+ Statistics +----------+

selectDept = wd.Select(title='Department:', value='', options=dept_list())

colors = ['#c9d9d3', '#718dbf', '#e84d60']
    
gpa = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
years = ['2015', '2016', '2017']
data = {}
data['gpa'] = gpa
data['2015'] = [0] * 9
data['2016'] = [0] * 9
data['2017'] = [0] * 9

source = ColumnDataSource(data=data)

p = figure(x_range=gpa, plot_height=500, title='GPA Counts by Year',
    toolbar_location=None, tools='')
p.vbar_stack(years, x='gpa', width=0.9, color=colors, source=source,
    legend=[value(x) for x in years])

p.y_range.start = 0
p.y_range.end = 30
p.legend.location = 'top_right'

page_sta = layout([[wb(selectDept), p]])

page1 = wd.Panel(child=page_info, title='Course Info')
page2 = wd.Panel(child=page_sta, title='Statistics')
tabs = wd.Tabs(tabs=[page1, page2])

btnGroupLetters.on_click(letterOnClick)
# btnGroupTitle.on_click(titleOnClick)
# btnGroupDept.on_click(deptOnClick)
selectDept.on_change('value', showPlot)

curdoc().add_root(tabs)