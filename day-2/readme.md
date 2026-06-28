today's obejctive is to learn manipulate files like a real production engineer

this commands can be used in daily debugging servers

Today's commanda are ->

touch: create empty files |
    in productionapplication generate logs you may need to create empty files while testing.

cp : copyfiles - cp <src> <dest>
Production use:
Before modifying
nginx.conf
create backup
cp nginx.conf nginx.conf.bak
mv 
rm
cat
less
wc
history


mv --

move or rename files  - can be used to rotate logs
mv app.log app.log.old

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

