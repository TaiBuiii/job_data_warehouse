job_roles_mapping = {
    "software engineer": [
        "Lập Trình Viên", "Developer", "Software Engineer", "Kỹ Sư Phần Mềm",
        "Backend Developer", "Frontend Developer", "Fullstack Developer",
        "Mobile Developer", "Game Developer", "Java Developer", "C# Developer",
        "Python Developer", "Nodejs Developer", "Reactjs Developer","mobile app"
    ],
    "AI engineer": [
        "AI Engineer", "Machine Learning Engineer", "Deep Learning Engineer",
        "Kỹ Sư AI", "Kỹ Sư Machine Learning", "Computer Vision", "NLP Engineer"
    ],
    "web developer": [
        "Web Developer", "Lập Trình Web", "Fullstack Web", "Frontend Web", "Backend Web",
        "HTML", "CSS", "HTML-CSS", "UI-UX", "UI/UX Designer", "React Native", "PHP Developer"
    ],
    "IT support": [
        "IT Helpdesk", "IT Support", "IT Staff", "IT Executive", "IT Service Desk",
        "IT Infrastructure", "IT Operator", "IT Monitoring", "IT Customer Support"
    ],
    "data engineer": [
        "Data Engineer", "Big Data Engineer", "Kỹ Sư Dữ Liệu"
    ],
    "data scientist": [
        "Data Scientist", "Nhà Khoa Học Dữ Liệu",'automation & analytics'
    ],
    "data analyst": [
        "Data Analyst", "Phân Tích Dữ Liệu", "Business Analyst", "BA", "DA",
        "Financial Analyst", "Planning Analyst"
    ],
    "tester / QA": [
        "Tester", "QA", "QA Engineer", "Automation Tester", "Manual Tester",
        "Kiểm Thử", "Process Quality Assurance", "PQA", "Quality Assurance"
    ],
    "devOps engineer": [
        "DevOps", "DevOps Engineer", "Site Reliability Engineer", "SRE"
    ],
    "system administrator": [
        "System Admin", "SysAdmin", "Quản Trị Hệ Thống", "IT System Leader"
    ],
    "cybersecurity engineer": [
        "Cybersecurity Engineer", "Security Engineer", "An Toàn Thông Tin",
        "An Toàn Mạng", "Application Security", "SOC"
    ],
    "sales representative": [
        "Sales", "Nhân Viên Kinh Doanh", "Chuyên Viên Kinh Doanh", "B2B Sales",
        "Kinh Doanh"
    ],
    "specialist": [
        "Specialist", "Chuyên Viên", "Executive"
    ],
    "manager": [
        "Manager", "Quản Lý", "Trưởng Phòng", "Giám Đốc Bộ Phận",
        "Leader", "Team Leader", "Technical Lead", "Tech Lead", "Project Leader",
        "Scrum Master"
    ],
    "intern": [
        "Intern", "Internship", "Thực Tập Sinh", "Trainee"
    ],
    "bridge engineer": [
        "BrSE", "Bridge SE", "Bridge Engineer", "IT Communicator", "IT Comtor",'brse tieng nhat'
    ],
    "game developer": [
        "Game Developer", "Unity", "Unity Developer", "Unreal", "Game Programmer",
        "Gameplay Programmer","in game"
    ],
    "designer": [
        "Designer", "Graphic Designer", "Thiết Kế Đồ Họa", "UI Designer", "UX Designer",
        "UI/UX Designer", "Visual Designer", "Motion Graphic Designer",
        "3D Artist", "2D Artist", "Animator", "Concept Artist",
        "Product Designer", "Creative Designer", "Art Director"
    ],
    "product owner": [
        "Product Owner", "PO", "Product Manager", "Phụ Trách Sản Phẩm"
    ],
    "solution architect": [
        "Solution Architect", "Software Architect", "Technical Architect"
    ],
    "consultant": [
        "Consultant", "Solution Consultant", "Implementation Consultant", "SAP Consultant"
    ],
    "database administrator": [
        "Database Administrator", "DBA", "Oracle Database Administrator"
    ],
    "project assistant": [
        "Project Assistant", "Project Coordinator", "Thư Ký Dự Án"
    ],
    "embedded developer":[
        "embedded",'Nhung','Lap trinh Nhung','embedded developer'
    ],
    "business analysis":[
        'phan tich nghiep vu', 'ba','Business Analysis'
    ]
}
programming_languages_mapping = [
    "python", "java", "c", "c++", "c#", "r", "scala", "php", "ruby", "go", "rust", 
    "kotlin", "swift", "dart", "typescript", "javascript", "html", "css", "bash", 
    "shell", "perl", "lua", "matlab", "objective-c", "visual basic", "f#", "haskell",
    "fortran", "ada", "sql", "postgresql", "mysql", "oracle", "mongodb", "redis", 
    "cassandra", "elasticsearch", "pl/sql", "tsql", "graphql","nosql"
]

