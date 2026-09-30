# Job Portal Search Keywords

Source: `data/resumes/Roles & Skills.pdf` (cleaned: typos fixed, synonyms merged).

Core skills = listed in 2+ roles in that category (ranked). Boolean queries work on LinkedIn, Indeed, Dice, and Google Jobs.

## IT Support (22 roles)

**Search titles:** IT Support Technician, Technical Support Engineer, Desktop Support Technician, IT Services Specialist, Service Desk Specialist, Desktop Analyst, Reception & IT Support Coordinator, Help Desk Analyst, Technical Support Specialist, IT Technician, Helpdesk Support Specialist, Help Desk Technician, IT Support Specialist, IT Technical Support Administrator, IT Coordinator, Junior IT Support Technician, IT Asset Management Coordinator, Deskside Technician, Customer Technical Support, Computer Field Service Technician, IT Support Analyst

**Core skills:** Windows, Microsoft Office, Ticketing, Troubleshooting, DNS, Microsoft 365, Outlook, Computer hardware, Email, IT support, LAN, Linux, macOS

**All skills:** Windows, Microsoft Office, Ticketing, Troubleshooting, DNS, Microsoft 365, Outlook, Computer hardware, Email, IT support, LAN, Linux, macOS, Active Directory, Android, Customer service, DHCP, Google Workspace, Intune, iOS, MDM, OneDrive, Printers, SCCM, TCP/IP, VPN, WAN

**Boolean query:**

```
("IT Support" OR "Help Desk" OR "Service Desk" OR "Desktop Support" OR "Technical Support") AND (Windows OR "Active Directory" OR "Microsoft 365" OR Intune OR SCCM OR ticketing OR DNS OR macOS)
```

## SAP (24 roles)

**Search titles:** SAP Data Architect, SAP HCM Mini Master Consultant, SAP OneSource Consultant, SAP Plant Maintenance Consultant, SAP EWM Architect, SAP FI-GL Consultant, SAP MDG Material Master Consultant, Buyer, Credit & Accounts Receivable Specialist, Reporting Tools Administrator, SAP Functional Analyst, Production Planner, Packaging Components Controller, SAP PP/QM Consultant, SAP BTP Architect, Procurement Agent, SAP S/4HANA MM Functional & GxP Consultant, SAP Credit Specialist, SAP PaPM Lead Consultant, SAP Technical Lead, SAP Business Process & IT Controls Sr Associate, Order Management Specialist (SAP/GHX/EDI), Supply Management Specialist, SAP Project Administrator

**Core skills:** SAP, SAP S/4HANA, Excel, SAP ECC, Mini Master, MRP, PeopleSoft, Power BI, SAP HCM, SAP MM, SAP QM

**All skills:** SAP, SAP S/4HANA, Excel, SAP ECC, Mini Master, MRP, PeopleSoft, Power BI, SAP HCM, SAP MM, SAP QM, Agile, BDC, BOMs, Data analysis, EDI, Enterprise data modeling, General Ledger, GHX, GxP, Inventory planning, LSMW, Master data, Pivot tables, PowerPoint, Production workflows, SAP ABAP, SAP Activate, SAP Ariba, SAP BTP, SAP BusinessObjects, SAP BW/4HANA, SAP ERP, SAP EWM, SAP FI, SAP FI-AR, SAP GRC, SAP integration, SAP MDG, SAP MDM, SAP OM, SAP PaPM, SAP PM, SAP PP, SAP SD, SAP transactions, SAP WM, SQL, Supply chain, Tableau, UAT, Waterfall, Windows, Word

**Boolean query:**

```
(SAP) AND ("S/4HANA" OR ECC OR "SAP MM" OR "SAP SD" OR "SAP FI" OR "SAP PP" OR "SAP QM" OR ABAP)
```

## Data Center Technician (11 roles)

**Search titles:** Data Center Administrator, Data Center Technician, Data Center Technical Operations Engineer, Data Center Floating Technician, Data Center Technician II, Data Center Server Support Specialist, Data Center Facilities Technician Level 2, Critical Facility Lead - AI Data Center, Entry Level Data Center Technician, AI Data Center Project Engineer, Data Center Operations Technician

