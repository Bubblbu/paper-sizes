import json
import os

with open("all_paper_sizes.json") as data_file:
    sizes = json.load(data_file)

priority = ["ISO paper sizes","North American sizes","ANSI paper sizes"]

def maketable(d, f):
    f.write("| Paper size | mm | inches | points |\n")
    f.write("| ---------- | :--: | :------: | :------: |\n")
    names = sorted(d.keys())
    for name in names:
        f.write("| {} | {} x {} | {} x {} | {} x {} |\n".format(name, d[name]['mm'][0],d[name]['mm'][1],
                                                             d[name]['inches'][0],d[name]['inches'][1],
                                                             d[name]['points'][0],d[name]['points'][1]))

with open("README.md", "w") as f:
	f.write("# paper-sizes\n")
	f.write("A quite extensive list of paper sizes in mm, inches and points.\n")

	for prior_cat in priority:
	    f.write("## {}\n".format(prior_cat))
	    maketable(sizes[prior_cat],f)

	for cat in sorted(sizes.keys()):
	    if cat not in priority:
	        f.write("## {}\n".format(cat))
	        maketable(sizes[cat],f)

	#f.write("Original source: [Paper sizes chart](http://resources.printhandbook.com/pages/paper-size-chart.php)\n")

	f.write(r'# License\n<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.')