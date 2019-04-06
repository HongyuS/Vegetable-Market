from bokeh.io import show, curdoc
from bokeh.models import widgets as wd, ColumnDataSource
from bokeh.layouts import widgetbox as wb, layout
from bokeh.core.properties import value
from bokeh.plotting import figure
from functools import partial
import string
import pymssql

g_selectedDept = 'Accounting'
# g_selectedDept = ''

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

# def selectDept(dept, year, gpa):
#     tsql = "select gpa, count(*) from lgu.student \
#             where dept_name = {} and year = {} and gpa = {}\
#             group by gpa \
#             order by gpa".format(dept, year, gpa)
#     with sqlConn.cursor(as_dict=True) as cursor:
#         cursor.execute(tsql)
#         rows = cursor.fetchall()
#         data = {}
#         for row in rows:
#             data['gpa'] = [row['gpa']]
#         for gpa in 
#     source = ColumnDataSource(data=data)

def onClick(idx):
    pass

def onChange(attr, old, new):
    global g_selectedDept
    g_selectedDept = new

def count_gpa(year, sd=g_selectedDept):
    l = list()
    tsql = "select dept_name, gpa, year from lgu.student order by dept_name"
    with sqlConn.cursor(as_dict=True) as cursor:
        cursor.execute(tsql)
        rows = cursor.fetchall()
        for d in rows:
            if str(d['dept_name']) == sd and int(d['year']) == year:
                l.append(d['gpa'])
    a = b = c = d = e = f = g = h = i = 0
    for item in l:
        if item == 'A+': a += 1
        elif item == 'A': b += 1
        elif item == 'B+': c += 1
        elif item == 'B': d += 1
        elif item == 'C+': e += 1
        elif item == 'C': f += 1
        elif item == 'D+': g += 1
        elif item == 'D': h += 1
        elif item == 'F': i += 1
    return [a, b, c, d, e, f, g, h, i]

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

if __name__ == '__main__':
    sqlConn = connectSQLServer()
    
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
    selectDept = wd.Select(title='Department:', value='', options=dept_list())
    
    colors = ['#c9d9d3', '#718dbf', '#e84d60']
    
    GPA = ['A+', 'A', 'B+', 'B', 'C+', 'C','D+', 'D','F']
    years = ['2015', '2016', '2017']
    
    data = {}
    data['gpa'] = GPA
    selectDept.on_change('value', onChange)
    data['2015'] = count_gpa(2015)
    data['2016'] = count_gpa(2016)
    data['2017'] = count_gpa(2017)
    
    source = ColumnDataSource(data=data)
    
    p = figure(x_range=GPA, plot_height=500, title='GPA Counts by Year',
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
    
    refresh.on_click(onClick)
    
    # show(tabs)
    curdoc().add_root(tabs)

# bokeh serve --show A2.py