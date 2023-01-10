"""
Python script for downloading public records that have been uploaded individually on a GovQA portal.

For questions, contact Ethan Campbell at ethanchenbell@gmail.com.

Steps for using this on MacOS:
1. Download this script (see "Raw" button at top right of GitHub page).
2. Log into the public records portal and click on the active request. Save the webpage as an HTML ["Page Source"] file (in Safari, go to File > Save As; in Chrome, go to File > Save Page As > Webpage, HTML Only).
3. Paste the full filepath of that file inside the quote marks next to "page_source" below (example filled in). On MacOS, you can do this easily by right-clicking on the file, holding down Option, and clicking "Copy... as Pathname".
4. Enter the full filepath where you'd like the downloaded files to be saved next to "download_to" below.
5. Save changes to this script. Copy its full filepath.
6. Open Terminal. On the command line prompt, type "python <filepath>", where <filepath> is the location of this script. Hit enter to run.

"""

import os

page_source = '/Users/Ethan/Desktop/Page_source.html'
download_to = '/Users/Ethan/Desktop/'

# read page source
file = open(page_source,'r')
source = file.read()
file.close()

# process using spaces as delimiter
source_blocks = source.split()

# extract URLs
urls = []
for block in source_blocks:
  if block.startswith('value="https://'):
    block = block.lstrip('value="').rstrip('"').replace('amp;','')
    urls.append(block)

# download each file
os.chdir(download_to)
for url_idx, url in enumerate(urls):
  print('Downloading {0} of {1}...'.format(url_idx+1,len(urls)))
  os.system('curl -O -J "{0}"'.format(url))