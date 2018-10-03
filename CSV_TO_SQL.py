import sys

if len(sys.argv) != 4:
    print "Incorrect Syntax: python CSV_TO_SQL.py <input_csv_path> <table_name> <output_sql_name>\n Ex: python CSV_TO_SQL.py resources/CSU/Campuses.csv CAMPUSES CSU-build-CAMPUSES.sql"

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[3], 'w')

first_line = True

for line in input_file:
    if first_line:
        # If this is the first line, skip it
        first_line = False
        continue
    output_file.write("INSERT INTO %s VALUES(%s);\n" % (sys.argv[2], line.rstrip()))

input_file.close()
output_file.close()
