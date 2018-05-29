#!/bin/bash
#Setting up alerts to notify System administrator if 
#a disk is running out of space or system load is going up
#or a process is stressing the memory.


#Disk Alert
kapacitor define disk_usage_alert -tick alerts/disk/disk_usage_percent.tick -dbrp "telegraf"."autogen" && kapacitor enable disk_usage_alert;

#Cpu Alerts
kapacitor define cpu_idle -tick alerts/cpu/cpu_idle.tick -dbrp "telegraf"."autogen" && kapacitor enable cpu_idle;
kapacitor define system_usage -tick alerts/cpu/system_usage.tick -dbrp "telegraf"."autogen" && kapacitor enable system_usage;
kapacitor define user_usage -tick alerts/cpu/user_usage.tick -dbrp "telegraf"."autogen" && kapacitor enable user_usage;

#Memory Alert
kapacitor define memory_usage -tick alerts/memory/memory_usage.tick -dbrp "telegraf"."autogen" && kapacitor enable memory_usage;

#System Alerts
kapacitor define load15_alert -tick alerts/system/load15.tick -dbrp "telegraf"."autogen" && kapacitor enable load15_alert;
kapacitor define load5_alert -tick alerts/system/load5.tick -dbrp "telegraf"."autogen" && kapacitor enable load5_alert;
kapacitor define load1_alert -tick alerts/system/load1.tick -dbrp "telegraf"."autogen" && kapacitor enable load1_alert;
