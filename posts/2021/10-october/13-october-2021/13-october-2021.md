#### What's inside:

- [Overview](#overview)
 <br>

 Here you learn the basics of both Azure Firewall and Azure Firewall Manager. This overview should help you decide whether Azure Firewall and Azure Firewall Manager are a good fit with Contoso's network security strategy.

<br>
---

### Overview of Azure Firewall
Azure Firewall is a cloud-based security service that protects your Azure virtual network resources from incoming and outgoing threats. In the next few sections, you'll learn the fundamentals and key features of Azure Firewall.
<br>

### What is a firewall?
A firewall is a community safety characteristic that sits among a depended on community and an untrusted community, consisting of the internet. The firewall's process is to investigate all incoming and outgoing community site visitors. Based on that analysis, the firewall both permits the site visitors to byskip, or it denies the site visitors. Ideally, the firewall permits all valid site visitors whilst denying malicious site visitors consisting of malware and intrusion attempts.

By default, maximum firewalls deny all incoming and outgoing site visitors. When a firewall analyzes community site visitors, it tests for sure situations to be met earlier than it permits the site visitors to byskip through. Those situations might be a precise IP address, FQDN, community port, community protocol, or any combination.

Together, those situations outline a firewall rule. A firewall may have simplest a unmarried rule, however maximum firewalls are configured with many guidelines. Only community site visitors that meets the situations of the firewall's guidelines is permitted to byskip through.

Some firewalls are hardware-primarily based totally and are living interior gadgets which can be constructed to behave as firewalls. Other firewalls are software program applications that run on general-reason computing gadgets.
<br>

### What is Azure Firewall?

Azure Firewall is a cloud-based firewall service. In most configurations, Azure Firewall is provisioned inside a hub virtual network. Traffic to and from the spoke virtual networks and the on-premises network traverses the firewall with the hub network.

All traffic to and from the internet is denied by default. Traffic is only allowed if it passes various tests, such as the configured firewall rules.

![firewallrules](https://github.com/dikkyryan/daily-progress/blob/main/posts/2021/10-october/13-october-2021/1.png)
<br>

### What is Azure Firewall Premium?
Azure Firewall Premium provides advanced threat protection that meets the needs of highly sensitive and regulated environments, such as the payment and healthcare industries.

![firewallrules](https://github.com/dikkyryan/daily-progress/blob/main/posts/2021/10-october/13-october-2021/1.png)
<br>

### Overview of Azure Firewall Manager
Azure Firewall Manager provides a central point of configuration and management of multiple Azure Firewall instances. Azure Firewall Manager enables you to create one or more firewall policies and rapidly apply them to multiple firewalls.
<br>

##What is a firewall policy?
The configuration of a single Azure Firewall can be complicated. For example, the firewall might be configured with multiple rule collections. A collection is a combination of any or all of the following items:

	- One or more network address translation (NAT) rules
	- One or more network rules
	- One or more application rules
    
When you include other firewall settings such as custom DNS and threat intelligence rules, configuring just a single firewall can be a burden. Adding to that burden are two common network security scenarios:

	- Your network architectures require multiple firewalls.
	- You want each firewall to implement both a base level of security rules that apply to everyone, plus special rules for designated groups such as developers, database users, and the marketing department.
    
To simplify the complexity of managing these and similar firewall scenarios, you can implement firewall policies. A firewall policy is an Azure resource that contains one or more collections of NAT, network, and application rules, custom DNS settings, threat intelligence settings, and more.

The key point here is that Azure offers a resource called Firewall Policy. A firewall policy that you create is an instance of that resource. As a separate resource, you can rapidly apply the policy to multiple firewalls using Azure Firewall Manager. You can create one policy to be the base policy, then have more specialized policies inherit the base policy's rules.
<br>

### Architecture options
Azure Firewall Manager provides security management for the following two network architectures:

	- Hub virtual network. A standard Azure virtual network where one or more firewall policies have been applied.
	- Secured virtual hub. An Azure Virtual WAN Hub where one or more firewall policies have been applied.
<br>

### How Azure Firewall works
You're familiar with the basic features of both Azure Firewall and Azure Firewall Manager. Now let's examine how these technologies work to provide security for your Azure resources. This information will help you evaluate whether Azure Firewall is the right tool for Contoso's network security strategy.
<br>

### How Azure Firewall protects an Azure virtual network
    
To understand how Azure Firewall protects your virtual network, know that there are two key characteristics to any Azure Firewall deployment:

	- The firewall instance has a public IP address to which all inbound traffic is sent.
	- The firewall instance has a private IP address to which all outbound traffic is sent.

That is, all traffic—inbound and outbound—goes through the firewall. By default, the firewall denies access to everything. Your job is to configure the firewall with the conditions under which traffic is allowed through the firewall. Each condition is called a rule and each rule applies one or more checks on the data. Only traffic that passes every check in all the firewall's rules is allowed to pass through.

How Azure Firewall manages network traffic depends on where the traffic originates:

	- For allowed inbound traffic, Azure Firewall uses DNAT to translate the firewall's public IP address to the private IP address of the appropriate destination resource in the virtual network.
	- For allowed outbound traffic, Azure Firewall uses SNAT to translate the source IP address to the firewall's public IP address.
<br>

### Where Azure Firewall fits into a virtual network
For Azure Firewall to do its job effectively, you must set it up as a barrier between a trusted network you want to protect and an untrusted network that offers potential threats. Most commonly, you deploy Azure Firewall as a barrier between your Azure virtual network and the internet.

Azure Firewall is best deployed using a hub and spoke network topology with the following characteristics:

	- A virtual network that acts as the central connectivity point. This network is the hub virtual network.
	- One or more virtual networks that are peered to the hub. These peers are the spoke virtual networks and are used to provision workload servers.
	- You deploy the firewall instance in a subnet of the hub virtual network and then configure all inbound and outbound traffic to go through the firewall.

Use the following general steps to set up an instance of Azure Firewall:

	1. Create a hub virtual network that includes a subnet for the firewall deployment.
	2. Create the spoke virtual networks and their subnets and servers.
	3. Peer the hub and spoke networks.
	4. Deploy the firewall to the hub's subnet.
	5. For outbound traffic, create a default route that sends traffic from all subnets to the firewall's private IP address.
	6. Configure the firewall with rules to filter inbound and outbound traffic.
<br>

### When to use Azure Firewall
You know what Azure Firewall is and how it works. Now you need some criteria to help you evaluate whether Azure Firewall and Azure Firewall Manager are suitable choices for your company. To help you decide, let's consider the following scenarios:

	- You want to protect your network against infiltration.
	- You want to protect your network against user error.
	- Your business includes e-commerce or credit card payments.
	- You want to configure spoke-to-spoke connectivity.
	- You want to monitor incoming and outgoing traffic.
	- Your network requires multiple firewalls.
	- You want to implement hierarchical firewall policies.

As part of your evaluation of Azure Firewall and Azure Firewall Manager, you know that Contoso has faced several of these scenarios. Read the following corresponding sections for more details.
<br>

### You want to protect your network against infiltration
A common goal of many malicious actors is to infiltrate your network. These intruders might want to use your network resources or examine, steal, or destroy sensitive or proprietary data.

Azure Firewall is designed to help prevent such intrusions. For example, a malicious hacker might try to infiltrate the network by requesting access to a network resource. Azure Firewall uses stateful inspection of network packets to examine the context of such requests. If a request is a response to earlier legitimate activity, then the firewall will likely allow the request; if a request came seemingly out of nowhere-as would the request sent by a would-be infiltrator—then the firewall would deny the request.
<br>

### You want to protect your network against user error
Perhaps the most common method for infiltrating a network or installing malware on a network computer is to trick a network user into clicking a link in an email message. That link sends the user to a malicious hacker-controlled website that either installs the malware or tricks the user into entering network credentials.

Azure Firewall prevents such attacks by using threat intelligence to deny access to known malicious domains and IP addresses.
<br>

### Your business includes e-commerce or credit card payments
Does your business have an e-commerce component, or does it process online credit card payments? If so, then your company might have to comply with the Payment Card Industry Data Security Standard (PCI DSS). The PCI DSS is a set of security standards created and maintained by the PCI Security Standards Council. To achieve PCI compliance, the PCI DSS lists a dozen requirements. Here's the first requirement:

	- Install and maintain a firewall configuration to protect cardholder data.

The PCI DSS specifies that you need to set up a firewall configuration that restricts all inbound and outbound traffic from untrusted networks and hosts. The firewall must also deny all other traffic except for the protocols needed to process payment cards.
<br>