**Core skills:** UPS, HVAC, PDUs, Cable testing, Cooling systems, Excel, Fiber optics, Outlook, Power distribution, Servers, Structured cabling, Word

**All skills:** UPS, HVAC, PDUs, Cable testing, Cooling systems, Excel, Fiber optics, Outlook, Power distribution, Servers, Structured cabling, Word, AI workloads, Chillers, Cooling towers, CRAH, Ethernet, Generators, Hardware installation, OTDR, RTU, ServiceNow, Troubleshooting, Windows

**Boolean query:**

```
("Data Center Technician" OR "Data Center Operations" OR "Critical Facilities") AND (UPS OR HVAC OR PDU OR "structured cabling" OR fiber OR servers OR generators OR cooling)
```

## Network Technician (24 roles)

**Search titles:** NOC Technician, 3rd Shift Network Technician, Junior Network Technician, Network Technician, Telecom Engineer, Customer Service NOC Tech, Network Administrator, IT Network Analyst, VoIP Technician, GCP Network Engineer (Contract W2), Network Engineer, Network Support Specialist, Jr. Network Application Engineer, Network Technician - Dispatch, Field Network Technician, Network Communication Technician I, Network Technician I, Network Technician - Tier 2, SCADA Network Specialist, Network Installation Technician, Junior VoIP Administrator, MSP System Admin / Network Admin III, Firewall Engineer, Intermediate Network Administrator

**Core skills:** Routing, Switching, TCP/IP, LAN, DNS, WAN, VLANs, VPN, DHCP, Firewalls, VoIP, OSPF, BGP, HTTP, IP subnetting, SIP, Wi-Fi

**All skills:** Routing, Switching, TCP/IP, LAN, DNS, WAN, VLANs, VPN, DHCP, Firewalls, VoIP, OSPF, BGP, HTTP, IP subnetting, SIP, Wi-Fi, Active Directory, Bash, BMC Remedy, Email, Excel, GCP, Linux, Microsoft 365, Network analysis, Outlook, PBX, PoE, QoS, RTMP, SD-WAN, ServiceNow, Ticketing, Troubleshooting, Word

**Boolean query:**

```
("Network Technician" OR "Network Administrator" OR "Network Engineer" OR "NOC Technician") AND ("TCP/IP" OR VLAN OR routing OR switching OR firewall OR VPN OR OSPF OR BGP)
```

## System Administrator (10 roles)

**Search titles:** IT Systems Administrator, Junior Systems Administrator, IT Systems Engineer, Systems Administrator, Senior Systems & Network Administrator, IT System Administrator, Systems Administrator (MSP), Systems Administrator - DevOps, Infrastructure Administrator, IT Operations Analyst

**Core skills:** Microsoft 365, DNS, Windows, AWS, Azure, DHCP, Linux, PowerShell, Ticketing

**All skills:** Microsoft 365, DNS, Windows, AWS, Azure, DHCP, Linux, PowerShell, Ticketing, Active Directory, ALM, AutoCAD, Computer hardware, Customer service, ERP systems, Kernel programming, LAN, Network hardware, Servers, Troubleshooting, UNIX, Virtualization, VPN, WAN

**Boolean query:**

```
("Systems Administrator" OR "System Administrator" OR "Infrastructure Administrator" OR "IT Systems Engineer") AND ("Active Directory" OR PowerShell OR "Microsoft 365" OR Azure OR AWS OR Linux OR virtualization OR DNS)
```

## ERP (10 roles)

**Search titles:** Supply Chain Associate, Accounts Payable Specialist, ERP Applications & Project Lead, ERP Analyst, Sales Order Entry Administrator, ERP System Administrator, Enterprise Systems Administrator, Order Entry Representative, Accounts Payable Admin Associate, Sales Order Processor

**Core skills:** ERP systems, Microsoft Office, Workflows

