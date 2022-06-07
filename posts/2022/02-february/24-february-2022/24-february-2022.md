#### Connect Azure assets to Microsoft Defender for Cloud 

- [Introduction](#introduction)

Resource protection in Microsoft Defender for Cloud can be automatically configured with autoprovisioning or may be manually deployed.

You are a Security Operations Analyst working at a company that is implementing cloud workload protection with Microsoft Defender for Cloud. Your job is to ensure Defender for Cloud automatically protects the Azure resources.

Your organization has a few Azure virtual machines that are not part of the autoprovisioning scheme. You must manually configure protection for these Azure resources.

Learn how to connect your various Azure assets to Microsoft Defender for Cloud to detect threats.

### Explore and manage your resources with asset inventory
The asset inventory page of Microsoft Defender for Cloud provides a single page for viewing the security posture of the resources you've connected to Defender for Cloud.

Defender for Cloud periodically analyzes the security state of your Azure resources to identify potential security vulnerabilities. It then provides you with recommendations on how to remediate those vulnerabilities.

When any resource has outstanding recommendations, they'll appear in the inventory.

Use this view and its filters to address such questions as:

	- Which of my subscriptions with Microsoft Defender for Cloud enabled have outstanding recommendations?

	- Which of my machines with the tag 'Production' are missing the Log Analytics agent?

	- How many of my machines tagged with a specific tag have outstanding recommendations?

	- How many resources in a specific resource group have security findings from a vulnerability assessment service?

The asset management possibilities for this tool are substantial and continue to grow.

### Key features of asset inventory

The inventory page provides the following tools:

	=> Summaries - Before you define any filters, a prominent strip of values at the top of the inventory view shows:

		- Total resources: The total number of resources connected to Defender for Cloud.

		- Unhealthy resources: Resources with active security recommendations. Learn more about security recommendations.

		- Unmonitored resources: Resources with agent monitoring issues - they have the Log Analytics agent deployed, but the agent isn't sending data or has other health issues.

	=> Filters - The multiple filters at the top of the page provide a way to quickly refine the list of resources according to the question you're trying to answer. For example, if you wanted to answer the question: Which of my machines with the tag 'Production' are missing the Log Analytics agent?

	=> As soon as you've applied filters, the summary values are updated to relate to the query results.

	=> Export options - Inventory provides the option to export the results of your selected filter options to a CSV file. You can also export the query itself to Azure Resource Graph Explorer to further refine, save, or modify the Kusto Query Language (KQL) query.

	=> Asset management options - Inventory lets you perform complex discovery queries. When you've found the resources that match your queries, inventory provides shortcuts for operations such as:

		- Assign tags to the filtered resources - select the checkboxes alongside the resources you want to tag.

		- Onboard new servers to Defender for Cloud - use the Add non-Azure servers toolbar button.

		- Automate workloads with Azure Logic Apps - use the Trigger Logic App button to run a logic app on one or more resources. Your logic apps have to be prepared in advance and accept the relevant trigger type (HTTP request).

### How does asset inventory work?

Asset inventory utilizes Azure Resource Graph (ARG), an Azure service that provides the ability to query Defender for Cloud's security posture data across multiple subscriptions. ARG is designed to provide efficient resource exploration with the ability to query at scale. Using the Kusto Query Language (KQL), asset inventory can quickly produce deep insights by cross-referencing ASC data with other resource properties.

### How to use asset inventory

	- From Defender for Cloud's sidebar, select Inventory.

	- Use the Filter by name box to display a specific resource, or use the filters as described below.

	- Select the relevant options in the filters to create the specific query you want to perform.

	- To use the Security findings contain filter, enter free text from the ID, security check, or CVE name of a vulnerability finding to filter to the affected resources:

<br>
<img src="https://github.com/dikkyryan/daily-progress/blob/main/posts/2022/24-february/24-february-2022/1.jpg?raw=true" />
<br>
<br>

	- To use the Defender for Cloud filter, select one or more options (Off, On, or Partial):

		=> Off - Resources that aren't protected by a Defender for Cloud plan. You can right-click on any of these and upgrade them:

		=> On - Resources that are protected by a Defender for Cloud plan

		=> Partial - This applies to subscriptions that have some but not all of the Defender for Cloud plans disabled.

### Configure auto provisioning

Microsoft Defender for Cloud collects data from your Azure virtual machines (VMs), virtual machine scale sets, IaaS containers, and non-Azure (including on-premises) machines to monitor for security vulnerabilities and threats.

Data collection is required to provide visibility into missing updates, misconfigured OS security settings, endpoint protection status, and health and threat protection. Data collection is only needed for compute resources (VMs, virtual machine scale sets, IaaS containers, and non-Azure computers). You can benefit from Defender for Cloud even if you don’t provision agents; however, you will have limited security, and the capabilities listed above are not supported.

Data is collected using:

	- The Log Analytics agent, which reads various security-related configurations and event logs from the machine and copies the data to your workspace for analysis. Examples of such data are operating system type and version, operating system logs (Windows event logs), running processes, machine name, IP addresses, and logged in user.

	- Security extensions, such as the Azure Policy Add-on for Kubernetes, which can also provide data to Security Center regarding specialized resource types.
<br>
<img src="https://github.com/dikkyryan/daily-progress/blob/main/posts/2022/24-february/24-february-2022/2.jpg?raw=true" />
<br>
<br>

### Why use auto provisioning?
Any of the agents and extensions described on this page can be installed manually. However, auto provisioning reduces management overhead by installing all required agents and extensions on existing - and new - machines to ensure faster security coverage for all supported resources.

### How does auto provisioning work?
Defender for Clouds's auto provisioning settings has a toggle for each type of supported extension. When you enable auto provisioning of an extension, you assign the appropriate Deploy if not exists policy to ensure that the extension is provisioned on all existing and future resources of that type.