from IPython.display import display
from IPython.core.display import HTML
from pandas import DataFrame

def htprint(s):
	display(HTML(s))
	
def showT(data):
	htprint(DataFrame(data).to_html())
	
def h(n, s):
	htprint('<h%d>%s</h%d>' % (n, s, n))