**All skills:** ERP systems, Microsoft Office, Workflows, Accounts receivable, BOMs, Chart of accounts, Finance, General Ledger, NetSuite, Procure to pay, Purchase orders, SOPs, TCP/IP, Troubleshooting, Word

**Boolean query:**

```
(ERP OR "Order Entry" OR "Accounts Payable" OR "Sales Order") AND (NetSuite OR "general ledger" OR "accounts receivable" OR "procure to pay" OR "purchase order" OR "bill of materials")
```

## Lab Technician (10 roles)

**Search titles:** Laboratory Technician I, Lab Technician, Lab Associate, Entry Level Lab Technician I, Lab Technician / Clerk, Laboratory Technician (General), Engineering Laboratory Technician, Lab Service Technician, Associate Laboratory Technician, Medical Laboratory Technician

**Core skills:** QA/QC, Data entry, Excel, Laboratory testing, Power tools, Sample preparation, SOPs, Word

**All skills:** QA/QC, Data entry, Excel, Laboratory testing, Power tools, Sample preparation, SOPs, Word, Analytical instruments, Computer hardware, Data collection, DDR memory, Documentation, Electrical systems, Forklift, GMP, Google Workspace, Jira, Lab equipment troubleshooting, Lab operations, Laboratory science, Linux, Mechanical systems, MSDS, Multimeters, Outlook, PDUs, PowerPoint, Report writing, Troubleshooting, Windows

**Boolean query:**

```
("Lab Technician" OR "Laboratory Technician" OR "Lab Associate") AND ("sample preparation" OR GMP OR "QA/QC" OR SOP OR "laboratory testing" OR "analytical instruments" OR MSDS)
```

## Digital Marketing (10 roles)

**Search titles:** Social Media Intern, PR / Social Media Assistant, Digital Marketing Coordinator, Virtual Assistant (Contract), Web Maintenance & Digital Marketing (PT), Marketing & Communications Assistant, Marketing & Communications Intern, Marketing & Communications Specialist (PT), Viral Marketing Intern, Social Media Marketing Specialist

**Core skills:** Digital marketing, Advertising, Social media marketing

**All skills:** Digital marketing, Advertising, Social media marketing, Adobe Creative Suite, Canva, CapCut, Editing, Email marketing, Facebook, Final Cut Pro, Google Analytics, Graphic design, Instagram, Internet culture, LinkedIn, Premiere Pro, X/Twitter

**Boolean query:**

```
("Digital Marketing" OR "Social Media" OR "Marketing Communications") AND ("social media" OR "Google Analytics" OR Canva OR "Adobe Creative Suite" OR "Premiere Pro" OR CapCut OR "email marketing")
```

## Test Technician (5 roles)

**Search titles:** Computer Hardware Technician & Tester, Final Integration & Test Technician, Materials Testing Technician, Test Technician, Test Technician 1

**Core skills:** Excel, Test equipment, Troubleshooting, Word

**All skills:** Excel, Test equipment, Troubleshooting, Word, Automation sensors, Computer hardware, ESD handling, Functional testing, ISO 9000, Multimeters, Networking, Optical systems, Oscilloscopes, PowerPoint, Product testing, Quality lab, Reporting, Sample preparation, Teams, Test automation, Test plans, Visio

**Boolean query:**

```
("Test Technician" OR "Hardware Tester" OR "Testing Technician") AND (oscilloscope OR multimeter OR "test plans" OR "functional testing" OR "test automation" OR ESD OR "ISO 9000")
```

## Project Coordinator (10 roles)

**Search titles:** Project Support Specialist, Project Coordinator, Technical Project Coordinator (Enterprise IT), Project Development Coordinator, Associate IT Project Manager, Project Management Coordinator, Entry Level Project Management, IT Project Coordinator, Project Coordinator - System Implementation, Project Coordinator, Portfolio Management

**Core skills:** Excel, Jira, Smartsheet, Microsoft Office, PowerPoint, Word

