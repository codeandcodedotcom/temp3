# mocks.py
# 12 demo cases: 4 x (Score < 40, no doc), 4 x (Score ≥ 40 & PAR), 4 x (Score ≥ 40 & PILM)
# The "responses" keys match EXACTLY the questions in questions.json.

LOW_SCORE = [
    {
        "id": "brief_low_01",
        "product_answer": "no",
        "total_score": 16,  # < 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "Yes",
            "Can you specify your Project Type / Capability": "IT Program Management",
            "Is your project Product related?": "No",
            "What is your expected budget?": "Less 1 million",
            "What is the current ERL* for the project?": "7+",
            "Is the project government or military funded?": "No",
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "Rolls-Royce has substantial expertise in this area, with established development and standardisation.",
            "How is the overall stability of the project?":
                "Very high - the business case is well defined and clear.",
            "What is the status of the cross-functional project team?":
                "The resources are engaged via capability owners.",
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Few (less than 5).",
            "To what extent do project risks reach?":
                "No significant areas of concern have been identified.",
            "The advancement of the project is approved and governed at:":
                "Department level (CEO -3).",
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Focus is limited to internal customers, with scope restricted to the local business.",
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "No reputational concerns or risks identified.",
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders are highly aligned; there are few stakeholders with limited influence.",
            "How many partners or contractors are actively involved in the project?":
                "No partners or contractors are involved.",
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "None - No core supply chain entities are directly managed.",
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "1 division/function, 1 site, 1 first language",
        },
        "sections": {
            "Project Name": "Internal Process Optimisation",
            "Project Sponsor": "Priya Desai",
            "Project Description": (
                "Optimise Finance and HR approvals using a lightweight workflow engine to reduce manual steps, "
                "improve handoffs and strengthen audit trails. The project will pilot streamlined processes in one "
                "department before limited rollout. ERP changes are minimal, with quick training for staff and simple "
                "reporting to monitor impact. Description focuses on efficiency without large-scale system integration."
            ),
            "Risks": [
                "Resistance from staff to adopt new SOPs and workflows may delay adoption.",
                "Connector reliability issues may lead to occasional disruptions in workflow routing.",
                "Data inconsistencies in HR and Finance systems could create bottlenecks."
            ],
            "Assumptions": [
                "ERP and HRIS systems remain stable throughout the project timeline.",
                "SMEs are available for requirements validation and user testing.",
                "Funding remains approved for the pilot and small-scale rollout."
            ],
            "Benefits": [
                "Reduced approval cycle times evidenced through reporting metrics.",
                "Improved compliance and auditability with standardised approvals.",
                "Simplified workflows reduce staff workload and increase transparency."
            ],
        },
    },
    {
        "id": "brief_low_02",
        "product_answer": "yes",
        "total_score": 24,  # < 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "No",
            "Can you specify your Project Type / Capability": "Technical Program Management",
            "Is your project Product related?": "Yes",
            "What is your expected budget?": "Less 1 million",
            "What is the current ERL* for the project?": "<5",
            "Is the project government or military funded?": "No",
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "Rolls-Royce is familiar with this area and sees it as an opportunity for improvement and growth.",
            "How is the overall stability of the project?":
                "High - the business case is established with limited risks.",
            "What is the status of the cross-functional project team?":
                "Bulk resources are available in 5 Year Plan but not committed by capability owners.",
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Few (less than 5).",
            "To what extent do project risks reach?":
                "Risks are limited to local or domestic matters that are easily managed.",
            "The advancement of the project is approved and governed at:":
                "Department level (CEO -3).",
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Focus is limited to internal customers, with scope restricted to the local business.",
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Limited reputational concerns or risks identified, all easily manageable.",
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders are moderately aligned; there are multiple stakeholders with limited influence.",
            "How many partners or contractors are actively involved in the project?":
                "A small group (1-2) of partners or contractors are involved.",
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "1-3 - A small number of core supply chain entities are directly managed.",
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, 1 first language",
        },
        "sections": {
            "Project Name": "HR Onboarding Streamline",
            "Project Sponsor": "Robert Martinez",
            "Project Description": (
                "Streamline HR onboarding with checklists, basic single sign-on, and automated notifications. "
                "Focus is on reducing duplicate data entry, clarifying role ownership, and improving visibility "
                "of onboarding tasks. The change scope is small and limited to HR. Implementation uses existing tools "
                "with minor configurations and requires minimal training."
            ),
            "Risks": [
                "HR staff may resist new procedures, preferring manual workarounds.",
                "Unclear task ownership across HR and IT may cause delays.",
                "System downtime during implementation could affect onboarding timelines."
            ],
            "Assumptions": [
                "Single sign-on services are already available in the environment.",
                "No major HR system upgrades are scheduled during rollout.",
                "Business leadership supports the quick pilot with resourcing."
            ],
            "Benefits": [
                "Faster onboarding and reduced lead times for new hires.",
                "Lower rework from missed steps or inconsistent processes.",
                "Increased visibility of onboarding progress for managers."
            ],
        },
    },
    {
        "id": "brief_low_03",
        "product_answer": "no",
        "total_score": 30,  # < 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "Yes",
            "Can you specify your Project Type / Capability": "Infrastructure Projects",
            "Is your project Product related?": "No",
            "What is your expected budget?": "Between 2-10 million",
            "What is the current ERL* for the project?": "<5",
            "Is the project government or military funded?": "No",
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "Rolls-Royce has substantial expertise in this area, with established development and standardisation.",
            "How is the overall stability of the project?":
                "High - the business case is established with limited risks.",
            "What is the status of the cross-functional project team?":
                "The resources are engaged via capability owners.",
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Several (5 to 9).",
            "To what extent do project risks reach?":
                "Risks are limited to local or domestic matters that are easily managed.",
            "The advancement of the project is approved and governed at:":
                "Business level (CEO -2).",
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Focus is limited to internal customers, with scope restricted to the local business.",
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Limited reputational concerns or risks identified, all easily manageable.",
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders are moderately aligned; there are multiple stakeholders with limited influence.",
            "How many partners or contractors are actively involved in the project?":
                "A small group (1-2) of partners or contractors are involved.",
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "1-3 - A small number of core supply chain entities are directly managed.",
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, 1 first language",
        },
        "sections": {
            "Project Name": "Procurement Approval Cleanup",
            "Project Sponsor": "Alice Johnson",
            "Project Description": (
                "Rationalise procurement approval paths by removing redundant steps and aligning thresholds with policy. "
                "The initiative will deliver a standardised request form, automated notifications, and clearer audit trails. "
                "This lightweight project is short in duration, focuses on approvals efficiency, and avoids major ERP changes."
            ),
            "Risks": [
                "Complex policy exceptions may complicate workflow design.",
                "Stakeholder disagreements on approval thresholds could delay implementation.",
                "Limited IT resources may extend the timeline."
            ],
            "Assumptions": [
                "Procurement policies and thresholds remain unchanged during the project.",
                "Approvers are available for workshops and validation sessions.",
                "Current IT infrastructure supports additional workflow rules."
            ],
            "Benefits": [
                "Shorter procurement approval times across departments.",
                "Improved audit readiness and compliance monitoring.",
                "Standardised request forms enhance consistency and reporting."
            ],
        },
    },
    {
        "id": "brief_low_04",
        "product_answer": "yes",
        "total_score": 38,  # < 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "No",
            "Can you specify your Project Type / Capability": "Strategic Business Development",
            "Is your project Product related?": "Yes",
            "What is your expected budget?": "Between 2-10 million",
            "What is the current ERL* for the project?": "5-6",
            "Is the project government or military funded?": "Yes, it is funded 50/50 by the company and by public funding",
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "Rolls-Royce is familiar with this area and sees it as an opportunity for improvement and growth.",
            "How is the overall stability of the project?":
                "Moderate - the business case and the related risks are understood.",
            "What is the status of the cross-functional project team?":
                "Required resources estimated but capability owners not engaged.",
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Several (5 to 9).",
            "To what extent do project risks reach?":
                "Risks are limited to local or domestic matters that are easily managed.",
            "The advancement of the project is approved and governed at:":
                "Business level (CEO -2).",
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement is considered for both internal and external customers and is geographically limited.",
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple reputational concerns or risks identified, all easily manageable.",
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have low alignment; there are multiple stakeholders with varying levels of influence.",
            "How many partners or contractors are actively involved in the project?":
                "A moderate group (3-4) of partners or contractors are involved.",
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "4-5 - A moderate number of core supply chain entities are directly managed.",
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, more than 1 first language",
        },
        "sections": {
            "Project Name": "Service Desk Triage Uplift",
            "Project Sponsor": "Fatima Sayed",
            "Project Description": (
                "Improve service desk triage with structured intake forms, classification rules, and basic automations. "
                "The aim is to increase first-time-right routing and reduce reassignment delays. The project is contained "
                "within the service desk and leverages existing ticketing tools. Limited training ensures adoption."
            ),
            "Risks": [
                "Inconsistent ticket categorisation may limit triage effectiveness.",
                "Partial data capture could reduce assignment accuracy.",
                "Resistance from agents who prefer manual assignment methods."
            ],
            "Assumptions": [
                "Existing ticketing platform supports rule-based routing.",
                "Team leads provide availability for user testing.",
                "Operational workload allows training without disruption."
            ],
            "Benefits": [
                "Faster resolution times with better triage accuracy.",
                "Reduced reassignments lower operational workload.",
                "Improved service visibility and reporting from structured intake."
            ],
        },
    },
]

