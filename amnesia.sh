echo "Amnesia Script | Clemens Dotson, 927961"
echo
echo "You're currently logged in as $(whoami) and are in the $(pwd) directory"
echo
echo -e "There's a total number of $(ls | wc -l) file(s) in the directory you're in...\n"
ls -a