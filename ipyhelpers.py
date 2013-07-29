htprint = lambda s: display(HTML(s))
showT = lambda _: htprint(DataFrame(_).to_html())
h = lambda n, s: htprint('<h%d>%s</h%d>' % (n, s, n))