PAR_HIGH = [
    {
        "id": "brief_par_01",
        "product_answer": "no",
        "total_score": 60,  # ≥ 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "Yes",
            "Can you specify your Project Type / Capability": "IT Program Management",
            "Is your project Product related?": "No",
            "What is your expected budget?": "More than 101 million",
            "What is the current ERL* for the project?": "5-6",
            "Is the project government or military funded?": "Yes",
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "This is highly novel, both for Rolls-Royce and globally.",
            "How is the overall stability of the project?":
                "Low - the business case is very volatile, is high level risks, and requirements are difficult to capture and anticipate.",
            "What is the status of the cross-functional project team?":
                "Resources are volatile and not agreed with high confidence.",
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Very diverse (15 or more, involving multiple disciplines and methods).",
            "To what extent do project risks reach?":
                "Major legal complexities are involved, such as joint ventures, navigating multiple legal systems across countries, international arbitration, or contracts established outside the company’s home country.",
            "The advancement of the project is approved and governed at:":
                "Board level.",
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement extends to external customers, is of global importance, and spans more than two divisions.",
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple potential reputational concerns identified.",
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have very low alignment; there are multiple stakeholders with significant influence.",
            "How many partners or contractors are actively involved in the project?":
                "A large, diverse consortium of partners or contractors is involved.",
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "More than 5 - A large number of core supply chain entities are directly managed.",
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "More than 3 divisions/functions, more than 3 sites, more than 1 first language",
        },
        "sections": {
            "Project Name": "Enterprise Workflow Rollout",
            "Project Sponsor": "John Smith",
            "Project Description": (
                "Implement a workflow engine across Finance, HR, and Procurement with ERP/HRIS integration, "
                "role-based approvals, and e-signatures. Planning is advanced with confirmed requirements, "
                "structured verification, user testing, and staged deployment. KPIs track cycle time, rework, "
                "and compliance effectiveness. Supplier capability is embedded in SoWs with measurable performance metrics. "
                "Change plans and training ensure adoption; handover to BAU includes ownership and in-service support."
            ),
            "Risks": [
                "Integration complexity with legacy ERP/HRIS may delay cutover.",
                "Cross-functional dependencies may extend the schedule.",
                "Change resistance during SOP adoption could reduce compliance.",
                "Supplier underperformance could affect timely deliverables."
            ],
            "Assumptions": [
                "Requirements are documented and consistent with scope.",
                "Contracts and SoWs include KPIs and performance remedies.",
                "Testing environments and representative data are available.",
                "Sufficient resourcing is secured for rollout activities."
            ],
            "Benefits": [
                "Measured cycle-time reduction and fewer rework instances.",
                "Improved auditability and compliance through e-signature.",
                "Standardised approval processes across functions.",
                "Clear ownership in BAU ensures sustained benefits delivery."
            ],
        },
    },
    {
        "id": "brief_par_02",
        "product_answer": "no",
        "total_score": 48,  # ≥ 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "No",
            "Can you specify your Project Type / Capability": "Contract Performance Management",
            "Is your project Product related?": "No",
            "What is your expected budget?": "Between 11-100 million",
            "What is the current ERL* for the project?": "5-6",
            "Is the project government or military funded?": "Yes, it is funded 50/50 by the company and by public funding",
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "This is highly novel, both for Rolls-Royce and globally.",
            "How is the overall stability of the project?":
                "Moderate - the business case and the related risks are understood.",
            "What is the status of the cross-functional project team?":
                "Required resources estimated but capability owners not engaged.",
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Relatively diverse (10 to 14).",
            "To what extent do project risks reach?":
                "There are several legal or contractual challenges within a single country, requiring support from subject matter experts or legal counsel.",
            "The advancement of the project is approved and governed at:":
                "Sector level (CEO -1).",
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement is considered for both internal and external customers, with additional global significance.",
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple reputational concerns or risks identified, all easily manageable.",
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have low alignment; there are multiple stakeholders with varying levels of influence.",
            "How many partners or contractors are actively involved in the project?":
                "A moderate group (3-4) of partners or contractors are involved.",
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "4-5 - A moderate number of core supply chain entities are directly managed.",
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, more than 1 first language",
        },
        "sections": {
            "Project Name": "Operations Transformation Programme",
            "Project Sponsor": "Fatima Sayed",
            "Project Description": (
                "Transform case handling operations by standardising SOPs and embedding quality controls. "
                "Requirements are current and approved; the schedule reflects committed funding with credible dependencies. "
                "Verification and testing use defined acceptance criteria. Benefits are tracked with KPIs. "
                "Supplier capability and value-for-money are evidenced; performance is reviewed against contracts. "
                "Change and communication plans support adoption, with handover to BAU secured."
            ),
            "Risks": [
                "Scope creep across diverse workstreams could increase cost and effort.",
                "Competing priorities for SMEs may impact schedules.",
                "Benefits realisation may slip if KPIs are not embedded effectively.",
                "Supplier delivery delays could impact readiness for testing."
            ],
            "Assumptions": [
                "Approved business case and funding are in place.",
                "RACI matrix confirmed for programme and supplier roles.",
                "Data migration strategy is agreed with operations.",
                "Stakeholder communications plan is active and supported."
            ],
            "Benefits": [
                "Quality and throughput improvements evidenced by KPIs.",
                "Lower cost-to-serve via process rationalisation.",
                "Improved transparency and adherence to schedule.",
                "More consistent customer and colleague experience across sites."
            ],
        },
    },
    {
        "id": "brief_par_03",
        "product_answer": "no",
        "total_score": 44,  # ≥ 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "Yes",
            "Can you specify your Project Type / Capability": "Infrastructure Projects",
            "Is your project Product related?": "No",
            "What is your expected budget?": "Between 11-100 million",
            "What is the current ERL* for the project?": "<5",
            "Is the project government or military funded?": "Yes",
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "Rolls-Royce is aware of this area, and it is currently being developed elsewhere.",
            "How is the overall stability of the project?":
                "Moderate - the business case and the related risks are understood.",
            "What is the status of the cross-functional project team?":
                "Required resources estimated but capability owners not engaged.",
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Relatively diverse (10 to 14).",
            "To what extent do project risks reach?":
                "There are several legal or contractual challenges within a single country, requiring support from subject matter experts or legal counsel.",
            "The advancement of the project is approved and governed at:":
                "Sector level (CEO -1).",
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement is considered for both internal and external customers, with additional global significance.",
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple reputational concerns or risks identified, all easily manageable.",
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have low alignment; there are multiple stakeholders with varying levels of influence.",
            "How many partners or contractors are actively involved in the project?":
                "A moderate group (3-4) of partners or contractors are involved.",
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "4-5 - A moderate number of core supply chain entities are directly managed.",
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, more than 1 first language",
        },
        "sections": {
            "Project Name": "Finance Case Management",
            "Project Sponsor": "Priya Desai",
            "Project Description": (
                "Introduce Finance case management with segregation of duties, RBAC, and audit trails. "
                "Detailed design is complete; verification and test results will demonstrate compliance. "
                "Costs are approved with contingency. Governance covers reporting, change, and escalation. "
                "Handover plan ensures ownership, training, and BAU support. KPIs track defect leakage, control compliance, and cycle time."
            ),
            "Risks": [
                "RBAC model delays could affect cutover readiness.",
                "Data quality issues during migration may extend testing.",
                "Late testing results could shift schedule."
            ],
            "Assumptions": [
                "Audit controls are defined and approved.",
                "Test environments and masked data are available.",
                "Resourcing is aligned to support migration and test execution."
            ],
            "Benefits": [
                "Greater compliance with audit controls and reduced rework.",
                "Improved cycle times with verified audit trail.",
                "Defects reduced, ensuring smoother operations post go-live."
            ],
        },
    },
    {
        "id": "brief_par_04",
        "product_answer": "no",
        "total_score": 52,  # ≥ 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "No",
            "Can you specify your Project Type / Capability": "Government Funding",
            "Is your project Product related?": "No",
            "What is your expected budget?": "More than 101 million",
            "What is the current ERL* for the project?": "5-6",
            "Is the project government or military funded?": "Yes",
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "This is highly novel, both for Rolls-Royce and globally.",
            "How is the overall stability of the project?":
                "Low - the business case is very volatile, is high level risks, and requirements are difficult to capture and anticipate.",
            "What is the status of the cross-functional project team?":
                "Resources are volatile and not agreed with high confidence.",
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Very diverse (15 or more, involving multiple disciplines and methods).",
            "To what extent do project risks reach?":
                "Major legal complexities are involved, such as joint ventures, navigating multiple legal systems across countries, international arbitration, or contracts established outside the company’s home country.",
            "The advancement of the project is approved and governed at:":
                "Board level.",
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement extends to external customers, is of global importance, and spans more than two divisions.",
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple potential reputational concerns identified.",
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have very low alignment; there are multiple stakeholders with significant influence.",
            "How many partners or contractors are actively involved in the project?":
                "A large, diverse consortium of partners or contractors is involved.",
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "More than 5 - A large number of core supply chain entities are directly managed.",
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "More than 3 divisions/functions, more than 3 sites, more than 1 first language",
        },
        "sections": {
            "Project Name": "Supplier Onboarding Digitisation",
            "Project Sponsor": "Robert Martinez",
            "Project Description": (
                "Digitise supplier onboarding with standard contracts, KYC checks, and automated approvals integrated with ERP. "
                "Requirements and test metrics are confirmed. Supplier capability and value-for-money are assessed in contracts. "
                "Training and communication plans address readiness, and handover to BAU includes ownership and in-service support. "
                "Benefits are tracked through KPIs in financial planning."
            ),
            "Risks": [
                "Third-party KYC data may be incomplete or delayed.",
                "Policy exceptions could complicate approval workflows.",
                "Integration defects could affect go-live readiness."
            ],
            "Assumptions": [
                "Supplier contracts include measurable performance obligations.",
                "Test data and environments are provisioned on time.",
                "Change champions are identified for early adoption."
            ],
            "Benefits": [
                "Faster supplier activation with reduced manual effort.",
                "Improved compliance with onboarding requirements.",
                "Better contract oversight with KPI monitoring."
            ],
        },
    },
]

