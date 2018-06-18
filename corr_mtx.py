def corrMtx(data, widget_width):
	'''
	Keep header/index field <= three characters or to keep <td>'s tight.
	'''

	
	### Value range to color hex map
	grade = [
		[-1.1, 		-1.0, 	'BA4340', -1],
		[-1.0, 		-0.7, 	'BA615F', -.7],
		[-0.7, 		-0.5, 	'BB807E', -.5],
		[-0.5, 		-0.3, 	'BC9E9D', -.3],
		[-0.3,  	0.3, 	'BDBDBD', 	0],
		[ 0.3,  	0.5, 	'9DA5BC',  .3],
		[ 0.5,  	0.7, 	'7E8DBB',  .5],
		[ 0.7,  	1.0, 	'5F75BA',  .7],
		[ 1.0,  	1.1, 	'405DBA',  1]
	]
	#  	lower limit,upper,	color,		label
	
	# See http://www.perbang.dk/rgbgradient/

	
	
	### Set sizes for <style> in proportion to widget width
	wrap_w = widget_width
	
	td_pad = wrap_w * 0.008
	
	
	circle_w_h = (wrap_w - len(data[0]) * td_pad * 2) / len(data[0])
	
	circle_line_h = circle_w_h
	
	circle_r = circle_w_h * 0.5
	
	table_font_s = circle_w_h * 0.4
	
	
	legend_td_w = wrap_w * 0.9 / len(grade)
	
	legend_line_h = circle_w_h * .66
		
	legend_font_s = legend_line_h * .2

	
	
	### CSS style scoped to div container	
	style = '''
	<style scoped>
		.corrMtx_wrap {
			width: %spx;
		}
		.corrTable {
			border-collapse: collapse;
			font-size: %spx;
		}
		.header {
			font-weight: bold;
			font-family: monospace;
			text-align: center;
		}
		.index {
			display: inline-block;
			transform: rotate(270deg);
			font-weight: bold;
			font-family: monospace;
			text-align: center;
		}
		td {
			padding: %spx;
			text-align: center;
			vertical-align: middle;
		}
		.circle {
			width: %spx;
			height: %spx;
			border-radius: %spx;
			line-height: %spx;
			text-align: center;
		}
		.labels {
			width: %spx;
			height: %spx;
			border-radius: 6px;
			background-color: #bfbfbf;
			line-height: %spx;
			text-align: center;
		}
		.legend {
			border-collapse: collapse;
			margin: auto;
			font-family: monospace;
			font-size: %spx;
			text-align: center;
		}
		.legend_td {
			width: %spx;
			padding: 0px;
			line-height: %spx;
			color: #fff;
		}
	</style>''' % (	wrap_w,			
					table_font_s,
					td_pad,
					circle_w_h,
					circle_w_h,
					circle_r,
					circle_line_h,
					circle_w_h,
					circle_w_h,
					circle_line_h,					
					legend_font_s,
					legend_td_w,
					legend_line_h
					)

					
	
	### Build the <table> <tr>'s
	trs = ''
	for r in data:
		trs += '''
		<tr>'''
		
		# Header <tr>
		if data.index(r) == 0:
			for d in r:
			
				# First <td> leave blank
				if r.index(d) == 0:
					trs += '''
			<td></td>'''
			
				else:
					trs += '''
			<td><div class='labels'><span class='header'>%s</span></div></td>''' % d
		
		# All other <tr>'s		
		else:
			for d in r:
			
				# Index column
				if r.index(d) == 0:
					trs += '''
			<td><div class='labels'><span class='index'>%s</span></div></td>''' % d
					
				# Data columns
				else:
					
					# For negative coefficients
					if d < 0:
						for g in grade:
							if g[0] < d <= g[1]:
								td = '''
			<td><div class='circle' style='background-color: #%s'></div></td>''' % g[2]
								break
							else:
								pass
					
					# Positive coefficients
					elif d >= 0:
						for g in grade:
							if g[0] <= d < g[1]:
								td = '''
			<td><div class='circle' style='background-color: #%s'></div></td>''' % g[2]
								break
							else:
								pass

					# For some unforeseen error
					else:
						td = '''
	<td><div class='circle' style='background-color: #fff'>ERR</div></td>'''
						
					trs += td
						
		trs += '''
		</tr>'''

		
		
	### Legend build
	# Iterate-add gradient colors with coefficient category labels
	tds = ''
	for r in grade:
		tds += '''
			<td class='legend_td' style='background-color: #%s'>%s</td>''' % (r[2], r[3])
			
	legend = '''
	<table class='legend'>
		<tr>%s
		</tr>
	</table>''' % tds
	
	
	
	### Putting it all together in <table> in <div> wrapper
	div_wrap = '''<div class='corrMtx_wrap'>%s
	<table class='corrTable'>%s
	</table><br>%s
</div>
''' % (style, trs, legend)



	### For testing, write file, otherwise return markup
	testing = True
	if testing:
		#print table
		with open('correlation-coefficient-matrix.html', 'w') as f:
			f.write(div_wrap)
	
	else:
		return div_wrap

	

### Example data


d = [
	['', 'A',			'B',			'C',	'D'],
	['A',	1.000000,	0.525361,	-0.948845,	0.009802],
	['B',	0.525361,	1.000000,	-0.789391,	0.011852],
	['C',	-0.948845,	-0.789391,	1.000000,	-0.303228],
	['D',	0.009802,	0.011852,	-0.303228,	1.000000]
	]



corrMtx(d,420)