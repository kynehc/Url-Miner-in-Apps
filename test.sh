echo "this is for test python on apk files"
starttime=`date +'%Y-%m-%d %H:%M:%S'`
echo "start time:"$starttime
path="apk/"
save="result/"
filenum=1
for file in $(ls $path)
do
    echo ""
    echo "start to analyze apk file "$filenum":" 
    echo $file
    python url.py $path$file > $save$file.log 2>&1
    echo "finished!" 
    let filenum++
done
echo ""
endtime=`date +'%Y-%m-%d %H:%M:%S'`
echo "end time:"$endtime
