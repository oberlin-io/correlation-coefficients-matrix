# Correlation Coefficient Matrix
Visualization of each variable pair's coefficient. Dark blue represents a strong, positive correlation. Dark red represents a strong, inverse correlation.

## Input
An array with header row of labels and index column of labels. And the desired width of the widget, in pixels, as an integer.

### Example Data
The correlation coefficients used in the example:

	['',	'A',		'B',		'C',		'D'],
	['A',	1.000000,	0.525361,	-0.948845,	0.009802],
	['B',	0.525361,	1.000000,	-0.789391,	0.011852],
	['C',	-0.948845,	-0.789391,	1.000000,	-0.303228],
	['D',	0.009802,	0.011852,	-0.303228,	1.000000]

## Output
An HTML <div> block that contains a <style> and two <table>'s blocks.