PILM_HIGH = [
    {
        "id": "brief_pilm_01",
        "product_answer": "yes",
        "total_score": 60,  # ≥ 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "Yes",
            "Can you specify your Project Type / Capability": "IT Program Management",
            "Is your project Product related?": "Yes",
            "What is your expected budget?": "More than 101 million",
            "What is the current ERL* for the project?": "5-6",
            "Is the project government or military funded?": "Yes",
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "This is highly novel, both for Rolls-Royce and globally.",
            "How is the overall stability of the project?":
                "Low - the business case is very volatile, is high level risks, and requirements are difficult to capture and anticipate.",
            "What is the status of the cross-functional project team?":
                "Resources are volatile and not agreed with high confidence.",
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Very diverse (15 or more, involving multiple disciplines and methods).",
            "To what extent do project risks reach?":
                "Major legal complexities are involved, such as joint ventures, navigating multiple legal systems across countries, international arbitration, or contracts established outside the company’s home country.",
            "The advancement of the project is approved and governed at:":
                "Board level.",
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement extends to external customers, is of global importance, and spans more than two divisions.",
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple potential reputational concerns identified.",
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have very low alignment; there are multiple stakeholders with significant influence.",
            "How many partners or contractors are actively involved in the project?":
                "A large, diverse consortium of partners or contractors is involved.",
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "More than 5 - A large number of core supply chain entities are directly managed.",
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "More than 3 divisions/functions, more than 3 sites, more than 1 first language",
        },
        "sections": {
            "Project Name": "Mobile Wallet MVP",
            "Project Sponsor": "Alice Johnson",
            "Project Description": (
                "Deliver a Mobile Wallet MVP covering registration, KYC, wallet funding, P2P transfers, merchant payments "
                "and rewards. Releases are iterative with feature flags and canary rollout. Non-functional requirements "
                "include performance SLIs, availability SLOs, encryption at rest/in transit, and privacy by design. "
                "Telemetry, alerting and run-books are prepared for BAU handover."
            ),
            "Risks": [
                "Third-party KYC API instability may delay onboarding flows.",
                "App store review timelines could impact release cadence.",
                "Insufficient device coverage in testing could cause production defects.",
                "Payment acquirer certification may extend the schedule."
            ],
            "Assumptions": [
                "Acquirer sandbox and certificates are available for end-to-end testing.",
                "Legal sign-off on T&Cs, consent wording and data retention is secured.",
                "Mobile CI/CD pipelines can support phased rollout and hotfixes.",
                "Product analytics is enabled to validate adoption and funnels."
            ],
            "Benefits": [
                "Faster time-to-market via MVP scope and incremental releases.",
                "Higher conversion with simplified onboarding and KYC pass rates.",
                "Better reliability from observability, playbooks and SLO monitoring.",
                "Improved compliance through strong encryption and privacy controls."
            ],
        },
    },
    {
        "id": "brief_pilm_02",
        "product_answer": "yes",
        "total_score": 50,  # ≥ 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "No",
            "Can you specify your Project Type / Capability": "Technical Program Management",
            "Is your project Product related?": "Yes",
            "What is your expected budget?": "Between 11-100 million",
            "What is the current ERL* for the project?": "5-6",
            "Is the project government or military funded?": "Yes, it is funded 50/50 by the company and by public funding",
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "This is highly novel, both for Rolls-Royce and globally.",
            "How is the overall stability of the project?":
                "Moderate - the business case and the related risks are understood.",
            "What is the status of the cross-functional project team?":
                "Required resources estimated but capability owners not engaged.",
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Relatively diverse (10 to 14).",
            "To what extent do project risks reach?":
                "There are several legal or contractual challenges within a single country, requiring support from subject matter experts or legal counsel.",
            "The advancement of the project is approved and governed at:":
                "Sector level (CEO -1).",
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement is considered for both internal and external customers, with additional global significance.",
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple reputational concerns or risks identified, all easily manageable.",
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have low alignment; there are multiple stakeholders with varying levels of influence.",
            "How many partners or contractors are actively involved in the project?":
                "A moderate group (3-4) of partners or contractors are involved.",
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "4-5 - A moderate number of core supply chain entities are directly managed.",
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, more than 1 first language",
        },
        "sections": {
            "Project Name": "Customer Platform Modernisation",
            "Project Sponsor": "Robert Martinez",
            "Project Description": (
                "Modernise the customer platform to a service-oriented architecture with shared identity, profile, "
                "payments and notifications. Roadmap emphasises MVP onboarding, then progressive enhancement. "
                "Security reviews cover OWASP MASVS/ASVS, secrets management and least privilege. "
                "Blue-green deploys, rollbacks and error budgets govern releases."
            ),
            "Risks": [
                "Legacy system dependencies may constrain API design and performance.",
                "Scope creep from adjacent product domains could dilute delivery focus.",
                "Insufficient non-functional testing could breach performance targets.",
                "Vendor lock-in risks around proprietary services and SDKs."
            ],
            "Assumptions": [
                "Data migration strategy is agreed with measurable cutover criteria.",
                "Foundational platform teams provide capacity for shared services.",
                "Threat modelling outcomes are actioned in the backlog.",
                "Customer research and accessibility standards inform UX patterns."
            ],
            "Benefits": [
                "Reduced time to launch new features through platform reuse.",
                "Improved security posture and auditability across the stack.",
                "Higher reliability and controlled change via blue-green and rollbacks.",
                "Consistent customer experience across channels and products."
            ],
        },
    },
    {
        "id": "brief_pilm_03",
        "product_answer": "yes",
        "total_score": 44,  # ≥ 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "Yes",
            "Can you specify your Project Type / Capability": "Strategic Business Development",
            "Is your project Product related?": "Yes",
            "What is your expected budget?": "Between 11-100 million",
            "What is the current ERL* for the project?": "<5",
            "Is the project government or military funded?": "Yes",
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "Rolls-Royce is aware of this area, and it is currently being developed elsewhere.",
            "How is the overall stability of the project?":
                "Moderate - the business case and the related risks are understood.",
            "What is the status of the cross-functional project team?":
                "Required resources estimated but capability owners not engaged.",
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Relatively diverse (10 to 14).",
            "To what extent do project risks reach?":
                "There are several legal or contractual challenges within a single country, requiring support from subject matter experts or legal counsel.",
            "The advancement of the project is approved and governed at:":
                "Sector level (CEO -1).",
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement is considered for both internal and external customers, with additional global significance.",
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple reputational concerns or risks identified, all easily manageable.",
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have low alignment; there are multiple stakeholders with varying levels of influence.",
            "How many partners or contractors are actively involved in the project?":
                "A moderate group (3-4) of partners or contractors are involved.",
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "4-5 - A moderate number of core supply chain entities are directly managed.",
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, more than 1 first language",
        },
        "sections": {
            "Project Name": "Data Insights Productisation",
            "Project Sponsor": "Priya Desai",
            "Project Description": (
                "Package high-value analytics into a product with curated datasets, governed access and self-serve "
                "dashboards. Focus on a small number of decision journeys, with privacy-preserving controls, lineage and "
                "quality SLAs. Incremental releases validate usefulness and adoption with real users."
            ),
            "Risks": [
                "Poor upstream data quality may undermine trust in insights.",
                "Ambiguous data ownership can slow governance decisions.",
                "Over-customisation for stakeholders risks product bloat.",
                "Insufficient anonymisation could raise privacy concerns."
            ],
            "Assumptions": [
                "Data contracts are defined with stewards for critical datasets.",
                "A metrics layer and catalog are available for discovery and reuse.",
                "Access is provisioned through RBAC and least privilege.",
                "Pilot users will provide feedback every sprint to shape the roadmap."
            ],
            "Benefits": [
                "Faster decision-making with reliable, curated metrics.",
                "Lower BI support costs through standardised, self-serve assets.",
                "Better compliance with documented lineage and data contracts.",
                "Higher adoption via tight focus on priority decision journeys."
            ],
        },
    },
    {
        "id": "brief_pilm_04",
        "product_answer": "yes",
        "total_score": 56,  # ≥ 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "No",
            "Can you specify your Project Type / Capability": "IT Program Management",
            "Is your project Product related?": "Yes",
            "What is your expected budget?": "More than 101 million",
            "What is the current ERL* for the project?": "5-6",
            "Is the project government or military funded?": "My function is not supported by military funding",
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "This is highly novel, both for Rolls-Royce and globally.",
            "How is the overall stability of the project?":
                "Low - the business case is very volatile, is high level risks, and requirements are difficult to capture and anticipate.",
            "What is the status of the cross-functional project team?":
                "Resources are volatile and not agreed with high confidence.",
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Very diverse (15 or more, involving multiple disciplines and methods).",
            "To what extent do project risks reach?":
                "Major legal complexities are involved, such as joint ventures, navigating multiple legal systems across countries, international arbitration, or contracts established outside the company’s home country.",
            "The advancement of the project is approved and governed at:":
                "Board level.",
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement extends to external customers, is of global importance, and spans more than two divisions.",
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple potential reputational concerns identified.",
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have very low alignment; there are multiple stakeholders with significant influence.",
            "How many partners or contractors are actively involved in the project?":
                "A large, diverse consortium of partners or contractors is involved.",
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "More than 5 - A large number of core supply chain entities are directly managed.",
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "More than 3 divisions/functions, more than 3 sites, more than 1 first language",
        },
        "sections": {
            "Project Name": "Partner API Gateway",
            "Project Sponsor": "Fatima Sayed",
            "Project Description": (
                "Launch a Partner API Gateway with developer portal, API keys/OAuth, rate limiting and observability. "
                "Release plan starts with a small set of high-value APIs and sandbox access. Non-functionals target "
                "availability, latency and error budgets; security includes mTLS, scopes and audit logging. "
                "Operational readiness includes SLAs, on-call rotas and incident playbooks."
            ),
            "Risks": [
                "Unclear external partner requirements could delay API design.",
                "Inadequate throttling may affect platform stability under load spikes.",
                "Key management or secret leakage could introduce security risk.",
                "Backward-compatibility pressures may slow iteration velocity."
            ],
            "Assumptions": [
                "API standards (versioning, pagination, error codes) are agreed.",
                "Central identity provider supports OAuth/OIDC patterns.",
                "Traffic management and WAF policies are in place before go-live.",
                "Partner onboarding process and documentation are resourced."
            ],
            "Benefits": [
                "Accelerated partner integrations with a high-quality developer experience.",
                "Improved platform stability through rate limiting and observability.",
                "Clear security posture with OAuth scopes, audit logs and mTLS.",
                "Reusable API patterns reduce time to expose new capabilities."
            ],
        },
    },
]

# Public list your app imports
MOCK_CASES = LOW_SCORE + PAR_HIGH + PILM_HIGH
