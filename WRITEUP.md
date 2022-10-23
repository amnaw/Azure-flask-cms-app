# Analysis of Azure Compute Resources

### Azure Virtual Machine:
- ##### Costs 
   -   some pricing options pay-as-you-go model (more flexible) and reserved instances (more cost-effective for long-term use), spot pricing (cost-effective if have low uptime and needs availability automation).
   -   VM prices differ based on the VM size and region.
- ##### Scalability 
   -  you can scale your Azure VMs using Azure virtual machine scale sets to easily and automatically scale and manage VM instances.
   -  resizing, you can scale the VM up or down by changing the VM size.
- ##### Availability 
   -   you can improve Azure VM using an availability set that is a logical grouping of the VMs instances within the data center that also provides redundancy.
   -   to protect your apps and data from the loss of a data center, Availability Zones, which is a physically separated zones, are used.
   -   you can also use a Load balancer to get the most application resiliency. It's used to distribute traffic between multiple virtual machines. 
- ##### Workflow 
   -   Azure VM is an IaaS solution, and that means you're responsible for setting and managing the whole infrastructure which may include:
          - Network Interface
          - Security Setup (Firewall, SSL Certificates)
          - Network (Virtual Network, Subnet, Network Security Group)
          - Public IP
          - DNS
          - Disk image 
          - OS and security updates and patches
          - Setting up the web server


### Azure App Service:
- ##### Costs 
   -   an App Service plan defines a set of computing resources for a web app to run in a specific region with additional details like : OS, No. of instances, size of VM, and pricing tier.
   -   the pricing tier of an App Service plan determines what App Service features you get and how much you pay for the plan.
- ##### Scalability 
   -   scale up your app service by getting more CPU, memory, disk space, and extra VMs or by changing the pricing tier of the App Service plan.
   -   scale out by increasing the number of VM instances that run your app.

- ##### Availability 
   -   you should have at least 2 instances of your App Service and use a multi-region architecture to provide higher availability with using Azure Front Door that pools two instances of a web application that run in different Azure regions.
   -   you can use Azure Traffic Manager (ATM) in front of your web apps to monitor your endpoints and provide automatic failover and reroute traffic to minimize downtime.

- ##### Workflow 
   - App Service is a PaaS solution, which is a fully managed platform that let the developers focus on application code and data.
   -   you can set up a CI CD pipeline with Azure DevOps, GitHub, BitBucket, Docker Hub, or Azure Container Registry. Promote updates through test and staging environments. 
   -   there are a few things you have to do to run an app service:
       -  specify the deployment source (Git Repository or local file deployment).
       -  deploy an app to the app service and set all configs.
       -  deploy your app to the App service.

   


 ***
 # The go-to Azure solution for our case
 ##### Azure App Service is the winner!
 - since my CMS flask application has a light workload and the app service is capable of processing power we need.
 - easier to build and configure.
 - allow me to focus on code and deployment configurations only.
 ##### Other considerations that make Azure Virtual Machine a better candidate:
- if we have some need to install certain programs or dependencies we would go for VM to gain more control over the OS.
- in case we have more resource-intensive apps VM is the best option here since compute power of Azure App Services is limited.
- if there are some security concerns or regulations that need to be met, we can achieve that using reserved VM instances.
   