**All skills:** Excel, Jira, Smartsheet, Microsoft Office, PowerPoint, Word, Adobe Acrobat, Adobe Creative Suite, Bluebeam, CAD, CRM, ERP systems, Monday.com, MS Project, Newforma, Outlook, PMP, Power BI, SAP, ServiceNow, SharePoint, Tableau, Teams, UAT, Workflow tools, Zoom

**Boolean query:**

```
("Project Coordinator" OR "Project Support" OR "IT Project Manager") AND (Jira OR Smartsheet OR "MS Project" OR ServiceNow OR SharePoint OR Monday.com OR "Power BI" OR PMP)
```

## Marketing Coordinator (10 roles)

**Search titles:** Marketing Coordinator, Marketing Specialist, Marketing Assistant, Entry Level Marketing, Marketing Events Coordinator, Field Marketing Associate, Affiliate Marketing Account Coordinator, Marketing & Member Relations, Content & Social Media Specialist, Hotel Digital Marketing Operations Associate

**Core skills:** Microsoft Office, Adobe Creative Suite, Excel, Canva, Word

**All skills:** Microsoft Office, Adobe Creative Suite, Excel, Canva, Word, Campaigns, ClickUp, CMS, Coupa, CRM, Customer engagement, Cvent, DocuSign, Domo, Dropbox, Email marketing, Figma, Google Analytics, Graphic design, HubSpot, Marketing tools, Marketo, Outlook, PowerPoint, Product training, Qualtrics, Salesforce

**Boolean query:**

```
("Marketing Coordinator" OR "Marketing Specialist" OR "Marketing Assistant") AND (Canva OR Adobe OR HubSpot OR Salesforce OR Marketo OR Figma OR "Google Analytics" OR "email marketing")
```

## CRM Support Specialist (10 roles)

**Search titles:** Client Success Specialist, GTM Operations Coordinator, Customer Experience Specialist, Customer Support Specialist, Customer Service Representative, Customer Relations Specialist, Customer Service Coordinator, Client Support Specialist, Customer Success Associate, CRM Specialist

**Core skills:** CRM, Excel, HubSpot, SLA, Word, Outlook

**All skills:** CRM, Excel, HubSpot, SLA, Word, Outlook, CRM dashboards, Customer retention, Customer satisfaction, Customer service, Documentation, Dynamics 365 Business Central, ERP systems, Google Sheets, Google Workspace, Microsoft Office, Record keeping, Salesforce, Ticketing, Trellus

**Boolean query:**

```
("CRM Specialist" OR "Customer Success" OR "Customer Support" OR "Client Support") AND (CRM OR HubSpot OR Salesforce OR SLA OR ticketing OR "Dynamics 365")
```

## Embedded Software (10 roles)

**Search titles:** Software Engineer - Embedded Platform, Control Engineer, Controls Engineer 2, Embedded Software Control Systems Engineer, Mechatronics Engineer, HIL Engineer, R&D Embedded Design Engineer, Firmware Software Engineer, Hardware Test Integration Program Engineer, Electrical Engineer

**Core skills:** C, C++, Linux, CAD, MATLAB, PCB, PLC, Simulink, SPI, Troubleshooting, UART

**All skills:** C, C++, Linux, CAD, MATLAB, PCB, PLC, Simulink, SPI, Troubleshooting, UART, BOMs, CAN bus, Control system design, Data analysis, Embedded Linux, Embedded system testing, Ethernet, Gerrit, Git, HIL testing, IndiCom, LabVIEW, Microsoft Office, Python, Qt, Root cause analysis, RTOS, SIL testing, System validation, Ubuntu, Windows

**Boolean query:**

```
("Embedded Software Engineer" OR "Firmware Engineer" OR "Controls Engineer" OR "HIL Engineer") AND (C++ OR "embedded C" OR RTOS OR "embedded Linux" OR MATLAB OR Simulink OR UART OR SPI)
```

## Validation Technician (10 roles)

