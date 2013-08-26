from IPython.display import display
from IPython.core.display import HTML
from pandas import DataFrame

def htprint(s):
	display(HTML(s))
	
def showT(data, rows=None):
	df = DataFrame(data)
	if rows:
		df = df[:rows]
	htprint(df.to_html())
	
def h(n, s):
	htprint('<h%d>%s</h%d>' % (n, s, n))
	
def hr():
	htprint('<hr>')
