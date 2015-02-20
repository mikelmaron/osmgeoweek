#!/usr/bin/python

from sys import stdin
from dateutil.parser import parse
from datetime import timedelta

start_date = parse("2014-11-15 00:00:00")
end_date = parse("2014-11-22 00:00:00")
cur_date = start_date
file_date = end_date
interval = 6

before_1st_interval = True

print stdin.readline().strip("\r\n") #header

line = stdin.readline()

while cur_date <= end_date:

  while cur_date < file_date:
    
    if line == None or line.strip("\r\n") == "":
      file_date = end_date

    elif before_1st_interval == True:
      line_list = line.split(',')
      file_date = parse(line_list[0])
      file_count = line_list[1]
      print str(cur_date) + "," + "0"
      cur_date = cur_date + timedelta(hours=interval)
      #print "cur date: %s" % cur_date
      #print "file date: %s" % file_date
      
    else:
      line_list = line.split(',')
      file_date = parse(line_list[0])
      file_count = line_list[1]
      
      print str(cur_date) + "," + previous_file_count.strip("\r\n")
      cur_date = cur_date + timedelta(hours=interval)
      #print "cur date2: %s" % cur_date
      #print "file date2: %s" % file_date

  #print "cur date3: %s" % cur_date
  #print "file date3: %s" % file_date
  before_1st_interval = False
  print str(cur_date) + "," + file_count.strip("\r\n")

  previous_line = line
  previous_line_list = previous_line.split(',')
  previous_file_count = previous_line_list[1]

  try:

    line = stdin.readline()
    line_list = line.split(',')
    file_date = parse(line_list[0])
    file_count = line_list[1]
    cur_date = cur_date + timedelta(hours=interval)

  except IndexError:
    #print "all done"
    quit()

