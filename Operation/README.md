# Operation Assesments
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
