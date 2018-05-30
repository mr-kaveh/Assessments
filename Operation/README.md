# Operation Assessments
In order to complete the Operation Problems,we will be Using Tick Stack which is a collection of products
from the developers of the time-series database InfluxDB. It is made up of the following components:
```
  -Telegraf collects time-series data from a variety of sources.
  -InfluxDB stores time-series data.
  -Chronograf visualizes and graphs the time-series data.
  -Kapacitor provides alerting and detects anomalies in time-series data.
```

each of these components separately, but if you use them together, you'll have a scalable, integrated 
open-source system for processing time-series data.The KEYWORDS of the problem #1 are database and 
access log and for the problem #2 it is simply Monitoring, and BINGO!!!
we are going to collect metrics from the system resources and services(webServer included) and make 
dashboards and graphs to monitor our system. let's first address the Problem #2.

# Problem #2

## Prerequisites

```
ansible 2.5
python 2.7
```

## Setting up Monitoring with Tick stack

The point is to have minimum Hand-ops, so i have used an ansible playbook to manage the configuration
as well as the installation of required packages.i am on centos 7 so, YUM will be our package manager.
the playbook will be played with the fillowing command:

```
# ansible-playbook -i "localhost," -c local playBook.yml
```

now we have all the required services to gather metrics from the System and visualize with Tick graphs.
you can access the Chronograf interface by visiting http://your_server_ip:8888 in your web browser.
the more specific address for the basic system metrics is http://your_server_ip:8888/sources/1/hosts/server_hostname .

tick enables us to create customized dashboards as well as numerous plugins that can be added to telegraf(the time-series data collector)
to help us monitor services like apache,nginx,mysql,docker,casandra,network interface traffic,.....

## Seting up Alerts with tick scripts

alerts directory contains scripts for setting up alerts based on resource thresholds. the scripts will be added and enabled 
with alertSetup.sh which automatically executes by playBook.yml

manage tasks(alerts) page 
```
http://your_server_ip:8888/sources/1/alert-rules
```
alerts are set to send to my email in my configuration, but it is possible to send them to your slack,telegram,.....

## Telegraf Plugins

There are more then 60 input plugins for Telegraf. It can gather metrics from many popular services and databases.it helps us
monitor a wide variaty of services on our development server and send specific reports for users and developers of an specific service.
in files/telegraf.d i have gathered few plugins which will gather data about nginx, apache, sysstat, net response,etc...
these plugins will be copied to /etc/telegraf during playBook.yml execution.

# Problem #1

so let's talk about influxdb which as it's name implies is a database system it has 3 main databases after playBook.yml execution
what we are going to work with, is telegraf database. you can enter influx database with following command:

```
# influx
```
or in our case with the following credentials:

```
influx -username 'hossein' -password 'hd@influx'
```
we mentioned telegraf plugins , they are tables in influxdb if type:
```
> use telegraf
```
and then 
```
> show measurements
```
you will see a list of system metrics in form of tables, which you can query.
creating a customized plugin as follows in /etc/telegraf/telegraf.d:

```
[[inputs.logparser]]
  ## files to tail.
  files = ["/var/log/nginx/access.log"]
  ## Read file from beginning.
  from_beginning = true
  ## Override the default measurement name, which would be "logparser_grok"
  name_override = "nginx_access_log"
  ## For parsing logstash-style "grok" patterns:
  [inputs.logparser.grok]
    patterns = ["%{COMBINED_LOG_FORMAT}"]

[[outputs.influxdb]]
  ## The full HTTP or UDP endpoint URL for your InfluxDB instance.
  urls = ["http://localhost:8086"] # required
  ## The target database for metrics (telegraf will create it if not exists).
  database = "telegraf" # required
  ## Write timeout (for the InfluxDB client), formatted as a string.
  timeout = "5s"
```
after adding the plugin, just restart telegraf service and check the status and 
nginx access log can be inserted into the influxdb every 10 seconds by telegraf and
problem #1 is completed as well.

## Testing the customized plugin
for testing the functionality of the customized telegraf plugin we can use the following command:
```
# telegraf --config /etc/telegraf/telegraf.d/customized_plugin.conf
```
this will assign our customized_plugin.conf as the main config file for telegraf temporarily and 
monitores nginx access log every 10 seconds and inserts the new line into the database. now if 
you login to influxdb and type in the following commands:
```
> use telegraf
> select * from nginx_access_log
```
you will see entries of /var/log/nginx/access.log as table rows.

## Useful Links

* (https://www.influxdata.com/blog/telegraf-correlate-log-metrics-data-performance-bottlenecks/) - Customized Plugin
* (https://github.com/influxdata/telegraf/tree/master/plugins/inputs/) - Telegraf Input Plugins