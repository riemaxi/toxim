cat import/protein.sergio.csv | awk -F ',' '{print toupper($2)}' | grep -v -e '^$' | awk '/^[0-9]/ {print $0}' | sort -u 
