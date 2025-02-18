# dataset
def get_data():
    appliso_data = [
        {
            "input": "What is Appliso Technologies known for?",
            "output": "Appliso Technologies is an innovative software technology company that crafts beautiful product experiences using smart design sprint strategies and advanced technology."
        },
        {
            "input": "Does Appliso offer training for digital marketing?",
            "output": "Yes, Appliso provides comprehensive digital marketing training covering SEO, PPC, social media marketing, and more."
        },
        {
            "input": "How can Appliso help technology startups?",
            "output": "Appliso offers CTO as a service, helping startups set up a solid technical foundation, plan their technology stack, and accelerate product development efficiently."
        },
        {
            "input": "Does Appliso provide remote learning options?",
            "output": "Yes, Appliso offers both in-person and remote learning options for all courses, allowing flexibility for students worldwide."
        },
        {
            "input": "What services does Appliso offer for product engineering?",
            "output": "Appliso helps startups design, build, and maintain high-quality technology products by fostering an excellent engineering culture and using best development practices."
        },
        {
            "input": "How does Appliso assist in technology stack planning?",
            "output": "Appliso helps businesses scale quickly by selecting and validating the right technology stack, avoiding long and expensive decision-making processes."
        },
        {
            "input": "Does Appliso provide job placement after training?",
            "output": "Yes, Appliso offers career support and job placement assistance for students upon course completion."
        },
        {
            "input": "What is the difference between front-end and back-end development?",
            "output": "Front-end development focuses on user interfaces and experience using HTML, CSS, and JavaScript, while back-end development manages server-side logic with languages like Python, Node.js, and Java."
        },
        {
            "input": "How is SAIL related to Appliso?",
            "output": "In collaboration with SAIL Innovation Lab, Appliso offers a Digital Marketing Program aimed at equipping individuals with essential digital skills for the tech industry."
        },
        {
            "input": "How does Appliso support businesses with product management?",
            "output": "Appliso helps businesses create sustainable operations and processes, joining in-house teams to spin off new ideas that require innovative approaches."
        },
        {
            "input": "Does Appliso offer UI/UX design services?",
            "output": "Yes, Appliso provides UI/UX design services to create intuitive and visually appealing digital experiences."
        },
        {
            "input": "What programming languages does Appliso specialize in?",
            "output": "Appliso specializes in JavaScript, Python, Node.js, React, and various modern frameworks to develop scalable applications."
        },
        {
            "input": "Does Appliso offer cloud computing services?",
            "output": "Yes, Appliso offers cloud computing solutions, including AWS, Azure, and Google Cloud, to help businesses scale efficiently."
        },
        {
            "input": "Can Appliso help businesses with automation?",
            "output": "Yes, Appliso helps businesses streamline operations through automation tools and AI-driven solutions."
        },
        {
            "input": "Does Appliso provide consulting services?",
            "output": "Yes, Appliso offers technology consulting services to help businesses improve efficiency and adopt the best digital solutions."
        },
        {
            "input": "What industries does Appliso work with?",
            "output": "Appliso works with various industries, including finance, healthcare, e-commerce, and education, providing tailored technology solutions."
        },
        {
            "input": "How does Appliso support startups with funding?",
            "output": "Appliso connects startups with potential investors and provides mentorship to help secure funding for their projects."
        },
        {
            "input": "Does Appliso develop mobile applications?",
            "output": "Yes, Appliso specializes in developing mobile applications for iOS and Android using React Native and Flutter."
        },
        {
            "input": "Does Appliso offer cybersecurity solutions?",
            "output": "Yes, Appliso provides cybersecurity solutions, including penetration testing and security audits, to protect businesses from cyber threats."
        },
        {
            "input": "What is Appliso’s approach to Agile development?",
            "output": "Appliso follows Agile methodologies to ensure fast iteration, continuous feedback, and efficient product development."
        },
        {
            "input": "How does Appliso help businesses with data analytics?",
            "output": "Appliso offers data analytics services, including business intelligence solutions, predictive analytics, and AI-powered insights."
        },
        {
            "input": "Does Appliso support blockchain development?",
            "output": "Yes, Appliso provides blockchain development services, including smart contracts, decentralized apps, and secure digital transactions."
        },
        {
            "input": "Can Appliso help businesses implement AI solutions?",
            "output": "Yes, Appliso assists businesses in integrating AI-powered solutions to enhance automation and decision-making."
        },
        {
            "input": "Does Appliso provide e-commerce solutions?",
            "output": "Yes, Appliso develops e-commerce platforms with payment gateway integration, inventory management, and user-friendly interfaces."
        },
        {
            "input": "How does Appliso assist with digital transformation?",
            "output": "Appliso helps businesses transition to digital-first operations through modern technology adoption and automation strategies."
        },
        {
            "input": "What project management tools does Appliso use?",
            "output": "Appliso uses tools like Jira, Trello, and Asana for efficient project management and collaboration."
        },
        {
            "input": "Does Appliso offer DevOps services?",
            "output": "Yes, Appliso provides DevOps services, including CI/CD automation, infrastructure management, and performance optimization."
        },
        {
            "input": "What payment integrations does Appliso support?",
            "output": "Appliso integrates various payment solutions, including PayPal, Stripe, Flutterwave, and Paystack, into applications."
        },
        {
            "input": "How does Appliso ensure software quality?",
            "output": "Appliso follows rigorous software testing processes, including automated testing, manual QA, and continuous monitoring."
        },
        {
            "input": "Does Appliso offer internship programs?",
            "output": "Yes, Appliso provides internship opportunities for students and young professionals looking to gain hands-on tech experience."
        },
        {
            "input": "What is Appliso’s approach to user research?",
            "output": "Appliso conducts user research through surveys, usability testing, and analytics to enhance product usability and customer satisfaction."
        },
        {
            "input": "Does Appliso provide enterprise software solutions?",
            "output": "Yes, Appliso develops enterprise-grade software solutions tailored to business needs, ensuring scalability and security."
        },
        {
            "input": "How does Appliso assist with SEO optimization?",
            "output": "Appliso provides SEO services, including keyword research, on-page optimization, and technical SEO improvements."
        },
        {
            "input": "What frameworks does Appliso use for web development?",
            "output": "Appliso leverages frameworks like React.js, Next.js, and Vue.js for modern and scalable web applications."
        },
        {
            "input": "Does Appliso provide SaaS development services?",
            "output": "Yes, Appliso specializes in building scalable SaaS platforms with cloud integration and multi-tenant architecture."
        },
        {
            "input": "How does Appliso handle API development?",
            "output": "Appliso designs and develops robust APIs using RESTful and GraphQL architectures to enable seamless system integrations."
        }
    ]
    return appliso_data

import lamini

# Set the API key
lamini.api_key = "b596ac20dc9e73a832131ea20cb3997c0e78039ec8dd53ac24b53bc79323e2d0"

# Initialize the Lamini model
llm = lamini.Lamini("meta-llama/Meta-Llama-3.1-8B-Instruct")

# Get the dataset
data = get_data()

# Fine-tune the model on the dataset
llm.tune(data_or_dataset_id=data,
         finetune_args={"learning_rate": 1e-5},
         )


# COmmon hyperparameters that cna be used
# learning_rate: float = 1e-5
# num_train_epochs: int = 3
# batch_size: int = 4
# weight_decay: float = 0.01
# early_stopping_patience: int = 3