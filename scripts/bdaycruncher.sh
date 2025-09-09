#!/bin/bash

echo "Zodiac Roast Generator"
echo "Enter birth month (1-12):"
read month
echo "Enter birth day (1-31):"
read day

echo "Your cosmic verdict..."

if [ $month -eq 3 ] && [ $day -ge 21 ] || [ $month -eq 4 ] && [ $day -le 19 ]; then
    echo "ARIES - Anger issues with legs"
elif [ $month -eq 4 ] && [ $day -ge 20 ] || [ $month -eq 5 ] && [ $day -le 20 ]; then
    echo "TAURUS - Argues with inanimate objects"
elif [ $month -eq 5 ] && [ $day -ge 21 ] || [ $month -eq 6 ] && [ $day -le 20 ]; then
    echo "GEMINI - Multiple personality discount"
elif [ $month -eq 6 ] && [ $day -ge 21 ] || [ $month -eq 7 ] && [ $day -le 22 ]; then
    echo "CANCER - Professional crybaby"
elif [ $month -eq 7 ] &&[ $day -ge 23 ] || [ $month -eq 8 ] && [ $day -le 22 ]; then
    echo "LEO - Main character syndrome"
elif [ $month -eq 8 ] && [ $day -ge 23 ] || [ $month -eq 9 ] && [ $day -le 22 ]; then
    echo "VIRGO - Judges your grammar silently"
elif [ $month -eq 9 ] && [$day -ge 23 ] || [ $month -eq 10 ] && [ $day -le 22 ]; then
    echo "LIBRA - Can't pick a restaurant"
elif [ $month -eq 10] && [ $day -ge 23 ] || [ $month -eq 11 ] && [ $day -le 21 ]; then
    echo "SCORPIO - Trust issues incarnate"
elif [ $month -eq 11 ] && [ $day -ge 22 ] || [ $month -eq 12 ] && [ $day -le 21 ]; then
    echo "SAGITTARIUS - Has 47 unfinished projects"
elif [ $month -eq 12 ] && [ $day -ge 22 ] || [ $month -eq 1 ] && [ $day -le 19 ]; then
    echo "CAPRICORN - Workaholic in denial"
elif [ $month -eq 1 ]&& [ $day -ge 20 ] || [ $month -eq 2 ] && [ $day -le 18 ]; then
    echo "AQUARIUS - Weird flex but okay"
elif [ $month -eq 2 ]&& [ $day -ge 19 ] || [ $month -eq 3 ] && [ $day -le 20 ]; then
    echo "PISCES - Lives in fantasy land"
else
    echo "Invalid date or alien birth"

echo "The stars have spoken!"
