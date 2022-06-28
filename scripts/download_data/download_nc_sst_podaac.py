#!/usr/bin/env python
# Script to download all .nc files from a THREDDS catalog directory
# Written by Sage 4/5/2016, revised 5/31/2018
  
from typing import Text
from xml.dom import minidom
from urllib.request import urlopen
from urllib.request import urlretrieve
  
# Divide the url you get from the data portal into two parts
# Everything before "catalog/"
period = ['2018']
server_url = "https://opendap.jpl.nasa.gov/opendap/allData/modis/L3/aqua/11um/v2019.0/4km/monthly/"
root_url = "https://opendap.jpl.nasa.gov/opendap"

# Everything after "catalog/"

# example from link above: tag_name = 'thredds:acess', já que é a linha que há o link p/ download da file;
# attribute_name = 'urlPath', já que é atributo da tag onde tem o link.

def get_elements(url, tag_name, attribute_name):
  """Get elements from an XML file""" 
  # usock = urllib2.urlopen(url)
  usock = urlopen(url)
  xmldoc = minidom.parse(usock)
  usock.close()
  tags = xmldoc.getElementsByTagName(tag_name)
  attributes=[]
  skip_duplicate = False
  for tag in tags:
    if skip_duplicate == True: # essa parte if etc é por conta de haver link de download duplicado.
      skip_duplicate = False
      continue
    attribute = tag.getAttribute(attribute_name)
    attributes.append(attribute)
    skip_duplicate = True
  return attributes

def main(year):
  url = server_url + year + '/catalog.xml'
  print(url)
  catalog = get_elements(url,'thredds:access','urlPath')
  count = 0
  for file_path in catalog:
    count +=1
    file_url = root_url + file_path
    
    file_prefix = file_url.split('/')[-1][:-3]
    file_extension = file_url.split('.')[-1]
    file_name = file_prefix + '_' + str(count) + "."+ file_extension
    print('Downloaing file %d of %d' % (count,len(catalog)))
    print(file_name)
    print(file_url)
    a = urlretrieve(file_url,file_name) # download file
    print(a)
 
# Run main function when in comand line mode        
if __name__ == '__main__':
  for year in period:
    main(year)