**Search titles:** Associate Validation Technician, Validation Technician, Commissioning Validation Specialist, Quality Assurance Technician, Quality Control Technician, Quality Technician, Quality Control Coordinator, Quality Control Analyst, Internal Quality Control Technician, Manufacturing Technician

**Core skills:** Excel, GMP, SOPs, Computer skills, FAI, Good Documentation Practices, PowerPoint, QA/QC, Word

**All skills:** Excel, GMP, SOPs, Computer skills, FAI, Good Documentation Practices, PowerPoint, QA/QC, Word, ATP testing, Calibration, CAPA, CMM, Data acquisition, Electronics, ERP systems, HVAC, Multimeters, NCRs, Outlook, Precision measurement tools, Quality audits, Test data analysis, Troubleshooting, Validation protocol execution

**Boolean query:**

```
("Validation Technician" OR "Quality Control Technician" OR "Quality Assurance Technician" OR "Quality Technician") AND (GMP OR cGMP OR SOP OR CAPA OR FAI OR calibration OR "validation protocol" OR "good documentation practices")
```

## Logistics Specialist (10 roles)

**Search titles:** Inventory Control Clerk II, Sea Logistics Pricing Specialist, Logistics Solutions Specialist, Logistics Clerk, Logistics Associate, Supply Chain Tech, Data Center Logistics Associate L1, Data Center Logistics Associate, Import/Export Forwarding Associate, Logistics Coordinator

**Core skills:** Computer skills, Excel, Microsoft Office, Warehouse operations

**All skills:** Computer skills, Excel, Microsoft Office, Warehouse operations, Accounting basics, Cables, Customer service, Data entry, Email, FIFO, Inventory management, Invoice coding, Logistics databases, Math skills, MS Access, Problem solving, Servers, Switches, Windows, Word

**Boolean query:**

```
("Logistics Specialist" OR "Logistics Coordinator" OR "Logistics Associate" OR "Inventory Control") AND (inventory OR warehouse OR FIFO OR "MS Access" OR shipping OR freight)
```

## Telecom Support Technician (5 roles)

**Search titles:** Retail Support Specialist, IT Operations & Service Coordinator, Call Center Sales & Business Development Agent (Verizon), Telecommunications Analyst, Voice Engineer / Contact Center Support (CCaaS)

**Core skills:** Customer service

**All skills:** Customer service, Call routing, CCaaS, CRM, Five9, IVR, Microsoft 365, Radio communication, SIP, SOPs, Ticketing, Voice processing, Voicemail systems, Wireless communication

**Boolean query:**

```
("Telecom Technician" OR Telecommunications OR "Voice Engineer" OR "Contact Center") AND (VoIP OR SIP OR Five9 OR IVR OR CCaaS OR "call routing" OR wireless OR PBX)
```

## Lab Assistant (7 roles)

**Search titles:** Lab Assistant, Entry Level Specimen Processor, Lab Associate, Lab Assistant (Accessioner), Clinical Lab Assistant, Medical Laboratory Assistant, Laboratory Assistant I/II

**Core skills:** Specimen processing, LIS, Data entry

**All skills:** Specimen processing, LIS, Data entry, Computer skills, Lab procedures, Microsoft Office, Record keeping, Sample preparation, Specimen collection, Waived testing

**Boolean query:**

```
("Lab Assistant" OR "Laboratory Assistant" OR "Specimen Processor" OR Accessioner) AND ("specimen processing" OR LIS OR accessioning OR "specimen collection" OR "waived testing" OR "data entry")
```

## Debug Technician (10 roles)

**Search titles:** Process Technician, Test Technician, Automation Technician, Repair Technician (2nd Shift), Engineering Lab Technician - Electrical Test & Calibration, Electronic Debug Technician, Service Technician, Manufacturing Technician, Technician, Maintenance Technician

**Core skills:** Oscilloscopes, PCB, Multimeters, Excel, Troubleshooting, Word

**All skills:** Oscilloscopes, PCB, Multimeters, Excel, Troubleshooting, Word, AC/DC converters, Analog circuits, BOMs, Calipers, Control circuits, Data entry, Digital circuits, Electrical systems, Injection molding, IPC standards, Low-voltage electrical systems, Mechanical systems, Micrometers, Microprocessors, Microsoft Copilot, Microsoft Office, PLC, Power tools, QA/QC, RF

