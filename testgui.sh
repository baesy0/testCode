#!/bin/sh
zenity --forms --title="Work notes" \
--text="오늘은 어떤 업무를 하셨나요?" \
--separator="," \
--add-calendar="Today" \
--add-entry="Name" \
--add-entry="Project" \
--add-entry="Note" >> worknote.csv

case $? in
	0)
		echo "done";;
	1)
		echo "cancel";;
	-1)
		echo "cancel";;
esac
