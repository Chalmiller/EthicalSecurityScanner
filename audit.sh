#!/bin/bash 
printf "Beginning execution of the lynis audit system check..."
  
sudo lynis audit system --quick 

# function for generating the text files associated with the different output of the script
# The suggested aspects of the output to pay attention to are:
#   - warnings, suggestions, installed_packages, available_shells
function generate_files () {
    printf "Generating $2 from script execution... \n"
    sudo cat /var/log/lynis-report.dat | grep $1 | sed -e "s/$1\[\]\=//g"
    sudo cat /var/log/lynis-report.dat | grep $1 | sed -e "s/$1\[\]\=//g" | cat > $2.txt 
    printf "To access the $2 output, please cite the text file in "$pwd" \n"
}

function change_permissions () {
    sudo chmod 755 $1
}
  
generate_files warning warnings
generate_files suggestion suggestions
generate_files installed_package packages
generate_files available_shell shells
  
change_permissions warnings.txt 
change_permissions suggestions.txt 
change_permissions packages.txt 
change_permissions shells.txt 
