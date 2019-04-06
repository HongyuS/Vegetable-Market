from bokeh.models import widgets
from bokeh.io import show, curdoc
from bokeh.layouts import widgetbox

button = widgets.Button(label='Refresh')
username = widgets.TextInput(title='Name', placeholder='enter your name...')
school = widgets.Select(title='School', options=['SSE', 'SME', 'HSS'])

def onClick():
    print('hahaha')

def onUserNameChange(attr, old, new):
    print(attr, old, new)

def onSchoolChange(attr, old, new):
    print('school', old, new)

button.on_click(onClick)
username.on_change('value', onUserNameChange)
school.on_change('value', onSchoolChange)

# show(widgetbox(button, username, school))
curdoc().add_root(widgetbox(button, username, school))
