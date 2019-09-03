# tower_job_events_log

docker build . -t mccbryan.ops/tower-to-li:v2

docker run -it  mccbryan.ops/tower-to-li:v2 -l liserver -t towerserver -j jobid -u admin -p password
