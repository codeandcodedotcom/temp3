# mocks.py
# 12 demo cases: 4 x (Score<40, no doc), 4 x (Score>=40 & PAR), 4 x (Score>=40 & PILM)
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
            "What is your expected budget?": "Less 1 million",  # 1
            "What is the current ERL* for the project?": "7+",  # 0
            "Is the project government or military funded?": "No",  # 2
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "Rolls-Royce has substantial expertise in this area, with established development and standardisation.",  # 1
            "How is the overall stability of the project?":
                "Very high - the business case is well defined and clear.",  # 1
            "What is the status of the cross-functional project team?":
                "The resources are engaged via capability owners.",  # 1
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Few (less than 5).",  # 1
            "To what extent do project risks reach?":
                "No significant areas of concern have been identified.",  # 1
            "The advancement of the project is approved and governed at:":
                "Department level (CEO -3).",  # 1
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Focus is limited to internal customers, with scope restricted to the local business.",  # 1
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "No reputational concerns or risks identified.",  # 1
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders are highly aligned; there are few stakeholders with limited influence.",  # 1
            "How many partners or contractors are actively involved in the project?":
                "No partners or contractors are involved.",  # 1
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "None - No core supply chain entities are directly managed.",  # 1
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "1 division/function, 1 site, 1 first language",  # 1
        },
        "sections": {
            "Project Name": "Internal Process Optimisation",
            "Project Sponsor": "Priya Desai",
            "Project Description": "Optimise approvals and case management with a lightweight workflow solution to reduce manual effort and improve auditability within six months.",
            "Risks": [
                "Vendor onboarding delays",
                "Resistance to adopting new SOPs",
                "Data quality issues during migration",
            ],
            "Assumptions": [
                "ERP/HRIS remains stable",
                "SMEs available for discovery and UAT",
            ],
            "Benefits": [
                "Faster approval cycles",
                "Improved control evidence",
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
            "What is your expected budget?": "Less 1 million",  # 1
            "What is the current ERL* for the project?": "<5",  # 2
            "Is the project government or military funded?": "No",  # 2
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "Rolls-Royce is familiar with this area and sees it as an opportunity for improvement and growth.",  # 2
            "How is the overall stability of the project?":
                "High - the business case is established with limited risks.",  # 2
            "What is the status of the cross-functional project team?":
                "Bulk resources are available in 5 Year Plan but not committed by capability owners.",  # 2
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Few (less than 5).",  # 1
            "To what extent do project risks reach?":
                "Risks are limited to local or domestic matters that are easily managed.",  # 2
            "The advancement of the project is approved and governed at:":
                "Department level (CEO -3).",  # 1
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Focus is limited to internal customers, with scope restricted to the local business.",  # 1
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Limited reputational concerns or risks identified, all easily manageable.",  # 2
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders are moderately aligned; there are multiple stakeholders with limited influence.",  # 2
            "How many partners or contractors are actively involved in the project?":
                "A small group (1-2) of partners or contractors are involved.",  # 2
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "1-3 - A small number of core supply chain entities are directly managed.",  # 2
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, 1 first language",  # 2
        },
        "sections": {
            "Project Name": "Internal Communications Pilot",
            "Project Sponsor": "Robert Martinez",
            "Project Description": "Pilot a small-scale communications toolkit to improve stakeholder updates and reduce ad-hoc email traffic.",
            "Risks": [
                "Limited change bandwidth from teams",
                "Competing priorities delay workshops",
            ],
            "Assumptions": [
                "Comms templates can be reused",
                "Basic analytics available",
            ],
            "Benefits": [
                "Clearer status reporting",
                "Less rework from misalignment",
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
            "What is your expected budget?": "Between 2-10 million",  # 2
            "What is the current ERL* for the project?": "<5",  # 2
            "Is the project government or military funded?": "No",  # 2
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "Rolls-Royce has substantial expertise in this area, with established development and standardisation.",  # 1
            "How is the overall stability of the project?":
                "High - the business case is established with limited risks.",  # 2
            "What is the status of the cross-functional project team?":
                "The resources are engaged via capability owners.",  # 1
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Several (5 to 9).",  # 2
            "To what extent do project risks reach?":
                "Risks are limited to local or domestic matters that are easily managed.",  # 2
            "The advancement of the project is approved and governed at:":
                "Business level (CEO -2).",  # 2
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Focus is limited to internal customers, with scope restricted to the local business.",  # 1
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Limited reputational concerns or risks identified, all easily manageable.",  # 2
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders are moderately aligned; there are multiple stakeholders with limited influence.",  # 2
            "How many partners or contractors are actively involved in the project?":
                "A small group (1-2) of partners or contractors are involved.",  # 2
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "1-3 - A small number of core supply chain entities are directly managed.",  # 2
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, 1 first language",  # 2
        },
        "sections": {
            "Project Name": "Procurement Approval Cleanup",
            "Project Sponsor": "Alice Johnson",
            "Project Description": "Rationalise approval paths and remove manual steps to improve transparency and reduce cycle time.",
            "Risks": [
                "Exception handling increases complexity",
                "Stakeholder misalignment on approvals",
            ],
            "Assumptions": [
                "Approval policy stable",
                "Key approvers available",
            ],
            "Benefits": [
                "Shorter approval times",
                "Better audit readiness",
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
            "What is your expected budget?": "Between 2-10 million",  # 2
            "What is the current ERL* for the project?": "5-6",  # 4
            "Is the project government or military funded?": "Yes, it is funded 50/50 by the company and by public funding",  # 2
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "Rolls-Royce is familiar with this area and sees it as an opportunity for improvement and growth.",  # 2
            "How is the overall stability of the project?":
                "Moderate - the business case and the related risks are understood.",  # 3
            "What is the status of the cross-functional project team?":
                "Required resources estimated but capability owners not engaged.",  # 3
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Several (5 to 9).",  # 2
            "To what extent do project risks reach?":
                "Risks are limited to local or domestic matters that are easily managed.",  # 2
            "The advancement of the project is approved and governed at:":
                "Business level (CEO -2).",  # 2
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement is considered for both internal and external customers and is geographically limited.",  # 2
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple reputational concerns or risks identified, all easily manageable.",  # 3
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have low alignment; there are multiple stakeholders with varying levels of influence.",  # 3
            "How many partners or contractors are actively involved in the project?":
                "A moderate group (3-4) of partners or contractors are involved.",  # 3
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "4-5 - A moderate number of core supply chain entities are directly managed.",  # 3
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, more than 1 first language",  # 3
        },
        "sections": {
            "Project Name": "Marketing Enablement Toolkit",
            "Project Sponsor": "John Smith",
            "Project Description": "Develop a reusable toolkit for go-to-market pilots and partner onboarding to standardise collateral and reduce cycle time.",
            "Risks": [
                "Limited data on pilot markets",
                "Late stakeholder alignment on scope",
            ],
            "Assumptions": [
                "Existing CRM integrations work",
                "Legal review available for assets",
            ],
            "Benefits": [
                "Faster partner activation",
                "Consistent branding assets",
            ],
        },
    },
]

PAR_HIGH = [
    {
        "id": "brief_par_01",
        "product_answer": "no",
        "total_score": 60,  # >= 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "Yes",
            "Can you specify your Project Type / Capability": "IT Program Management",
            "Is your project Product related?": "No",
            "What is your expected budget?": "More than 101 million",  # 4
            "What is the current ERL* for the project?": "5-6",  # 4
            "Is the project government or military funded?": "Yes",  # 4
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "This is highly novel, both for Rolls-Royce and globally.",  # 4
            "How is the overall stability of the project?":
                "Low - the business case is very volatile, is high level risks, and requirements are difficult to capture and anticipate.",  # 4
            "What is the status of the cross-functional project team?":
                "Resources are volatile and not agreed with high confidence.",  # 4
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Very diverse (15 or more, involving multiple disciplines and methods).",  # 4
            "To what extent do project risks reach?":
                "Major legal complexities are involved, such as joint ventures, navigating multiple legal systems across countries, international arbitration, or contracts established outside the company’s home country.",  # 4
            "The advancement of the project is approved and governed at:":
                "Board level.",  # 4
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement extends to external customers, is of global importance, and spans more than two divisions.",  # 4
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple potential reputational concerns identified.",  # 4
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have very low alignment; there are multiple stakeholders with significant influence.",  # 4
            "How many partners or contractors are actively involved in the project?":
                "A large, diverse consortium of partners or contractors is involved.",  # 4
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "More than 5 - A large number of core supply chain entities are directly managed.",  # 4
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "More than 3 divisions/functions, more than 3 sites, more than 1 first language",  # 4
        },
        "sections": {
            "Project Name": "Enterprise Workflow Rollout",
            "Project Sponsor": "John Smith",
            "Project Description": "Roll out a workflow engine across Finance, HR, and Procurement with ERP/HRIS integrations and role-based approvals.",
            "Risks": [
                "Integration complexity with legacy systems",
                "Change resistance in multiple functions",
                "Data reconciliation gaps",
            ],
            "Assumptions": [
                "Budget envelope sustained",
                "No ERP re-platform during rollout",
            ],
            "Benefits": [
                "30% lead-time reduction",
                "Consistent governance and e-signatures",
            ],
        },
    },
    {
        "id": "brief_par_02",
        "product_answer": "no",
        "total_score": 48,  # >= 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "No",
            "Can you specify your Project Type / Capability": "Contract Performance Management",
            "Is your project Product related?": "No",
            "What is your expected budget?": "Between 11-100 million",  # 3
            "What is the current ERL* for the project?": "5-6",  # 4
            "Is the project government or military funded?": "Yes, it is funded 50/50 by the company and by public funding",  # 2
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "This is highly novel, both for Rolls-Royce and globally.",  # 4
            "How is the overall stability of the project?":
                "Moderate - the business case and the related risks are understood.",  # 3
            "What is the status of the cross-functional project team?":
                "Required resources estimated but capability owners not engaged.",  # 3
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Relatively diverse (10 to 14).",  # 3
            "To what extent do project risks reach?":
                "There are several legal or contractual challenges within a single country, requiring support from subject matter experts or legal counsel.",  # 3
            "The advancement of the project is approved and governed at:":
                "Sector level (CEO -1).",  # 3
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement is considered for both internal and external customers, with additional global significance.",  # 3
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple reputational concerns or risks identified, all easily manageable.",  # 3
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have low alignment; there are multiple stakeholders with varying levels of influence.",  # 3
            "How many partners or contractors are actively involved in the project?":
                "A moderate group (3-4) of partners or contractors are involved.",  # 3
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "4-5 - A moderate number of core supply chain entities are directly managed.",  # 3
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, more than 1 first language",  # 3
        },
        "sections": {
            "Project Name": "Operations Transformation Programme",
            "Project Sponsor": "Fatima Sayed",
            "Project Description": "Digitise approvals, unify data governance, and standardise controls across operations as part of a change programme.",
            "Risks": [
                "Scope creep across workstreams",
                "Competing priorities for SMEs",
            ],
            "Assumptions": [
                "Steering committee cadence in place",
                "Vendor contracts executed",
            ],
            "Benefits": [
                "Unified compliance posture",
                "Cross-functional efficiency gains",
            ],
        },
    },
    {
        "id": "brief_par_03",
        "product_answer": "no",
        "total_score": 44,  # >= 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "Yes",
            "Can you specify your Project Type / Capability": "Infrastructure Projects",
            "Is your project Product related?": "No",
            "What is your expected budget?": "Between 11-100 million",  # 3
            "What is the current ERL* for the project?": "<5",  # 2
            "Is the project government or military funded?": "Yes",  # 4
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "Rolls-Royce is aware of this area, and it is currently being developed elsewhere.",  # 3
            "How is the overall stability of the project?":
                "Moderate - the business case and the related risks are understood.",  # 3
            "What is the status of the cross-functional project team?":
                "Required resources estimated but capability owners not engaged.",  # 3
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Relatively diverse (10 to 14).",  # 3
            "To what extent do project risks reach?":
                "There are several legal or contractual challenges within a single country, requiring support from subject matter experts or legal counsel.",  # 3
            "The advancement of the project is approved and governed at:":
                "Sector level (CEO -1).",  # 3
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement is considered for both internal and external customers, with additional global significance.",  # 3
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple reputational concerns or risks identified, all easily manageable.",  # 3
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have low alignment; there are multiple stakeholders with varying levels of influence.",  # 3
            "How many partners or contractors are actively involved in the project?":
                "A moderate group (3-4) of partners or contractors are involved.",  # 3
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "4-5 - A moderate number of core supply chain entities are directly managed.",  # 3
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, more than 1 first language",  # 3
        },
        "sections": {
            "Project Name": "Finance Case Management",
            "Project Sponsor": "Priya Desai",
            "Project Description": "Implement case management for finance operations with RBAC and e-signatures to improve control effectiveness.",
            "Risks": [
                "RBAC design delays",
                "Data migration gaps",
            ],
            "Assumptions": [
                "Audit controls defined",
                "Integration sandboxes available",
            ],
            "Benefits": [
                "Higher control compliance",
                "Reduced rework rate",
            ],
        },
    },
    {
        "id": "brief_par_04",
        "product_answer": "no",
        "total_score": 52,  # >= 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "No",
            "Can you specify your Project Type / Capability": "Government Funding",
            "Is your project Product related?": "No",
            "What is your expected budget?": "More than 101 million",  # 4
            "What is the current ERL* for the project?": "5-6",  # 4
            "Is the project government or military funded?": "Yes",  # 4
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "This is highly novel, both for Rolls-Royce and globally.",  # 4
            "How is the overall stability of the project?":
                "Low - the business case is very volatile, is high level risks, and requirements are difficult to capture and anticipate.",  # 4
            "What is the status of the cross-functional project team?":
                "Resources are volatile and not agreed with high confidence.",  # 4
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Very diverse (15 or more, involving multiple disciplines and methods).",  # 4
            "To what extent do project risks reach?":
                "Major legal complexities are involved, such as joint ventures, navigating multiple legal systems across countries, international arbitration, or contracts established outside the company’s home country.",  # 4
            "The advancement of the project is approved and governed at:":
                "Board level.",  # 4
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement extends to external customers, is of global importance, and spans more than two divisions.",  # 4
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple potential reputational concerns identified.",  # 4
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have very low alignment; there are multiple stakeholders with significant influence.",  # 4
            "How many partners or contractors are actively involved in the project?":
                "A large, diverse consortium of partners or contractors is involved.",  # 4
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "More than 5 - A large number of core supply chain entities are directly managed.",  # 4
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "More than 3 divisions/functions, more than 3 sites, more than 1 first language",  # 4
        },
        "sections": {
            "Project Name": "Global Controls Uplift",
            "Project Sponsor": "Alice Johnson",
            "Project Description": "Standardise governance and approval flows across business units with end-to-end traceability and analytics.",
            "Risks": [
                "Complex change across regions",
                "Lengthy vendor contracting",
            ],
            "Assumptions": [
                "Dedicated PMO and governance cadence",
                "Data model defined early",
            ],
            "Benefits": [
                "Unified control posture",
                "Improved audit readiness globally",
            ],
        },
    },
]

