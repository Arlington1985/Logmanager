printDate() {
   echo `date +'%d/%m/%Y %H:%M:%S'`
}
        echo "`printDate`       START Archiving logs from $1 to $2"
        cd $1
        for i in `find *log* -mtime +$3`; do
                tar -cjf $2/$i.bz2 $i --remove-files
                if [ $? -eq 0 ]; then
                        echo "`printDate`       $i file was archived SUCCESSFULLY";
                else
                        echo "`printDate`       $i file archiving FAILED";
                fi
        done;
        echo "`printDate`       FINISH Archiving logs from $1 to $2"

echo "`printDate`    START moving files from $2 to tmp for LOGSTORE";
    cd $2
    if [ ! -d "tmp" ]; then
        mkdir tmp
        echo "`printDate`       tmp folder was created"
    fi
    for file in `find * -type f \( -name "*.gz" -o -name "*.bz2" \) -mtime +$4`
    do
        #lftp -e "cd $3; put $file; bye" -u "user,password" server1
        mv $file tmp/
        if [ $? -eq 0 ]; then
            echo "`printDate`    $file was moved to tmp SUCCESSFULLY";
            rm -f $file
            if [ $? -eq 0 ]; then
                echo "`printDate`    $file was removed SUCCESSFULLY";
            else
                echo "`printDate`    $file removing FAILED";
            fi
        else
            echo "`printDate`    $file moving FAILED";
        fi
    done;
    echo "`printDate`    FINISH Moving files from $2 to tmp for LOGSTORE";
