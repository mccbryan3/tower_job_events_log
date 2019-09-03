# Tower_job_events_log

docker build . -t mccbryan.ops/tower-to-li:v2

docker run mccbryan.ops/tower-to-li:v2 -l liserver -t towerserver -j jobid -u admin -p password

# <h7> To see output

docker run -it mccbryan.ops/tower-to-li:v2 -l liserver -t towerserver -j jobid -u admin -p password

Script only spits out the output of the job events in json until uncommented
