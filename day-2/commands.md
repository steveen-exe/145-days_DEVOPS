touch - can used to create backup files in production
cp - used to create backup ffiles in production before modification of current configs
mv - can be used for rotation of old files like old logs and all app.lof - app.old.log
rm - remove files
rm -r -> delete folder
rm -rf -> force delete
#Production engineers always verify the path before using rm -rf.

cat - read file contents


less - read large file contents
Space → next page
b     → previous page
/word → search
q     → quit

Reading a 5 GB log using cat is impractical.

wc - used  to count words
#out -> 1000 12000 85000 access.log
        Useful
        wc -l access.log    

history - search prev. commands
-> history | grep kubectl

