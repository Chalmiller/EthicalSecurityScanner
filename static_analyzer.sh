#!/bin/bash 
printf "Beginning execution of the bandit static code analyzer..."

function change_permissions () {
    sudo chmod 755 $1
}

bandit -r . -f json -o bandit_report.json
change_permissions bandit_report.json