PILM_HIGH = [
    {
        "id": "brief_pilm_01",
        "product_answer": "yes",
        "total_score": 60,  # >= 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "Yes",
            "Can you specify your Project Type / Capability": "IT Program Management",
            "Is your project Product related?": "Yes",
            "What is your expected budget?": "More than 101 million",  # 4
            "What is the current ERL* for the project?": "5-6",  # 4
            "Is the project government or military funded?": "Yes",  # 4
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "This is highly novel, both for Rolls-Royce and globally.",  # 4
            "How is the overall stability of the project?":
                "Low - the business case is very volatile, is high level risks, and requirements are difficult to capture and anticipate.",  # 4
            "What is the status of the cross-functional project team?":
                "Resources are volatile and not agreed with high confidence.",  # 4
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Very diverse (15 or more, involving multiple disciplines and methods).",  # 4
            "To what extent do project risks reach?":
                "Major legal complexities are involved, such as joint ventures, navigating multiple legal systems across countries, international arbitration, or contracts established outside the company’s home country.",  # 4
            "The advancement of the project is approved and governed at:":
                "Board level.",  # 4
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement extends to external customers, is of global importance, and spans more than two divisions.",  # 4
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple potential reputational concerns identified.",  # 4
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have very low alignment; there are multiple stakeholders with significant influence.",  # 4
            "How many partners or contractors are actively involved in the project?":
                "A large, diverse consortium of partners or contractors is involved.",  # 4
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "More than 5 - A large number of core supply chain entities are directly managed.",  # 4
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "More than 3 divisions/functions, more than 3 sites, more than 1 first language",  # 4
        },
        "sections": {
            "Project Name": "SmartPay Mobile App",
            "Project Sponsor": "Priya Desai",
            "Project Description": "Deliver a secure mobile payment app covering registration, KYC, wallet, P2P, merchant payments, and rewards with staged releases.",
            "Risks": [
                "App store rejections",
                "Fraud and abuse risks",
                "Latency under load",
            ],
            "Assumptions": [
                "CI/CD and feature flags available",
                "Security testing planned",
            ],
            "Benefits": [
                "MAU growth from rewards",
                "Improved conversion at checkout",
            ],
        },
    },
    {
        "id": "brief_pilm_02",
        "product_answer": "yes",
        "total_score": 50,  # >= 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "No",
            "Can you specify your Project Type / Capability": "Technical Program Management",
            "Is your project Product related?": "Yes",
            "What is your expected budget?": "Between 11-100 million",  # 3
            "What is the current ERL* for the project?": "5-6",  # 4
            "Is the project government or military funded?": "Yes, it is funded 50/50 by the company and by public funding",  # 2
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "This is highly novel, both for Rolls-Royce and globally.",  # 4
            "How is the overall stability of the project?":
                "Moderate - the business case and the related risks are understood.",  # 3
            "What is the status of the cross-functional project team?":
                "Required resources estimated but capability owners not engaged.",  # 3
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Relatively diverse (10 to 14).",  # 3
            "To what extent do project risks reach?":
                "There are several legal or contractual challenges within a single country, requiring support from subject matter experts or legal counsel.",  # 3
            "The advancement of the project is approved and governed at:":
                "Sector level (CEO -1).",  # 3
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement is considered for both internal and external customers, with additional global significance.",  # 3
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple reputational concerns or risks identified, all easily manageable.",  # 3
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have low alignment; there are multiple stakeholders with varying levels of influence.",  # 3
            "How many partners or contractors are actively involved in the project?":
                "A moderate group (3-4) of partners or contractors are involved.",  # 3
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "4-5 - A moderate number of core supply chain entities are directly managed.",  # 3
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, more than 1 first language",  # 3
        },
        "sections": {
            "Project Name": "Retail Pay SuperApp",
            "Project Sponsor": "Robert Martinez",
            "Project Description": "Scale a payments superapp with rewards, merchant discovery, and analytics; enforce PCI and privacy controls with observability.",
            "Risks": [
                "Scale limits cause outages",
                "Compliance changes mid-program",
            ],
            "Assumptions": [
                "Observability and rate limiting in place",
                "Dedicated security squad",
            ],
            "Benefits": [
                "Higher retention via rewards",
                "Merchant conversion uplift",
            ],
        },
    },
    {
        "id": "brief_pilm_03",
        "product_answer": "yes",
        "total_score": 44,  # >= 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "Yes",
            "Can you specify your Project Type / Capability": "Strategic Business Development",
            "Is your project Product related?": "Yes",
            "What is your expected budget?": "Between 11-100 million",  # 3
            "What is the current ERL* for the project?": "<5",  # 2
            "Is the project government or military funded?": "Yes",  # 4
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "Rolls-Royce is aware of this area, and it is currently being developed elsewhere.",  # 3
            "How is the overall stability of the project?":
                "Moderate - the business case and the related risks are understood.",  # 3
            "What is the status of the cross-functional project team?":
                "Required resources estimated but capability owners not engaged.",  # 3
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Relatively diverse (10 to 14).",  # 3
            "To what extent do project risks reach?":
                "There are several legal or contractual challenges within a single country, requiring support from subject matter experts or legal counsel.",  # 3
            "The advancement of the project is approved and governed at:":
                "Sector level (CEO -1).",  # 3
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement is considered for both internal and external customers, with additional global significance.",  # 3
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple reputational concerns or risks identified, all easily manageable.",  # 3
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have low alignment; there are multiple stakeholders with varying levels of influence.",  # 3
            "How many partners or contractors are actively involved in the project?":
                "A moderate group (3-4) of partners or contractors are involved.",  # 3
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "4-5 - A moderate number of core supply chain entities are directly managed.",  # 3
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "2-3 divisions/functions, 2-3 sites, more than 1 first language",  # 3
        },
        "sections": {
            "Project Name": "Payments Wallet Revamp",
            "Project Sponsor": "Alice Johnson",
            "Project Description": "Revamp wallet UX and rewards with secure key management, telemetry-driven iterations, and staged rollouts.",
            "Risks": [
                "Security gaps in key handling",
                "Fragmented UX across platforms",
            ],
            "Assumptions": [
                "Design system tokens available",
                "Beta cohort recruited",
            ],
            "Benefits": [
                "Crash-free sessions improve",
                "Activation and adoption lift",
            ],
        },
    },
    {
        "id": "brief_pilm_04",
        "product_answer": "yes",
        "total_score": 56,  # >= 40
        "responses": {
            "Do you have approved budget and/or authorisation to proceed by your relevant business portfolio?": "No",
            "Can you specify your Project Type / Capability": "IT Program Management",
            "Is your project Product related?": "Yes",
            "What is your expected budget?": "More than 101 million",  # 4
            "What is the current ERL* for the project?": "5-6",  # 4
            "Is the project government or military funded?": "My function is not supported by military funding",  # 4
            "What is the degree of novelty for RR (new technology, supply chain, supplier, contract terms, organisation, methodology, IT services etc.)?":
                "This is highly novel, both for Rolls-Royce and globally.",  # 4
            "How is the overall stability of the project?":
                "Low - the business case is very volatile, is high level risks, and requirements are difficult to capture and anticipate.",  # 4
            "What is the status of the cross-functional project team?":
                "Resources are volatile and not agreed with high confidence.",  # 4
            "What is the number of functions or capabilities involved in the project (including: core engineering disciplines, management of SME, etc.)?":
                "Very diverse (15 or more, involving multiple disciplines and methods).",  # 4
            "To what extent do project risks reach?":
                "Major legal complexities are involved, such as joint ventures, navigating multiple legal systems across countries, international arbitration, or contracts established outside the company’s home country.",  # 4
            "The advancement of the project is approved and governed at:":
                "Board level.",  # 4
            "The strategic alignment with Rolls-Royce (across customers, sectors, and regions) can be described as follow:":
                "Involvement extends to external customers, is of global importance, and spans more than two divisions.",  # 4
            "Which statement best describes the reputational risks related to health, safety, environment, or publicly stated commitments for this project?":
                "Multiple potential reputational concerns identified.",  # 4
            "How would you describe the alignment of stakeholders on scope, requirements, and objectives for this activity?":
                "Stakeholders have very low alignment; there are multiple stakeholders with significant influence.",  # 4
            "How many partners or contractors are actively involved in the project?":
                "A large, diverse consortium of partners or contractors is involved.",  # 4
            "Considering only the core supply chain entities directly managed in the project, how many of them are involved?":
                "More than 5 - A large number of core supply chain entities are directly managed.",  # 4
            "How many divisions and/or enabling functions, sites, and languages are involved in the project?":
                "More than 3 divisions/functions, more than 3 sites, more than 1 first language",  # 4
        },
        "sections": {
            "Project Name": "Digital Wallet 2.0",
            "Project Sponsor": "Fatima Sayed",
            "Project Description": "Launch a next-gen wallet with rewards, merchant payments, and KYC improvements; deliver via staged releases and feature flags.",
            "Risks": [
                "Performance constraints under peak load",
                "App store policy changes",
            ],
            "Assumptions": [
                "Observability in place",
                "Security testing integrated in CI",
            ],
            "Benefits": [
                "Retention uplift from rewards",
                "Checkout conversion improvement",
            ],
        },
    },
]

# Public list your app imports
MOCK_CASES = LOW_SCORE + PAR_HIGH + PILM_HIGH
