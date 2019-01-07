#die_visual.py
import pygal
from die import Die

die_1 = Die()
die_2 = Die()
frenquencys = []
results = []
hist = pygal.SolidGauge(half_pie=True, inner_radius=0.70,
    style=pygal.style.styles['default'](value_font_size=10))
percent_formatter = lambda x: '{:.10g}'.format(x)
hist._value_format = percent_formatter
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
max_sides = die_1.num_sides + die_2.num_sides

for value in range(1,max_sides+1):
    frenquency = results.count(value)
    frenquencys.append(frenquency)    

for value in range(len(frenquencys)):
    hist.add(str(value+1),[{'value':frenquencys[value], "max_value":max(frenquencys)}])

hist.title = "Result of rolling one D"+ str(die_1.num_sides)  + " 10000 times."
    
hist.render_to_file("die_visual.svg")