import os ,shutil ,re

datepattern = re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-
((19|20)\d\d)(.*?)$""", re.VERBOSE)

for amrfilename in os.listdir("."):
    mo = datepattern.search(amrfilename)

    if mo ==None:

        continue
    beforepart = mo.group(1)
    monthpart = mo.group(2)
    daypart = mo.group(4)
    yearpart = mo.group(6)
    afterpart = mo.group(8)