required_skills_mapping = [
    # ================= Software Engineer =================
    "git", "github", "gitlab", "bitbucket",
    "docker", "kubernetes", "openshift",
    "react", "angular", "vue", "nextjs", "nuxtjs",
    "django", "flask", "spring", "express", "nodejs", "fastapi",
    "junit", "pytest", "selenium", "cypress", "playwright",

    # ================= Designer =================
    "figma", "photoshop", "illustrator", "adobe xd",
    "after effects", "indesign", "sketch", "coreldraw", "canva",

    # ================= Specialist / General =================
    "project management", "communication", "scrum", "agile",
    "jira", "confluence", "trello", "asana", "slack",

    # ================= Sales Representative =================
    "crm", "salesforce", "hubspot", "excel", "powerpoint",
    "google analytics", "customer service",

    # ================= Manager =================
    "leadership", "team management", "budgeting",
    "resource planning", "agile", "scrum",

    # ================= Data Analyst =================
    "sql", "excel", "tableau", "powerbi", "qlik", "looker", "metabase", "superset",
    "sas", "stata", "spss", "google analytics", "data visualization",

    # ================= Intern =================
    "teamwork", "communication", "git", "office", "excel",

    # ================= Tester / QA =================
    "selenium", "pytest", "junit", "cypress", "postman", "soapui",
    "jmeter", "loadrunner", "qtp", "testng", "karate", "playwright",

    # ================= AI Engineer =================
    "tensorflow", "keras", "pytorch", "scikit-learn", "xgboost", "lightgbm",
    "catboost", "opencv", "transformers", "nltk", "spacy", "gensim",
    "mlflow", "dvc", "ray", "horovod", "onnx",

    # ================= IT Support =================
    "windows server", "linux", "unix", "vpn", "firewall",
    "active directory", "service desk", "helpdesk", "vmware", "citrix",

    # ================= Web Developer =================
    "react", "angular", "vue", "nextjs", "nuxtjs",
    "django", "flask", "fastapi", "nodejs", "express",
    "bootstrap", "tailwindcss",

    # ================= DevOps Engineer =================
    "docker", "kubernetes", "terraform", "ansible", "puppet", "chef",
    "jenkins", "gitlab ci", "github actions", "circleci", "travisci",
    "prometheus", "grafana", "nagios", "zabbix", "elk", "splunk",
    "aws", "gcp", "azure", "databricks", "redshift", "s3", "lambda", "ec2", "eks", "cloudformation",

    # ================= Product Owner =================
    "scrum", "agile", "backlog management", "product roadmap",

    # ================= Data Engineer =================
    "spark", "pyspark", "hadoop", "hive", "kafka", "flink", "storm",
    "airflow", "luigi", "prefect", "dbt", "glue",
    "snowflake", "bigquery", "synapse", "databricks", "redshift",

    # ================= System Administrator =================
    "linux", "unix", "windows server", "bash", "shell",
    "vpn", "firewall", "nagios", "zabbix", "prometheus", "vmware", "hyper-v",

    # ================= Cybersecurity Engineer =================
    "penetration testing", "ethical hacking", "owasp", "burpsuite", "metasploit",
    "splunk", "wireshark", "ids", "ips", "siem", "security auditing",
    "iso 27001", "nist", "gdpr", "hipaa",

    # ================= Bridge Engineer =================
    "bilingual", "translation", "communication", "coordination",

    # ================= Solution Architect =================
    "aws", "gcp", "azure", "architecture", "cloud design",
    "docker", "kubernetes", "terraform",

    # ================= Embedded Developer =================
    "embedded c", "microcontroller", "arduino", "raspberry pi", "stm32",
    "rtos", "firmware", "cortex-m", "esp32", "fpga", "vhdl", "verilog",

    # ================= Data Scientist =================
    "pandas", "numpy", "scikit-learn", "pytorch", "tensorflow",
    "xgboost", "matplotlib", "seaborn", "statsmodels",
    "mlflow", "dvc", "databricks",

    # ================= Consultant =================
    "communication", "business analysis", "stakeholder management",

    # ================= Game Developer =================
    "unity", "unreal engine", "cocos2d", "cryengine",
    "3d modeling", "blender", "maya",

    # ================= Project Assistant =================
    "project management", "ms project", "teamwork", "communication",

    # ================= Database Administrator =================
    "mongodb", "cassandra",
    "redis", "elasticsearch", "mariadb", "cockroachdb"
]

education_mapping = {
    "university" : 'đại học',
    "college" : "cao đẳng",
    "intermediate" : 'trung cấp',
    "high school" : 'phổ thông',
    "secondary school" : 'cơ sở'
}

position_mapping = {
    "staff": "Nhân viên",
    "team leader": "Trưởng nhóm",
    "intern": "Thực tập sinh",
    "manager": "Quản lý / Giám sát",
    "head/deputy of department": "Trưởng/Phó phòng",
    "director": "Giám đốc",
    "branch manager": "Trưởng chi nhánh"
}
location_mapping = [
    "an giang",
    "ba ria vung tau",
    "bac giang",
    "bac kan",
    "bac lieu",
    "bac ninh",
    "ben tre",
    "binh dinh",
    "binh duong",
    "binh phuoc",
    "binh thuan",
    "ca mau",
    "can tho",
    "cao bang",
    "dak lak",
    "dak nong",
    "dien bien",
    "dong nai",
    "dong thap",
    "gia lai",
    "ha giang",
    "ha nam",
    "ha noi",
    "ha tinh",
    "hai duong",
    "hai phong",
    "hau giang",
    "hoa binh",
    "hung yen",
    "khanh hoa",
    "kien giang",
    "kon tum",
    "lai chau",
    "lam dong",
    "lang son",
    "lao cai",
    "long an",
    "nam dinh",
    "nghe an",
    "ninh binh",
    "ninh thuan",
    "phu tho",
    "phu yen",
    "quang binh",
    "quang nam",
    "quang ngai",
    "quang ninh",
    "quang tri",
    "soc trang",
    "son la",
    "tay ninh",
    "thai binh",
    "thai nguyen",
    "thanh hoa",
    "thua thien hue",
    "tien giang",
    "ho chi minh",
    "tra vinh",
    "tuyen quang",
    "vinh long",
    "vinh phuc",
    "yen bai",
    "nuoc ngoai",
    "nhat ban"
]