**Boolean query:**

```
("Debug Technician" OR "Electronics Technician" OR "Test Technician" OR "Repair Technician") AND (oscilloscope OR multimeter OR PCB OR RF OR IPC OR analog OR "digital circuits" OR PLC)
```

## Supply Chain Coordinator (10 roles)

**Search titles:** Logistics Coordinator, Supply Chain Technician, Shipping Coordinator, Senior Coordinator, Supply Chain, Supply Chain Assistant, Global Procurement Coordinator, Supply Chain Technical Coordinator, Inventory Coordinator, DC Coordinator, Workflow Coordinator

**Core skills:** Inventory management, Excel, ERP systems, Microsoft Office, Word

**All skills:** Inventory management, Excel, ERP systems, Microsoft Office, Word, Data entry, FIFO, KPI reporting, Logistics, LTL freight, Materials management, Microsoft 365, Operations, Outlook, PowerPoint, RMA, SAP, WMS

**Boolean query:**

```
("Supply Chain Coordinator" OR "Inventory Coordinator" OR "Procurement Coordinator" OR "Shipping Coordinator") AND (inventory OR ERP OR SAP OR WMS OR LTL OR FIFO OR RMA OR procurement)
```

## Database Admin (bucket list) (5 roles)

**Search titles:** Database Administrator, SQL Developer & Analyst, Database Admin, IBM i, SharePoint Administrator, Donor Database Specialist

**Core skills:** -

**All skills:** C#, Crystal Reports, DBMS, ERP systems, IBM i, Microsoft 365, Microsoft Office, MySQL, PostgreSQL, Raiser's Edge NXT, SharePoint, SQL Server, Stored procedures, T-SQL, Triggers, Views, Windows, Windows Server

**Boolean query:**

```
("Database Administrator" OR "SQL Developer" OR DBA) AND (MySQL OR PostgreSQL OR "SQL Server" OR "T-SQL" OR "stored procedures" OR "IBM i" OR "Crystal Reports")
```

## PL/SQL Developer (bucket list) (5 roles)

**Search titles:** Reporting Analyst, Teradata ETL Developer, Assistant Database Specialist, Programmer, Application Analyst

**Core skills:** SQL

**All skills:** SQL, C++, ETL, Excel, QA/QC, QlikView, RDBMS, SQL Server, SymXchange, Tableau, Teradata, UAT, UNIX

**Boolean query:**

```
("PL/SQL Developer" OR "SQL Developer" OR "ETL Developer" OR "Reporting Analyst") AND (SQL OR "PL/SQL" OR Teradata OR ETL OR "SQL Server" OR Tableau OR QlikView)
```

## Unix/Linux Admin (bucket list) (5 roles)

**Search titles:** NOC Systems Administrator, Linux, Operations Engineer, Linux / AIX SME, Linux Administration (Contract), Linux System Administrator / Engineer - Financial Services

**Core skills:** Linux, AWS, Patch management, VMware

**All skills:** Linux, AWS, Patch management, VMware, AIX, Debian, Oracle SQL, Perl, Rack and stack, RHEL, ServiceNow, Shell scripting, SOPs, Splunk, Troubleshooting

**Boolean query:**

```
("Linux Administrator" OR "Linux Engineer" OR "Unix Administrator" OR "Linux System Administrator") AND (RHEL OR Debian OR AIX OR VMware OR Splunk OR "shell scripting" OR "patch management" OR AWS)
```

## Where to search

**Staffing agencies:** TEKsystems, Randstad, Apex Systems, Robert Half, Kforce

**Startup job boards:** Y Combinator (Work at a Startup), Wellfound, Stealth startup

**Flagged as fake sites in the PDF (avoid):** Remote Hunter, Adzuna, Lensa, Talent Ally, Wira, Horizontal Talent, Jobright
