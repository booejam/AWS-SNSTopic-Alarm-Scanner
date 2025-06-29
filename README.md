A lightweight Python script that scans your AWS environment to identify which CloudWatch Alarms are configured to trigger a specific SNS (Simple Notification Service) topic.

**DESCRIPTION**

`sns-alarm-scanner` is an automation tool that helps monitor the connection between CloudWatch alarms and SNS topics. It eliminates the need for manual inspection by programmatically scanning all CloudWatch alarms and checking which ones are linked to a given SNS topic.

**🛠️ WHAT PROBLEM DOES IT SOLVES**

In complex AWS environments, it's common to lose track of which alarms are connected to which notification channels. This can lead to:

- **Orphaned SNS topics** – not triggered by any alarms  
- **Unmonitored alarms** – no alerts when issues occur  
- **Security gaps** – alarms that silently fail to notify  
- **Operational confusion** – during audits and incident reviews  

**This tool provides a quick and automated way to:**

- 🔍 Map CloudWatch alarms to SNS topics  
- 📊 Identify misconfigured or unused notification paths  
- ✅ Support compliance and operational monitoring hygiene 
