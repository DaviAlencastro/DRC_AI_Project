from transformers import pipeline

model = pipeline("summarization", model="facebook/bart-large-cnn")
response = model("The Globalization e-Invoicing Localization Unit is responsible for the development and maintenance of electronic invoicing solutions for Brazil"
                " and Latin America within S/4HANA, and multiple other countries within the SAP Document and Reporting Compliance, cloud edition. These solutions help " \
                "thousands of customers achieve compliance with local regulations while ensuring smooth integration into global business processes.  Our AI team" \
                " enhances these capabilities with advanced large language models, natural language processing, and automation. Join us at the forefront of integrating" \
                " cutting-edge Artificial Intelligence into SAP Globalization e-Invoicing localization products, shaping the future of compliance and automation for" \
                " customers worldwide. This is a rare opportunity to pioneer Generative AI capabilities from the ground up, delivering solutions that directly impact " \
                "critical business processes across multiple industries and countries. In this role, you’ll: Design, develop, and maintain AI-driven features for SAP" \
                " Globalization e-Invoicing localization products. Create tools to support other developers from different stacks (S/4HANA and cloud), working with ABAP" \
                ", Python, Type Script, Java Script. Work in agile teams on tasks such as requirements analysis, solution architecture, code implementation, testing,"
                " and deployment. Collaborate with cross-functional teams, including product managers, UX designers, data engineers, and localization experts to" \
                " deliver high-impact solutions. Stay ahead of emerging AI trends and technologies, applying them to continuously improve our products. Ensure AI " \
                "solutions meet high standards for performance, scalability, interpretability, and compliance. Take ownership of assigned components or features, " \
                "from design to deployment, with autonomy and accountability. Create and maintain functional, technical, and model documentation.   What you will bring:" \
                " Bachelor’s or Master’s degree in Computer Science, Artificial Intelligence, Data Science, Information Systems, or related field. Professional " \
                "experience in Cloud/ABAP development in a production environment. Proficiency in Python and experience with AI frameworks. Hands-on experience " \
                "with Large Language Models (LLMs), LangChain, LangGraph, and prompt engineering techniques (RAG, few-shot prompting). Solid understanding of software " \
                "engineering principles, object-oriented programming, and design patterns. Experience with cloud platforms (SAP BTP, AWS, Azure, or GCP). Familiarity" \
                " with containerization and orchestration (Docker, Kubernetes) and CI/CD tools (JIRA, Git, Jenkins). Knowledge of agile development methodologies and" \
                " DevOps practices. Fluent in English, with excellent written and verbal communication skills. Strong analytical, problem-solving, and debugging skills." \
                " Self-driven, adaptable, and collaborative mindset. Experience in electronic invoicing, SAP eDocuments Framework or ERP is a plus." \
                " Experience with RDF Knowledge Graphs is a plus. Experience with ABAP technology is a plus.")

print(response)